% rebase('layout.tpl', title=title)
<form method="post" action="/test" class="form">
<!--�������� ����� ��� ������ ����������-->
%with open("test1.txt",encoding="utf-8") as file:
   %int_number = file.read()
<!--����� ��� ������ � ������� -->
<style>
    .block-left {
        width:50%;
        height:800px;
        overflow:auto;
        float:left;
    }
    .block-right{
    width:50%;
    height:800px;
    overflow:auto;
    }

    body {
        background: #F6F9F9;
    }

    .form input, .form textarea, .form select 
    {
        padding: 9px;
        border: 1px solid #E5E5E5;
        border-radius: 5px;
    }
    .form textarea
    {
        width: 400px;
        max-width: 400px;
        min-width: 400px;
        line-height: 150%;
        resize: none;
    }
</style>
<body>
    <div  class=block-left id=left>
    <h2>News</h2>
    <h3>Latest news</h3>
    <!--���� ��� ������ ����������� �����-->
    <textarea id="text" name="text" rows ="10" readonly>{{int_number}}</textarea>
    </div>
    <!--����� ����� � ������ ������� -->
    <div class=block-right>
    <br>
    <!--���� ��� ����� ������-->
     <p>
         <label for="Author"><span class="formTextRed">*</span> Author:</label>
         <input type="text" name="Author" id="author" />
     </p>
     <!--���� ��� ����� ��������-->
     <p>
         <label for="News"><span class="formTextRed">*</span> News:</label>
         <textarea class=textarea1 rows="10" name="News" id="news"></textarea>
     </p>
     <p>
         <label for="Telefhone"><span class="formTextRed">*</span> Telefhone:</label>
         <input type="text" name="Telefhone" id="Telefhone" />
     </p>
     <!--���� ��� ����� ����-->
     <p>
         <label for="Date"><span class="formTextRed">*</span> Date:</label>
         <input type="date" name="Date" id="date" />
     </p>

     <p>
         <class="submit">
         <input type="submit" values="Send" />
     </p>
     <!--������ �����-->
     <p>
        <a class="btn btn-default" href=/home>Back</a>
     </p>
     </div>
</body>