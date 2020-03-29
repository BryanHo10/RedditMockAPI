import requests,time



base_url = "http://127.0.0.1:5000/"
api_url = "reddit-mock/api/v1.0/"

# Create Multiple Users
user_data=[]
user_data.append({
    "username":"bryanHd",
    "email":"bryanDF@gmail.com",
    "password":"hello"
})
user_data.append({
    "username":"Jon_Torres",
    "email":"jonT@csu.fullerton.edu",
    "password":"1234654681asdf"
})
user_data.append({
    "username":"caessar54",
    "email":"caesar_salad@yahoo.com",
    "password":"asdfasdfasdf"
})
user_data.append({
    "username":"teacher_V",
    "email":"prof@fullerton.edu",
    "password":"a168fa5fd5anj6^kl"
})
user_data.append({
    "username":"SadGuy911",
    "email":"sad@wahooo.edu",
    "password":"sdfgsdfg^kl"
})
# Test Create user
for user in user_data:
    requests.post(base_url+api_url+"user",data=user)
    print("Created "+user["username"])

print("----------------------------------------------------------")
# Test Get All users
print("All users in Reddit")
print()
all_users = requests.get(base_url+api_url+"user")
for user in all_users.json()['data']:
    print(user)


print("----------------------------------------------------------")
# Test Get Specific user
print("Retrieving teacher_V profile")
print()
good_user = "teacher_V"
get_user=requests.get(base_url+api_url+"user/"+good_user)
print(get_user, get_user.text)


print("----------------------------------------------------------")
# Test Increment Karma
print("Increase teacher_V karma")
print()
for i in range(9):
    inc_karma= requests.put(base_url+api_url+"user/"+good_user+"/karma/increment")
    print(inc_karma,inc_karma.text)

print("----------------------------------------------------------")
# Test Decrement Karma
print("Lower bryanHd karma")
print()
bad_user = "bryanHd"
for i in range(3):
    dec_karma= requests.put(base_url+api_url+"user/"+bad_user+"/karma/decrement")
    print(dec_karma,dec_karma.text)

print("----------------------------------------------------------")
# Update Email
print("Update email for bryanHd")
print()
user_lost = "bryanHd"
change_mail=requests.put(base_url+api_url+"user/"+user_lost,data={"email":"bryanHDTV@yahoo.com"})
print(change_mail,change_mail.text)

print("----------------------------------------------------------")
# Delete User
print("Delete SadGuy911 from Users")
print()
dlt_user = "SadGuy911"
delete_user = requests.delete(base_url+api_url+"user/"+dlt_user)
print(delete_user,delete_user.text)


print("----------------------------------------------------------")
# Check All users 
print("All users in Reddit")
print()
all_users = requests.get(base_url+api_url+"user")
for user in all_users.json()['data']:
    print(user)

print("----------------------------------------------------------")

# Post Test
post_data=[]
post_data.append({
    "username" :user_data[0]["username"],
    "message" :"Hello World",
    "communityID" :"CPSC",
    "URL" :"https://wwww.google.com",
})
post_data.append({
    "username" :user_data[3]["username"],
    "message" :"What's the Homework tonight?",
    "communityID" :"CPSC",
})
post_data.append({
    "username" :user_data[1]["username"],
    "message" :"Is this CPSC449?",
    "communityID" :"MATH",
})
post_data.append({
    "username" :user_data[0]["username"],
    "message" :"No this is MATH",
    "communityID" :"MATH",
    "URL" :"https://www.fullerton.edu",
})
post_data.append({
    "username" :user_data[2]["username"],
    "message" :"We finished the Project in time",
    "communityID" :"CPSC",
})
post_data.append({
    "username" :user_data[0]["username"],
    "message" :"Is this Reddit?",
    "communityID" :"HIST",
    "URL":"https://www.reddit.com"
})
post_data.append({
    "username" :user_data[3]["username"],
    "message" :"Nice Job Everyone",
    "communityID" :"CPSC",
})
post_data.append({
    "username" :user_data[0]["username"],
    "message" :"Where is Everyone?",
    "communityID" :"HIST",
})

# Create Posts
print("----------------------------------------------------------")
for posting in post_data:
    requests.post(base_url+api_url+"user/"+posting["username"]+"/post",data=posting)
    print(posting["username"] + " wrote "+posting["message"]+" on "+ posting["communityID"])
    time.sleep(1.5)



# print("----------------------------------------------------------")


print("----------------------------------------------------------")
num_posts = requests.get(base_url+api_url+"post/5")
print("Overall Posts: 5 most recent")
print()
for posts in num_posts.json()['data']:
    print(posts)

print("----------------------------------------------------------")

print("----------------------------------------------------------")
num_posts = requests.get(base_url+api_url+"post/CPSC/4")
print("CPSC Posts: 4 most recent")
print()
for posts in num_posts.json()['data']:
    print(posts)

print("----------------------------------------------------------")
print("----------------------------------------------------------")
print("Latest Post")
get_latest = requests.get(base_url+api_url+"user/"+num_posts.json()["data"][0][1]+"/post/"+num_posts.json()["data"][0][0])
print(get_latest.json()["data"])

print("----------------------------------------------------------")
print("----------------------------------------------------------")
print("Deleted Latest Post : ",num_posts.json()["data"][0][1],num_posts.json()["data"][0][0])
delete_latest = requests.delete(base_url+api_url+"user/"+num_posts.json()["data"][0][1]+"/post/"+num_posts.json()["data"][0][0])
print(get_latest)
print("----------------------------------------------------------")

print("----------------------------------------------------------")
num_posts = requests.get(base_url+api_url+"post/CPSC/2")
print("CPSC Posts: 2 most recent")
print()
for posts in num_posts.json()['data']:
    print(posts)

print("----------------------------------------------------------")