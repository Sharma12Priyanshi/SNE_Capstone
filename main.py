from profiles import UserProfile
from network_graph import SocialGraph
from algorithms import bfs_shortest_path, dfs_depth
from sorting import insertion_sort

profiles = UserProfile()
graph = SocialGraph()

# DEMO DATA
def demo():
    users = [
        ("u1", "Aman", 20, ["tech", "sports"]),
        ("u2", "Riya", 21, ["music", "tech"]),
        ("u3", "Raj", 22, ["sports", "travel"]),
        ("u4", "Simran", 23, ["music", "travel"]),
        ("u5", "Karan", 24, ["tech", "gaming"]),
        ("u6", "Neha", 25, ["fitness", "sports"]),
    ]

    for u in users:
        profiles.add_user(*u)
        graph.add_user(u[0])

    connections = [
        ("u1", "u2"), ("u1", "u3"),
        ("u2", "u4"), ("u3", "u5"),
        ("u4", "u6"), ("u5", "u6"),
        ("u2", "u3"), ("u3", "u6")
    ]

    for u1, u2 in connections:
        graph.add_friendship(u1, u2)

    # BFS TEST
    print("Shortest Path u1 → u6:", bfs_shortest_path(graph.graph, "u1", "u6"))
    print("Shortest Path u2 → u5:", bfs_shortest_path(graph.graph, "u2", "u5"))

    # DFS TEST
    print("DFS Depth 2:", dfs_depth(graph.graph, "u1", 2))
    print("DFS Depth 3:", dfs_depth(graph.graph, "u1", 3))

    # Suggestions
    suggest_friends("u1")


def suggest_friends(user_id):
    user_interests = profiles.get_user(user_id)["interests"]
    candidates = []

    for uid, data in profiles.users.items():
        if uid != user_id and uid not in graph.get_friends(user_id):
            common = len(set(user_interests) & set(data["interests"]))
            candidates.append((uid, common))

    sorted_list = insertion_sort(candidates)
    print("Top Suggestions:", sorted_list[:5])


if __name__ == "__main__":
    demo()