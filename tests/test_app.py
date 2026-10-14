import unittest
from app import app, properties, money

class CatalogueTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_and_full_catalogue(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        response = self.client.get('/?browse=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text.count('data-property-id='), 45)

    def test_all_details_and_missing_property(self):
        for prop in properties:
            response = self.client.get(f"/property/{prop['id']}?city=Pune")
            self.assertEqual(response.status_code, 200)
            self.assertIn(prop['title'], response.text)
            self.assertIn(prop['neighborhood'], response.text)
        self.assertEqual(self.client.get('/property/999').status_code, 404)

    def test_filters_and_sort_order(self):
        response = self.client.get('/?browse=1&state=Maharashtra&city=Pune&bedrooms=2')
        self.assertEqual(response.text.count('data-property-id='), 1)
        self.assertIn('Hinjewadi IT Flat', response.text)
        response = self.client.get('/?browse=1&sort=price_asc')
        self.assertLess(response.text.index('data-property-id="27"'), response.text.index('data-property-id="2"'))

    def test_empty_invalid_and_old_search(self):
        response = self.client.get('/?browse=1&price_range=50000000-999999999')
        self.assertIn('No homes match', response.text)
        self.assertEqual(response.text.count('data-property-id='), 0)
        self.assertEqual(self.client.get('/?browse=1&price_range=bad&bedrooms=oops').status_code, 200)
        response = self.client.post('/', data={'state':'Gujarat','city':'Surat'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text.count('data-property-id='), 3)

    def test_currency_and_assets(self):
        self.assertEqual(money(28000000), '₹2.8 Cr')
        self.assertEqual(money(5500000), '₹55 Lakh')
        for asset in ('style.css','app.js'):
            with self.client.get('/static/' + asset) as response:
                self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

