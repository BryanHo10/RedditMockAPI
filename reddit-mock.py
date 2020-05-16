from flask import Flask
from flask import request
from flask import render_template
import json

import User.userAPI as userService
import Post.postAPI as postService
import Voting.votesAPI as voteService
import Message.messageAPI as messageService

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
@app.route('/reddit-mock/api/v1.0/post/<size>',methods=["GET"])
def list_posts(size):
    if request.method == 'GET':
        return json.dumps({'success':True , 'data':postService.get_posts_from(size)}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'}  

# (n):size will be a query parameter
@app.route('/reddit-mock/api/v1.0/post/<communityid>/<size>',methods=["GET"])
def list_community_posts(communityid,size):
    if request.method == 'GET':
        return json.dumps({'success':True , 'data':postService.get_posts_from(size,communityid)}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'}  

@app.route('/reddit-mock/api/v1.0/user/<userid>/post',methods=['POST'])
def user_post(userid):
    if request.method == 'POST':
        request_json = request.form
        if "URL" in request_json:
            return json.dumps({'success':True , 'data':postService.create_post(userid,request_json["title"],request_json["message"],request_json["communityID"],request_json["URL"])}), 200, {'ContentType':'application/json'}
        return json.dumps({'success':True , 'data':postService.create_post(userid,request_json["title"],request_json["message"],request_json["communityID"])}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'}  

@app.route('/reddit-mock/api/v1.0/user/<userid>/post/<postid>',methods=['GET','DELETE'])
def unique_post(userid,postid):
    if request.method == 'DELETE':
        return json.dumps({'success':True , 'data':postService.delete_post(userid,postid)}), 200, {'ContentType':'application/json'}
    elif request.method == "GET":
        return json.dumps({'success':True , 'data':postService.get_post(userid,postid)}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'}  


'''
Voting Microservice
    GET:
        - Retrieve existing post's current vote
        - List n most voted posts from any community
        - Return list of sorted scores (w/ from a list of post id's)
    PUT:
        - Upvote a post
        - Downvote a post
    
'''

@app.route('/reddit-mock/api/v1.0/post/<postid>/vote', methods=['GET'])
def retrieve_post_score(postid):
    if request.method == 'GET':
        return json.dumps({'success':True,'data':voteService.get_unique_post_score(postid)}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 

@app.route('/reddit-mock/api/v1.0/post/vote/<size>', methods=['GET'])
def retrieve_list_post(size):
    if request.method == 'GET':
        return json.dumps({'success':True,'data':voteService.get_scores(size)}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 

@app.route('/reddit-mock/api/v1.0/post/vote', methods=['GET'])
def retrieve_unique_list():
    if request.method == 'GET':
        request_json = request.form
        # print(request_json)
        print()
        return json.dumps({'success':True,'data':voteService.get_list_scores(request_json["postIDset"])}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 


@app.route('/reddit-mock/api/v1.0/user/<userid>/post/<postid>/upvote', methods=['PUT'])
def upvote(userid,postid):
    if request.method == 'PUT':
        return json.dumps({'success':True,'data':voteService.upvote_post(userid,postid)}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 
@app.route('/reddit-mock/api/v1.0/user/<userid>/post/<postid>/downvote', methods=['PUT'])
def downvote(userid,postid):
    if request.method == 'PUT':
        return json.dumps({'success':True,'data':voteService.downvote_post(userid,postid)}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'}  

'''
Messaging Microservice
    POST:
        - Send Message
    DELETE:
        - Delete Message
    PUT:
        - Favorite Message
    
'''

@app.route('/reddit-mock/api/v1.0/user/<userid>/message', methods=['POST','GET'])
def user_message(userid):
    if request.method == 'GET':
        return json.dumps({'success':True,'data':messageService.get_user_message(userid)}), 200, {'ContentType':'application/json'}
    elif request.method == 'POST':
        request_json = request.form
        return json.dumps({'success':True,'data':messageService.create_message(userid,request_json["content"],request_json["recipient"])}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 

@app.route('/reddit-mock/api/v1.0/user/<userid>/message/<messageid>', methods=['DELETE','PUT'])
def message_actions(userid,messageid):
    if request.method == 'DELETE':
        return json.dumps({'success':True,'data':messageService.delete_message(messageid)}), 200, {'ContentType':'application/json'}
    elif request.method == 'PUT':
        return json.dumps({'success':True,'data':messageService.favorite_message(messageid)}), 200, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 404, {'ContentType':'application/json'} 