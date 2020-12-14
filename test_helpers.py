import unittest
from time_calculator import split_time, make_time, add_time, weekday_after


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

    def test_weekday_after_same(self):
        actual = weekday_after('fRiDay')
        expected = "Friday"
        self.assertEqual(
            actual, expected, f'Expected calling "weekday_after" with "fRiDay" to return {str(expected)}')

    def test_weekday_after_2daylater(self):
        actual = weekday_after('TUESday', 2)
        expected = "Thursday"
        self.assertEqual(
            actual, expected, f'Expected calling "weekday_after" with "TUESday", 2 to return {str(expected)}')

    def test_weekday_after_rollover(self):
        actual = weekday_after('saturday', 3)
        expected = "Tuesday"
        self.assertEqual(
            actual, expected, f'Expected calling "weekday_after" with "saturday", 3 to return {str(expected)}')

    def test_same_period(self):
        actual = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        self.assertEqual(
            actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"')


if __name__ == "__main__":
    unittest.main()
