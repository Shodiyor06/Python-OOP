class User:
    def __init__(self, username, email, is_active):
        self.username= username
        self.email= email
        self.is_active = is_active
    def activate(self):
        if self.is_active == False:
            self.is_active = True
            print(f"{self.username} faollashtirildi.")
    def deactivate(self):
        if self.is_active == True:
            self.is_active = False
            print(f"{self.username} o'chirildi.")

user1 = User('ali', 'ali@gmail.com', False)
user1.activate()
print(user1.username)
print(user1.email)
print(user1.is_active)