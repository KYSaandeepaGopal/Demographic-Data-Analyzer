import unittest
import pandas as pd
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_demographic_analysis(self):
        result = demographic_data_analyzer.demographic_data_analyzer()
        self.assertIsInstance(result['race_count'], pd.Series)
        self.assertAlmostEqual(result['average_age_men'], 39.4, delta=0.1)
        self.assertAlmostEqual(result['percentage_bachelors'], 16.4, delta=0.1)
        self.assertAlmostEqual(result['higher_education_rich'], 46.5, delta=0.1)
        self.assertAlmostEqual(result['lower_education_rich'], 17.4, delta=0.1)
        self.assertEqual(result['min_work_hours'], 1)
        self.assertAlmostEqual(result['rich_min_workers_percentage'], 10.0, delta=0.1)
        self.assertEqual(result['highest_earning_country'], 'India')
        self.assertAlmostEqual(result['highest_earning_country_percentage'], 42.9, delta=0.1)
        self.assertEqual(result['top_IN_occupation'], 'Prof-specialty')

if __name__ == '__main__':
    unittest.main()
