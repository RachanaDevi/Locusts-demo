from locust import User, task, constant


class MyTest(User):
    wait_time = constant(1)

    # this task is a python decorator
    @task
    def say_hello(self):
        print("Hello world")

    @task
    def wear_mask(self):
        print("Wear mask! Stay safe")

    def say_goodbye(self):
        print("Good bye!")

# if __name__ == '__main__':
#     print_hi('PyCharm')
