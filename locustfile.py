from locust import HttpLocust, TaskSet

def login(l):
    l.client.get("/age?age=31")

def logout(l):
    l.client.get("/id?customerId=1")

def index(l):
     l.client.get("/showall")

def profile(l):
    l.client.get("/firstname?firstName=HariOm")
	
def lastname(l):
    l.client.get("/lastname?lastName=Misra")

class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1, lastname:1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000