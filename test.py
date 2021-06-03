from bottle import post, request, route, run, redirect,put
import re
import pdb  
import json
@post('/test', method="post")
def Entry_form():
    author = request.forms.get('Author')
    news = request.forms.get('News')
    date = request.forms.get('Date')
    #telefhone = request.forms.get('Telefhone')
    f=open("test1.txt","a",encoding="utf-8")
    f.writelines("---"+"\n")
    f.writelines(author+"\n")
    f.writelines(news+"\n")
    f.writelines(date+"\n")
    #f.writelines(telefhone+"\n")
    f.close()
    return  ('''<h2 align=center> </h2>'''+"<br>"+'''
    <style>

        h2
        {
        font-size: 200%;
        font-family: Verdana, Arial, Helvetica, sans-serif;
        color: #808080;
        }
        .h4 {
        border-radius: 12px;
        background: wight;
        border-color: #cccccc;
        color: black;
        font-size: 9pt;
        height: 70px;
        width: 200px;
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%,0);
        }
    </style>
        <p><a href="/test">Back<input class=h4  type="submit" value="Back"></a></p>''')