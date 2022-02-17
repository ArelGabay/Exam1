import requests as requests


class Post:
    def __init__(self, user_id, post_id, title, body):
        self.user_id = user_id
        self.post_id = post_id
        self.title = title
        self.body = body

    def __str__(self):
        return f"Post Details:\nUser ID: {self.user_id}\nPost ID: {self.post_id}\nPost Title: " \
               f"{self.title}\nPost Body:{self.body} "


API = "https://jsonplaceholder.typicode.com/posts"

index = input("Enter an index ")

response = requests.get(f"{API}/{index}")
data = response.json()

post = Post(user_id=data['userId'], post_id=data['id'], title=data['title'], body=data['body'])
print(post)
