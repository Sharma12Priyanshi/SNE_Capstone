class UserProfile:
    def __init__(self):
        self.users = {}  # HashTable (dict)

    def add_user(self, user_id, name, age, interests):
        if user_id in self.users:
            print("User already exists!")
            return
        self.users[user_id] = {
            "name": name,
            "age": age,
            "interests": interests
        }

    def get_user(self, user_id):
        return self.users.get(user_id, "User not found")

    def update_user(self, user_id, name=None, age=None, interests=None):
        if user_id not in self.users:
            print("User not found!")
            return
        if name:
            self.users[user_id]["name"] = name
        if age:
            self.users[user_id]["age"] = age
        if interests:
            self.users[user_id]["interests"] = interests

    def display_users(self):
        for uid, data in self.users.items():
            print(uid, ":", data)