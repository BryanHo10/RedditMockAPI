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
    def put_user_profile_error(self):
        self.client.put("/reddit-mock/api/v1.0/user")




    @task(1)
    def inc_karma_put(self):
        self.client.put("/reddit-mock/api/v1.0/user/2/karma/increment")

    @task(1)
    def inc_karma_error_post(self):
        self.client.post("/reddit-mock/api/v1.0/user/2/karma/increment")

    @task(1)
    def dec_karma_put(self):
        self.client.put("/reddit-mock/api/v1.0/user/2/karma/decrement")

    @task(1)
    def dec_karma_error_post(self):
        self.client.post("/reddit-mock/api/v1.0/user/2/karma/decrement")




    @task(1)
    def delete_user(self):
        self.client.delete("/reddit-mock/api/v1.0/user/2")

    @task(1)
    def update_user_email(self):
        self.client.put("/reddit-mock/api/v1.0/user/2")

    @task(1)
    def get_user(self):
        self.client.get("/reddit-mock/api/v1.0/user/2")

    @task(1)
    def error_post_user(self):
        self.client.post("/reddit-mock/api/v1.0/user/2")









    @task(5)
    def create_post(self):
        self.client.post("/reddit-mock/api/v1.0/user/2/post", {"title": "First!", "message": "This is my first message",
                                                               "communityID": "load1"})

    @task(1)
    def create_post_get_error(self):
        self.client.get("/reddit-mock/api/v1.0/user/2/post", {"title": "First!", "message": "This is my first message",
                                                               "communityID": "load1"})

    @task(1)
    def delete_user_post(self):
        self.client.delete("/reddit-mock/api/v1.0/user/2/post/1")

    @task(1)
    def get_user_post(self):
        self.client.get("/reddit-mock/api/v1.0/user/2/post/1")

    @task(1)
    def put_user_post_error(self):
        self.client.put("/reddit-mock/api/v1.0/user/2/post/1")

    @task(1)
    def get_list_posts(self):
        self.client.get("/reddit-mock/api/v1.0/post/2")

    @task(1)
    def put_list_posts_error(self):
        self.client.put("/reddit-mock/api/v1.0/post/2")

    @task(1)
    def get_community_list_posts(self):
        self.client.get("/reddit-mock/api/v1.0/post/cpsc/2")

    @task(1)
    def put_community_list_posts_error(self):
        self.client.put("/reddit-mock/api/v1.0/post/cpsc/2")



class MyWebsiteUser(HttpLocust):
    task_set = MyTasks
    wait_time = between(1, 2)