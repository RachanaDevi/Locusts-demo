from locust import HttpUser, constant, task, SequentialTaskSet

# SequentialTaskSet means executing the task sequentially

class MyReqRes(SequentialTaskSet):

    @task
    def get_users(self):
        res = self.client.get("/")
        print("Get Method status is ", res.status_code)

    @task
    def post_status(self):
        res = self.client.post("/?status=success")
        print("Post Method status is ", res.status_code)


class MySeqTest(HttpUser):
    wait_time = constant(1)
    host = "http://example.com"

    tasks = [MyReqRes]
