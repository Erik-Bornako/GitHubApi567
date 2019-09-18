from Erik_Bornako_SSW567_HW04a import get_commits, get_repos
import unittest

class TestHW04(unittest.TestCase):
    
    def test_get_repos(self):

        self.assertEqual(get_repos("richkempinski"), ['hellogitworld', 'helloworld', 'Mocks', 'Project1', 'threads-of-life'])
    
    def test_get_commits(self):

        self.assertEqual(get_commits("richkempinski",'hellogitworld'), 30)
        self.assertEqual(get_commits("richkempinski",'Project1'), 2)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)