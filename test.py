import unittest
import connect, os

DIR = os.environ.get('CI_HOME') or os.getcwd()
COMMAND="cd {0}; ls".format(DIR)
HOST="localhost"
result = connect.run(HOST,COMMAND) 

HOSTS = ["localhost" for i in range(5)]
COMMANDS = [COMMAND,"pwd","echo hello"]
results = connect.run_group(HOSTS,COMMANDS)

class TestConnection(unittest.TestCase):
    global result

    def test_exists_result(self):
        self.assertTrue(result)
    def test_connect_in_result(self):
        self.assertTrue('connect.py' in str(result))
    def test_result_has_keys(self):
        self.assertEqual(connect.results[HOST][COMMAND],result)

    # test group commands
    def test_result_group_dict(self):
        self.assertEqual(connect.results[HOST][COMMAND],results[HOST][COMMAND])
    # def test_result_has_keys(self):
    #    self.assertEqual(result_group,results)
     

if __name__ == '__main__':
    unittest.main()
