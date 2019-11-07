from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status


class BondCategoriesTest(TestCase):
    fixtures = ['bonds_data.json']

    def test_get_all_bond_categories(self):
        """
        Make a GET request to endpoint "bond/api/bond-categories" to
        1. get all bond categories data
        2. get bond categories using search
        """
        url = reverse_lazy('pbm_bonds:bond_categories')

        # get all bond categories
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        api_index_data = r.json()
        self.assertIsNotNone(api_index_data)
        self.assertIsNot(len(api_index_data), 0)
        self.assertEqual(api_index_data[0]['category'], '7500')


class BondDrawDatesTest(TestCase):
    fixtures = ['bonds_data.json']

    def test_get_bond_draw_dates(self):
        """
        Make a GET request to endpoint "api/draw-dates/(?P<category>[0-9]+)" to
        1. get bond draw dates data
        """
        # Without bond in url
        url = reverse_lazy('pbm_bonds:bond_draw_dates')

        # get bond draw dates
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        api_index_data = r.json()
        self.assertIsNotNone(api_index_data)
        self.assertEqual(len(api_index_data), 0)

        # With bond in url
        url = reverse_lazy('pbm_bonds:bond_draw_dates', args=('7500',))

        # get bond draw dates
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)

        api_index_data = r.json()
        self.assertIsNotNone(api_index_data)
        self.assertIsNot(len(api_index_data), 0)
