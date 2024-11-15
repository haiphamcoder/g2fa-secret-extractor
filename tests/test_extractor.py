import unittest
from g2fa_secret_extractor.extractor import extract_secret_key

class TestExtractor(unittest.TestCase):
    def test_extract_secret_key(self):
        uri = "otpauth-migration://offline?data=SGVsbG8gd29ybGQ"
        secret_key = extract_secret_key(uri)
        self.assertEqual(secret_key, "Hello world")

if __name__ == "__main__":
    unittest.main()
