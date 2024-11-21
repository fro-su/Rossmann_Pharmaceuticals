import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.utils import *

class TestDataAnalysisFunctions(unittest.TestCase):

    def setUp(self):
        # Create test data
        self.df = pd.DataFrame({
            'A': [1, 2, None, 4],
            'B': [None, 2, 3, 4],
            'C': ['x', 'y', 'z', 'w'],
            'D': [1, 2, 2, 4]
        })

        self.duplicate_df = pd.DataFrame({
            'ID': [1, 2, 2, 3],
            'Value': [10, 20, 20, 30]
        })

        self.numeric_df = pd.DataFrame({
            'A': [1, 2, -3, 4],
            'B': [100, 200, 300, 400]
        })

        self.date_df1 = pd.DataFrame({
            'Date1': ['2024-01-01', '2024-01-02', '2024-01-03'],
            'Value1': [10, 20, 30]
        })

        self.date_df2 = pd.DataFrame({
            'Date2': ['2024-01-02', '2024-01-03', '2024-01-04'],
            'Value2': [100, 200, 300]
        })


    def test_check_missing_data(self):
        result = check_missing_data(self.df)
        expected = pd.DataFrame({
            'Column Name': ['A', 'B'],
            'Missing Values': [1, 1],
            'Percentage Missing': [25.0, 25.0]
        })
        assert_frame_equal(result.reset_index(drop=True), expected)
    

    def test_get_total_missing_percentage(self):
        result = get_total_missing_percentage(self.df)
        self.assertEqual(result, 12.5)
    
    def test_check_duplicates(self):
        result = check_duplicates(self.duplicate_df)
        expected = pd.DataFrame({
            'ID': [2],
            'Number of Duplicates': [2]
        })
        assert_frame_equal(result.reset_index(drop=True), expected)
    
    def test_check_data_types(self):
        result = check_data_types(self.df)
        self.assertEqual(result, "Success: Data types per column are uniform.")


    

if __name__ == '__main__':
    unittest.main()
