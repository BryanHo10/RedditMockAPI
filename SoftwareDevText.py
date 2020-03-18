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

for user in user_data:
    resp = requests.post(base_url+api_url+"user",data = user)
    print(user,' was added')