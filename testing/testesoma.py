import unittest
from src.main import soma


class TesteSoma(unittest.TestCase):
    def test_retorno_soma(self):
        self.assertEqual(soma(10, 10), 20)
