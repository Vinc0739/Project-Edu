from edupage_api import Edupage
from dotenv import dotenv_values
#-> Configs laden
env = dotenv_values('./src/configs/.env')

edupage = Edupage()

def getUserData():
    try:
        edupage.login(env['LOGIN_USERNAME'], env['LOGIN_PASSWORD'], env['SCHOOL_SUBDOMAIN'])
    except:
        raise Exception('LOGIN_ERROR: wrong username/password')
    return edupage