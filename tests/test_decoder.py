import unittest
from g2fa_secret_extractor.decoder import decode_data

class TestDecoder(unittest.TestCase):
    def test_decode_data(self):
        data = "SGVsbG8gd29ybGQ"
        decoded_data = decode_data(data)
        self.assertEqual(decoded_data.decode("utf-8"), "Hello world")

if __name__ == "__main__":
    unittest.main()
