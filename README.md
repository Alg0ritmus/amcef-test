# amcef-test

## URLS:

'admin/'                      | admin dashboard (default django) <br>
'api/'                        | main page <br>
'api/posts/'                  | get all Posts from API <br>
'api/post/\<int\>/'           | get Post by it's ID <br>
'api/updatePost/\<int\>/'     | update Post <br>
'api/getPostByUsedId/\<int\>/'| get Post by User ID <br>
'api/createPost/'             | create Post <br>
'api/deletePost/\<int\>/'     | delete Post <br>

---
## Simple Info
APP is available on url: http://127.0.0.1:8000/api/ (locally -> py manage.py runserver).<br>
Main page contains 2 buttons (`Get By ID` & `Get By userId`) with associated fields and <br>
1 button for Post creation.<br><br>

ALL requests to backend ('api/..') are returning Python objects (because of using Django-templates)<br>
which means, that backend are NOT returning JSON obj (but it could be easily rewrited for JSON support<br>
in case we want to deal with real frontend framework/library).<br><br>

Every Create, Update, Delete request updates loacal DB (sqlite for simplicity),<br>
but also updates 3rd party API. <br>

--
## Starting App from scratch:
Everything you need to do is just:<br>
1.a) Double-click on batch script `start-app.bat` (for Windows)<br>
1.b) Double-click on shell script `start-app.sh`  (for Linux)<br>

