from edupage_api import Edupage
from dotenv import dotenv_values
from ..api.api_handler import getEdupage

edupage = getEdupage()

def getStudentCount():
    allStudents = edupage.get_all_students()
    studentCount = len(allStudents)
    return studentCount