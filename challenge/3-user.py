#!/usr/bin/python3
"""User class implementation"""

class User():
    """User class"""

    def __init__(self, first_name, last_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.__password = password

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def is_valid_password(self, pwd):
        return self.__password == pwd

if __name__ == "__main__":
    u = User("Test", "User", "123456")
    print(u)
    if u.is_valid_password("123456"):
        print("is_valid_password should return True if it's the right password")
    if not u.is_valid_password("12345"):
        print("is_valid_password should return False if it's not the right password")
