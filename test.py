from bottle import post, request, route, run, redirect,put
import re
import pdb  
import json
@post('/test', method="post")
def Entry_form():
    #инициализация переменных из test.tpl
    author = request.forms.get('Author')
    news = request.forms.get('News')
    date = request.forms.get('Date')
    telefhone = request.forms.get('Telefhone')
    # открытие файла для чтения
    #f=open("test1.txt","a",encoding="utf-8")
    #f.writelines("---"+"\n")#запись в файл 
   # f.writelines(author +"\n")
   # f.writelines(news +"\n")
   # f.writelines(date +"\n")
  #  f.writelines(telefhone+"\n")
  #  f.close()
    #return  ('''<h2 align=center>You added your article</h2>'''+"<br>"+'''

    match = '^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$'
    if author=="" or  news=="" or  date=="" or  telefhone=="":
         return "Not all fields are filled "
    else:
         if (re.search(match, telefhone)):
             # открытие файла для чтения
             f=open("test1.txt","a",encoding="utf-8")
             f.writelines("---"+"\n")#запись в файл 
             f.writelines(author +"\n")
             f.writelines(news +"\n")
             f.writelines(date +"\n")
             f.writelines(telefhone+"\n")
             return  ('''<h2 align=center>You added your article</h2>'''+"<br>"+'''
    <style>
    <!--стили для конопки с подтверждением-->
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
        <p><a href="/test"><input class=h4  type="submit" value="Back"></a></p>''')
          
         else:
               return "invalid number"
