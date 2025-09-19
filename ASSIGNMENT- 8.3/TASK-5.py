import unittest

from TASK-5 import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    def test_standard_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")

    def test_single_digit_month_day(self):
        self.assertEqual(convert_date_format("2023-1-5"), "5-1-2023")

    def test_leap_year(self):
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")

    def test_end_of_year(self):
        self.assertEqual(convert_date_format("2022-12-31"), "31-12-2022")

    def test_start_of_year(self):
        self.assertEqual(convert_date_format("2022-01-01"), "1-1-2022")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("15-10-2023")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_non_date_string(self):
        with self.assertRaises(ValueError):
            convert_date_format("not-a-date")

    def test_short_year(self):
        with self.assertRaises(ValueError):
            convert_date_format("23-10-15")

    def test_extra_spaces(self):
        self.assertEqual(convert_date_format(" 2023-10-15 "), "15-10-2023")

    def test_month_and_day_with_leading_zeros(self):
        self.assertEqual(convert_date_format("2023-04-09"), "9-4-2023")

    def test_all_zeros(self):
        self.assertEqual(convert_date_format("0000-00-00"), "0-0-0000")

    def test_large_year(self):
        self.assertEqual(convert_date_format("9999-12-31"), "31-12-9999")

if __name__ == "__main__":
    unittest.main()