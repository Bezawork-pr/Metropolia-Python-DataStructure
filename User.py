"""Make a class called `User`.
Create the following attributes: first_name and last_name, email, and location."""
class User:
    
    def __init__(self, first_name, last_name, user_name, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.location = location
        
    def describe_user(self):
        print("Name: {} {}".format(self.first_name, self.last_name))
        print("Username: {}".format(self.user_name))
        print("Email: {}".format(self.email))
        print("Location: {}".format(self.location))
    def greet_user(self):
        print("Welcome back {}!".format(self.user_name))
