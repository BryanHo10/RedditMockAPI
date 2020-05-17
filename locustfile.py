from locust import HttpLocust, TaskSet, task, between


class MyTasks(TaskSet):
    @task(2)
    def create_user_profile(self):
        self.client.post("/reddit-mock/api/v1.0/user", {"username": "load1", "email": "load1@gmail.com",
                                                        "password": "load1"})
    @task(1)
    def get_user_profile(self):
        self.client.get("/reddit-mock/api/v1.0/user")





    @task(1)
    def inc_karma_put(self):
        self.client.put("/reddit-mock/api/v1.0/user/2/karma/increment")

    

    @task(1)
    def dec_karma_put(self):
        self.client.put("/reddit-mock/api/v1.0/user/2/karma/decrement")

   



    @task(1)
    def delete_user(self):
        self.client.delete("/reddit-mock/api/v1.0/user/2")

    @task(1)
    def update_user_email(self):
        self.client.put("/reddit-mock/api/v1.0/user/2")

    @task(1)
    def get_user(self):
        self.client.get("/reddit-mock/api/v1.0/user/2")

   

    @task(5)
    def create_post(self):
        self.client.post("/reddit-mock/api/v1.0/user/2/post", {"title": "First!", "message": "This is my first message",
                                                               "communityID": "load1"})

    

    @task(1)
    def delete_user_post(self):
        self.client.delete("/reddit-mock/api/v1.0/user/2/post/1")

    @task(1)
    def get_user_post(self):
        self.client.get("/reddit-mock/api/v1.0/user/2/post/1")

    

    @task(1)
    def get_list_posts(self):
        self.client.get("/reddit-mock/api/v1.0/post/2")

   

    @task(1)
    def get_community_list_posts(self):
        self.client.get("/reddit-mock/api/v1.0/post/cpsc/2")


    @task(1)
    def create_message(self):
        self.client.post("/reddit-mock/api/v1.0/user/2/message")

    @task(1)
    def get_user_message(self):
        self.client.get("/reddit-mock/api/v1.0/user/2/message")

    @task(1)
    def favorite_message(self):
        self.client.put("/reddit-mock/api/v1.0/user/1/message/", {"messageID" : "428c8230-9af6-44bb-9912-ac78ff28ba9b"})

    @task(1)
    def delete_message(self):
        self.client.delete("/reddit-mock/api/v1.0/user/1/message/", {"messageID" : "428c8230-9af6-44bb-9912-ac78ff28ba9b"})

    @task(1)
    def upvote_post(self):
        self.client.put("/reddit-mock/api/v1.0/user/2/post/1/upvote")

    @task(1)
    def downvote_post(self):
        self.client.put("/reddit-mock/api/v1.0/user/2/post/1/downvote")

    @task(1)
    def get_scores(self):
        self.client.get("/reddit-mock/api/v1.0/post/1/vote")

    @task(1)
    def get_list_scores(self):
        self.client.get("/reddit-mock/api/v1.0/post/vote/2")
    @task(1)
    def get_uniqe_post_score(self):
        self.client.get("/reddit-mock/api/v1.0/post/vote")

    

    



class MyWebsiteUser(HttpLocust):
    task_set = MyTasks
    wait_time = between(1, 2)