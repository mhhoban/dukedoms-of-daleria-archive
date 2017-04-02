from daleria_archives.views import (home_page,
                                   full_list_page,
                                   request_list_page)
from daleria_archives.models import Card
from django.core import serializers
from django.core.urlresolvers import resolve
from django.test import TestCase
import HTMLParser

class CustomListPageTest(TestCase):

    def test_custom_list_page_loads(self):
        response = resolve('/request-list')
        self.assertEqual(response.func,
                         request_list_page,
                         'custom list page not properly resolving')

    def test_custom_list_page_serves_valid_request(self):
        response = self.client.post(
                   '/request-list',
                   data={"request_set":"[1,2,3]"}
                   )
        self.assertEqual(response.status_code,
                         200,
                         'custom_list not serving valid request')

    def test_custom_list_page_does_not_serve_invalid_request(self):
        get_response = self.client.get('/request-list')
        self.assertEqual(get_response.status_code,
                         404,
                         'custom_list serving get request')

        bad_data_response = self.client.post(
                            '/request-list',
                            data={"cards":"[1,2,3]"}                            )
        self.assertEqual(bad_data_response.status_code,
                         404,
                         'custom_list serving bad POST request')

class HomePageLoadsTest(TestCase):

    def test_archive_homepage_loads(self):
        response = resolve('/')
        self.assertEqual(response.func,
                         home_page,
                         'root url not resolving to homepage')

class FullListPageTest(TestCase):

    def unescape_html(self, html):
        parser = HTMLParser.HTMLParser()
        unescaped_html = parser.unescape(
            html
        )

        return unescaped_html

    def test_full_page_endpoint_loads(self):
        full_list_page_candidate = resolve('/full-list/')
        self.assertEqual(full_list_page_candidate.func,
                         full_list_page,
                         'Full List page not loading right endpoint')

    def test_full_db_contents_served(self):
        """
        Test that contents of db are being correctly served
        """
        Card.objects.create(
            name='test card 1',
            type='test type',
            cost=13,
            treasure=7,
            victory_points=7,
            actions='None'
        )
        Card.objects.create(
            name='test card 2',
            type='test type',
            cost=13,
            treasure=7,
            victory_points=7,
            actions='None'
        )

        response = self.client.get(
            '/full-list/'
        )

        response_content = self.unescape_html(response.content)
        cardDb_contents = serializers.serialize(
            'json',
            Card.objects.all()
        )

        self.assertEqual(
            str(response_content).strip(),
            str(cardDb_contents),
            'database serving incorrect data')
