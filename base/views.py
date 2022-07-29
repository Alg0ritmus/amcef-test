from ast import Raise
from django.shortcuts import render, get_object_or_404, redirect
from .custom_code.requestCall import *
from .forms.postForm import *

# Create your views here.

def home(request):
    context = {
        'all_posts': Post.objects.all()
    }
    return render(request, 'base/home.html',context)

def getData(request):
    # get users
    list_of_users = getUSersId()
    
    
    return render(request, 'base/home.html') 

def getPost(request):
    dataFromReq = getReq(host="jsonplaceholder.typicode.com", url = "/posts" )

    context= {
        "data" : dataFromReq, 
    }
    return render(request, 'base/home.html', context) 

def getPostById(request,post_id):
    # search post in DB
    dataToReturn = {}
    try:
        myPost = Post.objects.get(pk=post_id)
        dataToReturn['id'] = myPost.pk
        dataToReturn['userId'] = myPost.userId
        dataToReturn['title'] = myPost.title
        dataToReturn['body'] = myPost.body

    except:
        postData = getReq(host="jsonplaceholder.typicode.com", url = "/posts/"+str(post_id))
        dataToReturn = {
            'id': postData['id'],
            'userId': postData['userId'],
            'title': postData['title'],
            'body':postData['body'],
        }
        
        Post.objects.create(pk=dataToReturn['id'],
        userId=dataToReturn['userId'],
        title=dataToReturn['title'],
        body=dataToReturn['body']
        )


    context= {
        "postById" : dataToReturn, 
    }
    return render(request, 'base/home.html', context) 

def getPostByUsedId(request,user_id):
    myPosts = Post.objects.filter(pk=user_id)
    print(myPosts,len(myPosts))

    # search post in DB
    try:
        myPosts = Post.objects.filter(userId=user_id)
        if len(myPosts) <1:
            raise "Post obj not found in DB!"
        
        # format data from DB accordingly to API data obj (for consistency )
        dataToReturn = []
        for myPost in myPosts:
            myPostfromReturn ={}
            myPostfromReturn['id'] = myPost.pk
            myPostfromReturn['userId'] = myPost.userId
            myPostfromReturn['title'] = myPost.title
            myPostfromReturn['body'] = myPost.body
            dataToReturn.append(myPostfromReturn)
         
    except:
        dataToReturn = getReq(host="jsonplaceholder.typicode.com", url = "/posts?userId="+str(user_id))

    context= {
        "data" : dataToReturn, 
    }
    return render(request, 'base/home.html', context) 




def updatePost(request,post_id):
    # ak nie je v DB ale je mimo tak pridaj do db
    # ak je post, zmen
    # ak get nahraj

    # is post in DB ?
    try:
        postToUpdate = get_object_or_404(Post,pk = post_id)

    # if not get info from API and save to db
    except:
        dataFromAPI = getReq(host="jsonplaceholder.typicode.com",url="/posts/"+str(post_id))
        print(dataFromAPI)
        postToUpdate = Post.objects.create(pk=dataFromAPI['id'],title=dataFromAPI['title'],body=dataFromAPI['body'],userId=dataFromAPI['userId'])
        postToUpdate.save()
    
    # if not post req
    if request.method != 'POST':
        context = {
        'myUPDATEform':updateForm(instance = postToUpdate),
        'myUPDATEform_id': post_id,
        }

        return render(request, 'base/post.html', context) 


    # If POST reQ
    myUpladeForm = updateForm(request.POST,instance = postToUpdate)
    if myUpladeForm.is_valid():
        # validate form and save post do DB
        myUpladeForm.save()
        # save post to 3nd party
        # to update create obj id/title/body/userId
        payload = {
            'id' : postToUpdate.pk,
            'title': postToUpdate.title,
            'body': postToUpdate.body,
            'userId': postToUpdate.userId
        }
        updateAPI(payload)
        # redirect
    else:
        print("Some error w saving obj to DB")

    return redirect('base:home')



def createPost(request):
    if request.method == 'POST':
        myform = createForm(request.POST)
        if myform.is_valid():
            # pre-save to DB
            presaved = myform.save(commit=False)
            # check if userId is valid, bc. we are not able to create new Users: 
            list_of_userIds= getUSersId()
            if presaved.userId in list_of_userIds:
                presaved.save()
            else: 
                Raise ("UserId not found during createPost")


            # save to api after succesfully save to local DB
            payload = {
                'title' : presaved.title,
                'body' : presaved.body,
                'userId': presaved.userId 
            }
            if createAPI(payload):
                return redirect('base:home')
            else:
                Raise ("Some error with creating creating API post")
    else:
        myform = createForm()
    
    context = {
        'myUpladeForm':myform,
    }
    return render(request, 'base/post.html', context) 

def deletePost(request, post_id):
    # get Post obj and delete it from DB
    mypost = get_object_or_404(Post,pk=post_id)
    mypost.delete()

    # delete Post from 3nd party API
    deleteAPI(post_id)

    return redirect('base:home')

