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
# (email) will be a query parameter
@app.route('/reddit-mock/api/v1.0/user/<userid>',methods=['GET','PUT','DELETE'])
def unique_user(userid):
    error = None
    if request.method == 'DELETE':
        return delete_user(userid)
    elif request.method == 'PUT':
        return 
    return 'Index Page'

# Decrement Karma from unique user
@app.route('/reddit-mock/api/v1.0/user/<userid>/karma/decrement',methods=['PUT'])
def karma_dec(userid):
    error = None
    if request.method == 'PUT':
        return 
    return 'Index Page'

# Increment Karma for unique user
@app.route('/reddit-mock/api/v1.0/user/<userid>/karma/increment',methods=['PUT'])
def karma_inc(userid):
    error = None
    if request.method == 'PUT':
        return 
    return 'Index Page'

@app.route('/reddit-mock/api/v1.0/user',methods=['GET','POST'])
def user():
    if request.method == 'POST':
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

# (n):size will be a query parameter
@app.route('/reddit-mock/api/v1.0/post')
def list_posts():
    query_parameters = request.args

    num_post = query_parameters.get('size')
    return list_posts()

# (n):size will be a query parameter
@app.route('/reddit-mock/api/v1.0/post/<communityid>')
def list_community_posts(communityid):
    query_parameters = request.args

    num_post = query_parameters.get('size')
    return list_posts(communityid)

@app.route('/reddit-mock/api/v1.0/user/<userid>/post',methods=['POST'])
def user_post(userid):
    return create_user_post(userid)

@app.route('/reddit-mock/api/v1.0/user/<userid>/post/<postid>',methods=['GET','DELETE'])
def unique_post(userid,postid):
    error = None
    if request.method == 'DELETE':
        return delete_user_post(userid,postid)

    return show_user_post(userid,postid)