# クラスを使う


class Post:
    # 属性の定義（コンストラクター）
    def __init__(self, text, likes):
        self.text = text
        self.likes = likes

    # メソッドの定義
    def show(self):
        print(f"{self.text} - {self.likes}")


posts = [Post("Hello", 3), Post("Hi", 5)]

# print(posts[0].text)
# print(posts[0].likes)
# print(posts[1].text)
# print(posts[1].likes)

posts[0].show()
posts[1].show()
