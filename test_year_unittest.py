import unittest
from what_is_year_now import what_is_year_now
from unittest.mock import patch, MagicMock
import urllib.request


class TestYear(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_year_now(self, mock_urlopen):
        cm = MagicMock()
        cm.read.return_value = '{"currentDateTime": "2019-03-01"}'
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm

        with urllib.request.urlopen('') as response:
            self.assertEqual(response.read(), '{"currentDateTime": "2019-03-01"}')
            actual = what_is_year_now()
            self.assertEqual(actual, 2019)

    @patch('urllib.request.urlopen')
    def test_year2(self, mock_urlopen):
        cm = MagicMock()
        cm.read.return_value = '{"currentDateTime": "01.03.2019"}'
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm

        with urllib.request.urlopen('') as response:
            self.assertEqual(response.read(), '{"currentDateTime": "01.03.2019"}')
            actual = what_is_year_now()
            self.assertEqual(actual, 2019)

    @patch('urllib.request.urlopen')
    def test_exception(self, mock_urlopen):
        cm = MagicMock()
        cm.read.return_value = '{"currentDateTime": "01/01/2022"}'
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm

        with urllib.request.urlopen('') as response:
            self.assertRaises(ValueError, what_is_year_now, )
