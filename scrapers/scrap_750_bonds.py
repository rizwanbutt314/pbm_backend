from utils import (
    extract_first_prize,
    extract_second_prizes,
    extract_third_prizes,
    insert_bond_data,
    insert_draw_dates,
    make_get_request,
    make_text_file_request,
    format_db_date,
    fetch_previous_bond_dates
)


def main(home_url, table_name, bond_category):
    print("Scraping 750 bonds data")
    bond_dates_links = list()
    new_bond_dates = list()

    bond_prev_dates = fetch_previous_bond_dates(table_name, bond_category)

    soup = make_get_request(home_url)
    try:
        dates_tables = soup.find_all('table', {'class': 'cmsms_table'})
    except:
        dates_tables = list()

    for table in dates_tables:
        dates_links = table.find_all('a')
        for date in dates_links:
            bond_text = date.get_text().strip()
            draw_date, draw_year = format_db_date(bond_text)
            if draw_date not in bond_prev_dates:
                bond_link = date['href']
                bond_dates_links.append([bond_link, draw_date, draw_year])
                new_bond_dates.append({
                    'year': draw_year,
                    'date': draw_date,
                    'bond_category_id': bond_category,
                })

    if new_bond_dates:
        # Save New draw dates
        insert_draw_dates(new_bond_dates)

    for draw_data in bond_dates_links:
        bond_link = draw_data[0]
        draw_date = draw_data[1]
        draw_year = draw_data[2]
        print("Link: ", bond_link)
        print("Date: ", draw_date)
        print("Year: ", draw_year)

        bond_file_data = make_text_file_request(bond_link)

        # Extracting bond numbers from list
        splitted_content = bond_file_data.split(
            '--------------------------------------------------------------------------')
        first_prize = extract_first_prize(splitted_content[1], draw_year, draw_date, bond_category)
        second_prizes = extract_second_prizes(splitted_content[2], draw_year, draw_date, bond_category)
        try:
            third_prizes = extract_third_prizes(splitted_content[4], draw_year, draw_date, bond_category)
        except:
            third_prizes = extract_third_prizes(splitted_content[3], draw_year, draw_date, bond_category)

        all_bonds = list()
        all_bonds.append(first_prize)
        all_bonds.extend(second_prizes)
        all_bonds.extend(third_prizes)

        insert_bond_data(table_name, all_bonds)

    print("Scraping 750 bonds data completed!")


if __name__ == "__main__":
    HOME_URL = 'http://savings.gov.pk/rs-750-draws/'
    TABLE_NAME = 'pbm_bonds_bond750'
    BOND_CATEGORY = 1
    main(HOME_URL, TABLE_NAME, BOND_CATEGORY)
