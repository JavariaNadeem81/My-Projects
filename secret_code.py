class Greeting:
    def __init__ (self, defualt_greeting="Hello"):
        self.defualt_greeting = defualt_greeting
        
    def get_greeting_message(self):
        greeting_message = input("Enter your greeting message (defualt: {self.defualt}): ") or self.defualt_greeting
        User_name = input("Enter your name:") or "User"
        return f"{greeting_message}, {User_name}!"
    
#creating an instance of the greeting class and call the method:
greeting_instance = Greeting()
print(greeting_instance.get_greeting_message())
        