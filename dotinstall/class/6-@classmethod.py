# クラスそのものに紐付いた属性とメソッド


class Post:
    _count = 0  # クラス自身が持つ属性

    def __init__(self, text):
        self._text = text
        self._likes = 0
        Post._count += 1

    # クラス自身が持つメソッド
    @classmethod
    def show_count(cls):
        print(f"{cls._count} instances created")

    def show(self):
        print(f"{self._text} - {self._likes}")

    def like(self):
        self._likes += 1


posts = [Post("Hello"), Post("Hi")]

for post in posts:
    post.show()

Post.show_count()
