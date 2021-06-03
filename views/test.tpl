% rebase('layout.tpl', title=title)
<form method="post" action="/test" class="form">
%with open("test1.txt",encoding="utf-8") as file:
   %int_number = file.read()
<style>
    .form textarea {
        width: 400px;
        max-width: 400px;
        min-width: 400px;
        line-height: 150%;
    }
</style>
<h2>{{ title }}</h2>
<h3>Latest news</h3>
<textarea id="text" name="text" rows ="10">{{int_number}}</textarea>
<body>
    <div  class=block-left id=left>
     <p>
         <label for="Author"><span class="formTextRed">*</span> Author:</label>
         <input type="text" name="Author" id="author" />
     </p>

     <p>
         <label for="News"><span class="formTextRed">*</span> News:</label>
         <input type="text" name="News" id="news" />
     </p>

     <p>
         <label for="Date"><span class="formTextRed">*</span> Date:</label>
         <input type="text" name="Date" id="date" />
     </p>

     <p>
         <class="submit">
         <input type="submit" velues="Send" />
     </p>
     </div>
</body>