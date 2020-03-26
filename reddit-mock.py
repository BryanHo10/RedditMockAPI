from flask import Flask
from flask import request
from flask import render_template
import json

import User.userAPI as userService
import Post.postAPI as postService

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
    if request.method == 'DELETE':
        return json.dumps({'success':True , 'data':userService.delete_user(userid)}), 200, {'ContentType':'application/json'}
    elif request.method == 'PUT':
        email_addr = request.form['email']
        print(email_addr)
        return json.dumps({'success':True , 'data':userService.update_email(userid,email_addr)}), 200, {'ContentType':'application/json'}
    elif request.method == 'GET':
        return json.dumps({'success':True , 'data':userService.get_user(userid)}), 200, {'ContentType':'application/json'}

    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 

# Decrement Karma from unique user
@app.route('/reddit-mock/api/v1.0/user/<userid>/karma/decrement',methods=['PUT'])
def dec_karma(userid):
    if request.method == 'PUT':
        return json.dumps({'success':True , 'data':userService.dec_karma(userid) }), 200, {'ContentType':'application/json'}

    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 

# Increment Karma for unique user
@app.route('/reddit-mock/api/v1.0/user/<userid>/karma/increment',methods=['PUT'])
def inc_karma(userid):   
    if request.method == 'PUT':
        return json.dumps({'success':True , 'data':userService.inc_karma(userid)}), 200, {'ContentType':'application/json'}
    
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 

@app.route('/reddit-mock/api/v1.0/user',methods=['GET','POST'])
def user():
    
    if request.method == 'POST':
        request_json = request.form
        userService.create_user(request_json["username"],request_json["email"],request_json["password"])
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    elif request.method == 'GET':
        all_users = userService.get_all_users()
        for user in all_users:
            print(user)
        return json.dumps({'success':True , 'data':all_users}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'}  


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
    return get_posts_from(num_post,communityid)

@app.route('/reddit-mock/api/v1.0/user/<userid>/post',methods=['POST'])
def user_post(userid):
    return create_post(userid)

@app.route('/reddit-mock/api/v1.0/user/<userid>/post/<postid>',methods=['GET','DELETE'])
def unique_post(userid,postid):
    if request.method == 'DELETE':
        return delete_post(userid,postid)

    return get_user_post(userid,postid)