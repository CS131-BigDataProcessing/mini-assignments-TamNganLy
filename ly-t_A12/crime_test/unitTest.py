import unittest
import pandas as pd
from validate_functions import validate_vict_sex, validate_vict_age
from stats_functions import calculate_mean_age, calculate_median_age

class TestValidateFunctions(unittest.TestCase):
    def setUp(self):
        # Valid DataFrame with proper columns
        self.valid_df = pd.DataFrame({
            'Vict Sex': ['M', 'F', 'M'],
            'Vict Age': [25, 30, 40]
        })

        # DataFrame with invalid 'Vict Sex' column
        self.invalid_sex_df = pd.DataFrame({
            'Vict Sex': ['M', 'X', None],
            'Vict Age': [25, 30, 40]
        })

        # DataFrame with invalid 'Vict Age' column
        self.invalid_age_df = pd.DataFrame({
            'Vict Sex': ['M', 'F', 'M'],
            'Vict Age': [0, 100, None]
        })

        # DataFrame with invalid 'Vict Age' column
        self.invalid_age_1_df = pd.DataFrame({
            'Vict Sex': ['M', 'F', 'M'],
            'Vict Age': [0, 150, 90]
        })

        # DataFrame missing 'Vict Sex' column
        self.missing_vict_sex_df = pd.DataFrame({
            'Vict Age': [25, 30, 40]
        })

        # DataFrame missing 'Vict Age' column
        self.missing_vict_age_df = pd.DataFrame({
            'Vict Sex': ['M', 'F', 'M']
        })

        self.empty_df = pd.DataFrame()

    def test_validate_vict_sex(self):
        self.assertTrue(validate_vict_sex(self.valid_df))
        self.assertFalse(validate_vict_sex(self.invalid_sex_df))
        self.assertFalse(validate_vict_sex(self.missing_vict_sex_df))
        self.assertFalse(validate_vict_sex(self.empty_df))

    def test_validate_vict_age(self):
        self.assertTrue(validate_vict_age(self.valid_df))
        self.assertFalse(validate_vict_age(self.invalid_age_df)) 
        self.assertFalse(validate_vict_age(self.invalid_age_1_df))      
        self.assertFalse(validate_vict_age(self.missing_vict_age_df))    
        self.assertFalse(validate_vict_age(self.empty_df))

class TestStatsFunction(unittest.TestCase):
    def setUp(self):
        # Valid DataFrame with proper columns
        self.valid_df = pd.DataFrame({'Vict Age': [25, 30, 40]})

        # Valid DataFrame with only one value
        self.single_df = pd.DataFrame({'Vict Age': [40]})

        # Valid DataFrame with identical values
        self.identical_df = pd.DataFrame({'Vict Age': [25, 25, 25]})

        # Valid DataFrame with even # of entries
        self.even_df = pd.DataFrame({'Vict Age': [25, 30, 35, 40]})

    def test_calculate_mean_age(self):
        self.assertAlmostEqual(calculate_mean_age(self.valid_df), 31.67, places=2)
        self.assertEqual(calculate_mean_age(self.single_df), 40)
        self.assertEqual(calculate_mean_age(self.identical_df), 25)

    def test_calculate_median_age(self):
        self.assertEqual(calculate_median_age(self.valid_df), 30)
        self.assertEqual(calculate_median_age(self.single_df), 40)
        self.assertEqual(calculate_median_age(self.even_df), 32.5)

if __name__ == '__main__':
    unittest.main()
