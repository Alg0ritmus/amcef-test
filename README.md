# amcef-test

## URLS:

'admin/'                      -> admin dashboard (default django)
'api/'                        -> main page
'api/posts/'                  -> get all Posts from API
'api/post/<int>/'             -> get Post by it's ID
'api/updatePost/<int>/'       -> update Post
'api/getPostByUsedId/<int>/'  -> get Post by User ID
'api/createPost/'             -> create Post
'api/deletePost/<int>/'       -> delete Post

---
## Simple Info
APP is available on url: http://127.0.0.1:8000/api/ (locally -> py manage.py runserver).
Main page contains 2 buttons (`Get By ID` & `Get By userId`) with associated fields and
1 button for Post creation.

ALL requests to backend ('api/..') are returning Python objects (because of using Django-templates)
which means, that backend are NOT returning JSON obj (but it could be easily rewrited for JSON support
in case we want to deal with real frontend framework/library).

Every Create, Update, Delete request updates loacal DB (sqlite for simplicity),
but also updates 3rd party API. 

--
## Starting App from scratch:
Everything you need to do is just:
1.a) Double-click on batch script `start-app.bat` (for Windows)
1.b) Double-click on shell script `start-app.sh`  (for Linux)

