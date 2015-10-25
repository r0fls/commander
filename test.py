import unittest
import connect, os

DIR = os.environ.get('TRAVIS_BUILD_DIR') or os.getcwd()
COMMAND="cd {}; ls".format(DIR)
HOST="localhost"
class TestConnection(unittest.TestCase):
    global result
    result = connect.run(HOST,COMMAND) 
    def test_exists_result(self):
        self.assertTrue(result)
    def test_connect_in_result(self):
        self.assertTrue('connect.py' in str(result))

if __name__ == '__main__':
    unittest.main()
