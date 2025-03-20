from unittest import TestCase
from unittest.mock import patch
from scraper import PlantScraper


base_url = "https://naman.com"
page_url = "https://naman.com/page={}"


class TestPlantScraper(TestCase):
    def setUp(self):
        self.scraper = PlantScraper(base_url, page_url)
        
    def test_extract_plant_names_single_line_format(self):
        """test case for single line format"""
        test_text = "Plants included: 1. Plant A 2. Plant B 3. Combo Plant"
        expected = ["Plant A", "Plant B", "Combo Plant"]
        result = self.scraper.extract_plant_names(test_text)
        self.assertEqual(result, expected)
        
    def test_extract_plant_names_newline_format(self):
        """test case for newline-separated text"""
        test_text = "1. Plant A\n2. Plant B Variegated\n3. Plant C Combo Variegated"
        expected = ["Plant A", "Plant B Variegated", "Plant C Combo Variegated"]
        result = self.scraper.extract_plant_names(test_text)
        self.assertEqual(result, expected)
        
    def test_extract_plant_names_empty_input(self):
        """test case for empty input"""
        result = self.scraper.extract_plant_names("")
        self.assertEqual(result, [])

    @patch('requests.get')
    def test_make_request(self, mock_get):
        """test case for HTTP request"""
        mock_get.return_value.text = "content"
        result = self.scraper.make_request(base_url)
        self.assertEqual(result, "content")