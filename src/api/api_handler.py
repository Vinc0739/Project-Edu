from edupage_api import Edupage
from dotenv import dotenv_values

# Keys von der .env Datei bekommen
env = dotenv_values('./src/bot/.env')

edupage = Edupage()
# edupage.login(env['LOGIN_USERNAME'], env['LOGIN_PASSWORD'], env['SCHOOL_SUBDOMAIN'])
def getUserData(username, password):
    try:
        edupage.login(username, password, env['SCHOOL_SUBDOMAIN'])
    except:
        return Exception('LOGIN_ERROR: wrong username/password')
    return edupage