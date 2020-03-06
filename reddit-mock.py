from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


'''
User Microservice
    - User ( Username, Email, Karma)
    GET:
        - Create User
    PUT
        - Update email
        - Increment Karma
        - Decrement Karma
    DELETE
        -Deactivate account
'''
@app.route('/reddit-mock/api/v1.0/user/<userid>',methods=['GET','PUT','DELETE'])
def unique_user():
    error = None
    if request.method == 'DELETE':
    elif request.method == 'PUT':
    
    return 'Index Page'
@app.route('/reddit-mock/api/v1.0/user',methods=['GET','POST'])
def user():
    if request.moethod == 'POST':
    
    return 'All Users'

'''
Post Microservice
    - Post ( Message, Community, optional URL, username, date_created)
    GET:
        - Retrieve existing post
        - List n most recent posts from a community
        - List n most recent posts from any community
    DELETE:
        - Delete an existing post
    POST:
        - Create a new Post
'''
@app.route('reddit-mock/api/v1.0/post')
def list_posts():
    return 'List of Posts'

@app.route('reddit-mock/api/v1.0/post/<communityid>')
def list_community_posts():
    return 'List of Posts'

@app.route('reddit-mock/api/v1.0/user/<userid>/post',method=['POST'])
def user_post():
    return 'Post created by User'

@app.route('reddit-mock/api/v1.0/user/<userid>/post/<postid>',method=['GET','DELETE'])
def unique_post():
    error = None
    if request.method == 'DELETE':

    return 'Post by user'





@app.route('/hello')
def hello_world():
    return 'Hello, World!'

