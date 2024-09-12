from edupage_api import Edupage
from dotenv import dotenv_values
#-> Configs laden
config = dotenv_values('./.env')

edupage = Edupage()

try:
    edupage.login(config['LOGIN_USERNAME'], config['LOGIN_PASSWORD'], config['SCHOOL_SUBDOMAIN'])
except:
    raise Exception('LOGIN_ERROR: wrong username/password')

def getEdupage():
    return edupage