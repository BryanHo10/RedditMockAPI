from flask import Flask
from flask import request
from flask import render_template

from User/userAPI.py import *
from Post/postAPI.py import *

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
# (email) will be a query parameter
@app.route('/reddit-mock/api/v1.0/user/<userid>',methods=['GET','PUT','DELETE'])
def unique_user(userid):
    query_parameters = request.args


    if request.method == 'DELETE':
        return delete_user(userid)
    elif request.method == 'PUT':
        email_addr = query_parameters['email'] 
    	return update_email(userid, email_addr)

    return get_user(userid)

# Decrement Karma from unique user
@app.route('/reddit-mock/api/v1.0/user/<userid>/karma/decrement',methods=['PUT'])
def dec_karma(userid):
    error = None
    if request.method == 'PUT':
        return dec_karma(userid)

    return error

# Increment Karma for unique user
@app.route('/reddit-mock/api/v1.0/user/<userid>/karma/increment',methods=['PUT'])
def inc_karma(userid):
    error = None

    if request.method == 'PUT':
        return inc_karma(userid)

    return error

@app.route('/reddit-mock/api/v1.0/user',methods=['GET','POST'])
def user():
    if request.method == 'POST':
    	return create_user()
    return get_all_users()

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

# (n):size will be a query parameter
@app.route('/reddit-mock/api/v1.0/post')
def list_posts():
    query_parameters = request.args

    num_post = query_parameters.get('size')
    return get_posts_from(num_post)

# (n):size will be a query parameter
@app.route('/reddit-mock/api/v1.0/post/<communityid>')
def list_community_posts(communityid):
    query_parameters = request.args

    num_post = query_parameters.get('size')
    return get_posts_from(num_post, communityid)

@app.route('/reddit-mock/api/v1.0/user/<userid>/post',methods=['POST'])
def user_post(userid):
    return create_post(userid)

@app.route('/reddit-mock/api/v1.0/user/<userid>/post/<postid>',methods=['GET','DELETE'])
def unique_post(userid,postid):
    error = None
    if request.method == 'DELETE':
        return delete_post(userid,postid)

    return get_user_post(userid,postid)