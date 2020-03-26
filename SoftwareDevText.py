import requests



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

# Test Get All users
all_users = requests.get(base_url+api_url+"user")
for user in all_users.json()['data']:
    print(user)


# Test Get Specific user
good_user = "teacher_V"
get_user=requests.get(base_url+api_url+"user/"+good_user)
print(get_user, get_user.text)


# Test Increment Karma
for i in range(9):
    inc_karma= requests.put(base_url+api_url+"user/"+good_user+"/karma/increment")
    print(inc_karma,inc_karma.text)

# Test Decrement Karma
bad_user = "bryanHd"
for i in range(3):
    dec_karma= requests.put(base_url+api_url+"user/"+bad_user+"/karma/decrement")
    print(dec_karma,dec_karma.text)

# Update Email
user_lost = "bryanHd"
change_mail=requests.put(base_url+api_url+"user/"+user_lost,data={"email":"bryanHDTV@yahoo.com"})
print(change_mail,change_mail.text)

# Delete User
dlt_user = "SadGuy911"
delete_user = requests.delete(base_url+api_url+"user/"+dlt_user)
print(delete_user,delete_user.text)

# Check All users 
all_users = requests.get(base_url+api_url+"user")
for user in all_users.json()['data']:
    print(user)