import unittest
from src.llm_integration import get_llm_response

class TestLLMIntegration(unittest.TestCase):
    def test_llm_response(self):
        query = "What was the revenue of Flipkart for 2023?"
        response = get_llm_response(query)
        self.assertIn('company', response)
        self.assertIn('parameter', response)

if __name__ == "__main__":
    unittest.main()
