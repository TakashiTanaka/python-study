# setter, getter


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

    # セッター
    def set_likes(self, num):
        self._likes = num

    # ゲッター
    def get_likes(self):
        return self._likes


posts = [Post("Hello"), Post("Hi")]

posts[0].set_likes(100)
print(posts[0].get_likes())

# for post in posts:
#     post.show()
