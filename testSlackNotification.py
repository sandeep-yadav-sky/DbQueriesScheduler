import unittest
from slackNotification import SlackNotification 

class testExecuteQuery(unittest.TestCase):

    def test_slackNotification(self):
        self.assertEqual(SlackNotification().post_to_slack_channel("hello","hi"),"success")


if __name__ == '__main__':
    unittest.main()
