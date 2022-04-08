from distutils.log import error
import unittest
from slackNotification import SlackNotification 

def check():
    x = -1
    try:
        if x < 0:
            raise ValueError
    except Exception as e:
        pass


class testExecuteQuery(unittest.TestCase):

    def test_slackNotification(self):
        self.assertEqual(SlackNotification().post_to_slack_channel("hello","hi"),"success")
    def test_afunction_throws_exception(self):
        self.assertRaises(TypeError, check())

if __name__ == '__main__':
    unittest.main()
