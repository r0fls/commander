import unittest
import connect, os

COMMAND="cd {}; ls".format(os.getcwd())
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