from bottle import post, request
import re
import pdb
import json
@post('/index', method='post')
def my_form():
    questions = {}
    mail = request.forms.get('ADRESS')
    qwer =  request.forms.get('QUEST')
    if qwer=="" or  mail=="":
         return "Not all fields are filled "
    else:
        match = re.search ('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,5}$', mail)
        if match!=None:
            questions[mail]=qwer
            with open ('data.txt','a') as outfile:
                jp = json.dumps(questions)
                open('data.txt','a').write('\n'+jp)
            return "Thanks! The answer will be sent to the mail %s" % mail
        else:
            return "This mail doesn't exist %s"% mail
 ##       pdb.set_trace()