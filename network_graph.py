class SocialGraph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user_id):
        if user_id not in self.graph:
            self.graph[user_id] = []

    def add_friendship(self, u1, u2):
        if u1 not in self.graph or u2 not in self.graph:
            print("User not found!")
            return
        if u2 not in self.graph[u1]:
            self.graph[u1].append(u2)
            self.graph[u2].append(u1)

    def remove_friendship(self, u1, u2):
        if u2 in self.graph.get(u1, []):
            self.graph[u1].remove(u2)
            self.graph[u2].remove(u1)

    def get_friends(self, user_id):
        return self.graph.get(user_id, [])