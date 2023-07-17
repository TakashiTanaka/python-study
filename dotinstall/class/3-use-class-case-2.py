# クラスを使う


class Post:
    # 属性の定義（コンストラクター）
    def __init__(self, text):
        self._text = text
        self._likes = 0  # 慣習的にプライベートにしたい変数には接接頭として_をつける

    # メソッドの定義
    def show(self):
        print(f"{self._text} - {self._likes}")

    # メソッドを介して_likesの数を増やす
    def like(self):
        self._likes += 1


posts = [Post("Hello"), Post("Hi")]

# posts[0]._likes += 1
posts[0].like()

for post in posts:
    post.show()
