from daleria_archives.views import home_page, full_list_page
from daleria_archives.models import Card
from django.core import serializers
from django.core.urlresolvers import resolve
from django.test import TestCase
import HTMLParser

class HomePageLoadsTest(TestCase):

    def test_archive_homepage_loads(self):
        home_page_candidate = resolve('/')
        self.assertEqual(home_page_candidate.func,
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

        self.assertEqual(str(response_content).strip(), str(cardDb_contents))
