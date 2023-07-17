# @property


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

    # ゲッター
    @property
    def likes(self):
        return self._likes

    # セッター（読み取り専用にしたい場合、セッターを記述しなければOK）
    @likes.setter
    def likes(self, num):
        self._likes = num


posts = [Post("Hello"), Post("Hi")]

posts[0]._likes = 1000
print(posts[0]._likes)

# for post in posts:
#     post.show()
