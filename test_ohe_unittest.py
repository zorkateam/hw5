import unittest
from one_hot_encoder import fit_transform


class TestFT(unittest.TestCase):
    def test_ft(self):
        # test function to test result
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [('Moscow', [0, 0, 1]),
                    ('New York', [0, 1, 0]),
                    ('Moscow', [0, 0, 1]),
                    ('London', [1, 0, 0])]
        self.assertEqual(actual, expected)

    def test_empty(self):
        # test function to test result
        actual = fit_transform([])
        expected = []
        self.assertEqual(actual, expected)

    def test_not_empty(self):
        # test function to test empty result
        actual = fit_transform('Moscow')
        self.assertTrue(actual)

    def test_exception(self):
        # test function to test raise TypeError exception
        self.assertRaises(TypeError, fit_transform, )

    def test_notIN(self):
        # test function to test whether key is present in container
        actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
        expected = [('Ptz', [0, 0, 1])]
        # error message in case if test case got failed
        msg = 'Key is present in container'
        # assertNotIn() to check if key is in container
        self.assertNotIn(actual, expected, msg)
