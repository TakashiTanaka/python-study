# クラスの継承


class Post:  # 親クラス・Superクラス
    def __init__(self, text):
        self._text = text
        self._likes = 0

    def show(self):
        print(f"{self._text} - {self._likes}")

    def like(self):
        self._likes += 1


class SponsoredPost(Post):  # 子クラス・Subクラス
    pass


posts = [Post("Hello"), Post("Hi"), SponsoredPost("Hey")]

for post in posts:
    post.show()
