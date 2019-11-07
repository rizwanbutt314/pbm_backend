import config
import re
import argparse
import requests
import psycopg2
import psycopg2.extras
from bs4 import BeautifulSoup

header = {
    'Referer': 'http://savings.gov.pk/rs-7500-draws/',
    'Host': 'savings.gov.pk',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
}


def arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bond", help="Bond to scrap")
    args = parser.parse_args()
    return args


def make_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=config.PG_DATABASE,
            user=config.PG_USERNAME,
            password=config.PG_PASSWORD,
            host=config.PG_HOST,
            port=config.PG_PORT
        )
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return conn, cursor
    except psycopg2.DatabaseError:
        print("Connection Failed to database")
        return None, None


def make_get_request(HOME_URL):
    r = requests.get(HOME_URL, headers=header)
    soup = BeautifulSoup(r.text, 'html5lib')
    return soup


def make_text_file_request(url):
    response = requests.get(url)
    return response.text


def format_db_date(date):
    splitted_date = date.split('-')
    draw_year = splitted_date[2]
    draw_date = '{0}-{1}-{2}'.format(splitted_date[2], splitted_date[1], splitted_date[0])
    return draw_date, draw_year


def fetch_previous_bond_dates(table_name, bond_category):
    db_cnx, db_cur = make_db_connection()

    bond_dates_query = """SELECT date FROM pbm_bonds_bonddrawdates WHERE bond_category_id={bond_category_id}""".format(
        bond_category_id=bond_category
    )

    db_cur.execute(bond_dates_query)
    data = db_cur.fetchall()
    db_cnx.commit()
    db_cnx.close()

    return [str(db_row[0]) for db_row in data]


def fetch_available_bonds():
    db_cnx, db_cur = make_db_connection()

    bonds_query = """SELECT id, category FROM pbm_bonds_bondcategory"""

    db_cur.execute(bonds_query)
    data = db_cur.fetchall()
    db_cnx.commit()
    db_cnx.close()

    return {str(db_row[1]): db_row[0] for db_row in data}


def insert_bond_data(table_name, data):
    db_cnx, db_cur = make_db_connection()

    data = tuple(data)
    db_keys = list(data[0].keys())
    columns_string = ",".join(db_keys)

    values_list = ['%({0})s'.format(col) for col in db_keys]
    values_string = ",".join(values_list)

    bulk_insert_query = """INSERT INTO {table}({columns_string}) VALUES ({values_string})""".format(
        table=table_name,
        columns_string=columns_string,
        values_string=values_string
    )

    db_cur.executemany(bulk_insert_query, data)
    db_cnx.commit()
    db_cnx.close()


def insert_draw_dates(data):
    db_cnx, db_cur = make_db_connection()

    data = tuple(data)
    db_keys = list(data[0].keys())
    columns_string = ",".join(db_keys)

    values_list = ['%({0})s'.format(col) for col in db_keys]
    values_string = ",".join(values_list)

    bulk_insert_query = """INSERT INTO pbm_bonds_bonddrawdates({columns_string}) VALUES ({values_string})""".format(
        columns_string=columns_string,
        values_string=values_string
    )

    db_cur.executemany(bulk_insert_query, data)
    db_cnx.commit()
    db_cnx.close()


def extract_first_prize(content, year, date, bond_category):
    first_prize = re.findall(r'[0-9]+', content)
    bond_number = first_prize[0]
    db_object = {
        'year': year,
        'date': date,
        'bond_number': bond_number,
        'bond_level': 1,
        'bond_category_id': bond_category,
    }
    return db_object


def extract_second_prizes(content, year, date, bond_category):
    second_prizes = re.findall(r'[0-9]+', content)
    second_prizes_list = list()
    for bond_number in second_prizes:
        db_object = {
            'year': year,
            'date': date,
            'bond_number': bond_number,
            'bond_level': 2,
            'bond_category_id': bond_category,
        }
        second_prizes_list.append(db_object)
    return second_prizes_list


def extract_third_prizes(content, year, date, bond_category):
    third_prizes = re.findall(r'[0-9]+', content)

    third_prizes_list = list()
    for bond_number in third_prizes:
        db_object = {
            'year': year,
            'date': date,
            'bond_number': bond_number,
            'bond_level': 3,
            'bond_category_id': bond_category,
        }
        third_prizes_list.append(db_object)
    return third_prizes_list
