from daleria_archives.views import home_page

from django.core.urlresolvers import resolve
from django.test import TestCase

class PageLoadsTest(TestCase):

    def test_archive_homepage_loads(self):
        home_page_candidate = resolve('/')
        self.assertEqual(home_page_candidate.func,
                         home_page,
                         'root url not resolving to homepage')
