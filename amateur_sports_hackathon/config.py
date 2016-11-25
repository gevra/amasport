"""
after cloning the code one must first run
git update-index --assume-unchanged amateur_sports_hackathon/config.py
to tell git not to track the changes to the config file and then put the config info
"""


class Config:
    def __init__(self):
        # for database
        self.DBNAME = 'your_db_name'
        self.DBUSER = 'your_db_user_name'
        self.DBPASSWORD = 'your_db_user_password'
        self.HOST = 'localhost'
        self.PORT = ''  # Set to empty string for default.

        # for project
        self.DEBUG = False
        self.TEMPLATE_DEBUG = False
        self.SECRET_KEY = 'your_django_project_secret_key'

config = Config()

