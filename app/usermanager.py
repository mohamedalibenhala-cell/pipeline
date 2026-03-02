class UserManager:

    def __init__(self):
        self.users = []

    def add_users(self, username):
        if not username:
            raise ValueError("nom utilisateur obligatoire")
        if username in self.users:
            raise ValueError("existant deja")
        self.users.append(username)

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("existe pas")
        self.users.remove(username)

    def count_users(self):
        return len(self.users)
    
    
def count_total_users(users):
    return len(users)
