# クラスを使わなかった場合


def show(post):
    print(f"{post['text']} - {post['likes']}")


posts = [
    {"text": "Hello", "likes": 3},
    {"text": "Hi", "likes": 5},
]

print(posts)

show(posts[0])
show(posts[1])
