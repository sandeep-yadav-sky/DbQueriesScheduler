# db authentication parameters
# import logging
import os
from datetime import datetime
import logging
from slackNotification import SlackNotification
notify = SlackNotification()

#using .env configurations
from dotenv import load_dotenv
load_dotenv()
dbHost = os.getenv('dbHost')
dbName = os.getenv('dbName')
dbUser = os.getenv('dbUser')
dbPassword = os.getenv('dbPassword')


dirPath = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dirPath, 'testLog.log')

# Library to make a connection to db
import psycopg2

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# configuring the logger for module
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def executeQuery():
    try:
        conn = psycopg2.connect(dbname = dbName, user = dbUser, password = dbPassword, host = dbHost)
        # creating a thread to execute query
        try:
            cur = conn.cursor()
            logger.info("connected successfully")
            # for just using same table name every time , i'll delete the old table
            try:
                cur.execute('drop table tb1')
            # executing the query and creating a table for the result of query
                cur.execute('select id, name, rollno into tb1 from person where id = 1')
                logger.info("query Executed successfully")
                notify.post_to_slack_channel("query Executed successfully","pyscript")

            except Exception as e:
                print(e + "cursor execution failed")
        except Exception as e:
            print(e + "cursor thread creation faled")

        #making changes persistant in the database
        conn.commit()

        #terminating the thread and connections
        cur.close()
        conn.close()
    except Exception as e:
        notify.post_to_slack_channel("connection failed","pyscript")
        logger.error(e, "connection failed")
    