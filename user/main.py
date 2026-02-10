from user import User

class Main:
    def __init__(self) -> None:
        users: list[User] = [
        User("John", "Doe"),
        User("Jane", "Morgan")
        ]
        print("All users:")
        for user in users:
            user.fullName()
        return None
    
if __name__ == "__main__":
    app = Main()