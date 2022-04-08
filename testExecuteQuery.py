import unittest
from executeQuery import executeQuery 

class testExecuteQuery(unittest.TestCase):

    def test_executeQuery(self):
        self.assertEqual(executeQuery(),"success")


if __name__ == '__main__':
    unittest.main()
