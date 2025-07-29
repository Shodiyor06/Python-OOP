class User:
    def __init__(self, username, email, is_active):
        self.username= username
        self.email= email
        self.is_active = is_active
    
user1 = User('ali', 'ali@gmail.com', False)
print(user1.username)
print(user1.email)
print(user1.is_active)