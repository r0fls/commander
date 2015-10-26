import unittest
import connect, os

DIR = os.environ.get('CI_HOME') or os.getcwd()
COMMAND="cd {0}; ls".format(DIR)
HOST="localhost"
class TestConnection(unittest.TestCase):
    global result
    result = connect.run(HOST,COMMAND) 
    def test_exists_result(self):
        self.assertTrue(result)
    def test_connect_in_result(self):
        self.assertTrue('connect.py' in str(result))
    def test_result_has_keys(self):
        self.assertEqual(connect.results[HOST][COMMAND],result)

if __name__ == '__main__':
    unittest.main()
