"""
to execute this test: 
    python -m unittest tests.py
"""

from unittest import TestCase
from unittest.mock import patch

from helloworld import do_hello, URL

class FakeResult:
    text = '<title>"Hello, World!" program - Wikipedia</title>'

class TestHelloWorld(TestCase):
    """Tests to ensure that helloworld runs propoerly"""
    @patch('helloworld.requests.get')
    def test_do_hello(self, mock_get):
        mock_get.return_value = FakeResult()

        do_hello()
        mock_get.assert_called_once_with(URL)

if __name__ == '__main__':
    from unittest import main
    main()