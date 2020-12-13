import unittest
from time_calculator import split_time, make_time


class UnitTests(unittest.TestCase):

    def test_pm(self):
        actual = split_time("3:30 PM")
        expected = (15, 30, "PM")
        self.assertEqual(
            actual, expected, f'Expected calling "split_time()" with "3:30 PM" to return (15, 30), actual: {str(actual)}')

    def test_am(self):
        actual = split_time("3:30 AM")
        expected = (3, 30, "AM")
        self.assertEqual(
            actual, expected, f'Expected calling "split_time()" with "3:30 PM" to return (3, 30), actual: {str(actual)}')

    def test_24h(self):
        actual = split_time("15:30")
        expected = (15, 30, "")
        self.assertEqual(
            actual, expected, f'Expected calling "split_time()" with "15:30" to return (15, 30), actual: {str(actual)}')

    def test_24h_to_12h(self):
        actual = split_time("15:30", False)
        expected = (3, 30, 'PM')
        self.assertEqual(
            actual, expected, f"Expected calling split_time() with 15:30, False to return (3, 30), actual: {str(actual)}")

    def test_maketime_base(self):
        actual = make_time(630)
        expected = (10, 30, "AM", 0)
        self.assertEqual(
            actual, expected, f'Expected calling "make_time()" with 630 to return {str(expected)}')

    def test_maketime_nextday(self):
        actual = make_time(2070)
        expected = (10, 30, "AM", 1)
        self.assertEqual(
            actual, expected, f'Expected calling "make_time()" with 2070 to return {str(expected)}')

    def test_maketime_nextday_pm(self):
        actual = make_time(2165)
        expected = (12, 5, "PM", 1)
        self.assertEqual(
            actual, expected, f'Expected calling "make_time()" with 2165 to return {str(expected)}')

    def test_maketime_nextday_pm(self):
        actual = make_time(4950)
        expected = (10, 30, "AM", 3)
        self.assertEqual(
            actual, expected, f'Expected calling "make_time()" with 4950 to return {str(expected)}')


if __name__ == "__main__":
    unittest.main()
