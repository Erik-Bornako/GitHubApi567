from Erik_Bornako_SSW567_HW04a import get_commits, get_repos
import unittest
from unittest.mock import patch, Mock
import requests
import json
from requests.models import Response

class TestHW04(unittest.TestCase):

    @patch('requests.get')
    def test_get_repos(self, injectedMock):
        json_str = b'[{"name":"repo1"}, {"name":"repo2"}]'
        the_response = Response()
        the_response._content = json_str
        injectedMock.return_value = the_response

        self.assertEqual(get_repos("richkempinski"), ['repo1', 'repo2'])
    
    @patch('requests.get')
    def test_get_commits(self, injectedMock):
        json_str = b'[{"commit":"blahh"}, {"commit":"blahhh"}, {"commit":"blahhh"}]'
        the_response = Response()
        the_response._content = json_str
        injectedMock.return_value = the_response

        self.assertEqual(get_commits("richkempinski",'hellogitworld'), 3)
        self.assertEqual(get_commits("richkempinski",'Project1'), 3)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)