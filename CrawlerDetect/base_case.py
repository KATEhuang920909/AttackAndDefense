from unittest import TestCase

from detectmodel import DetectModel


class CrawlerDetectTestCase(TestCase):
    def setUp(self):
        self.cd = DetectModel()

    def tearDown(self):
        pass
