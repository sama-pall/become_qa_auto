import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')

        return r.json()

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={'q': name}
        )
        return r.json()

    def get_emojis(self):
        r = requests.get('https://api.github.com/emojis')

        return r.j
