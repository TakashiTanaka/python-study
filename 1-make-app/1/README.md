# とりあえず作ってみる

## 必要なもの

### pyInstaller

PyInstallerというライブラリで実行可能ファイルを生成できる。

`pip install pyinstaller`

## プログラムを書く

tkinterのdeprecatedメッセージの対処をする

## pyinstallerでアプリ化する

`pyinstaller test.py --onefile`

pyinstallerを実行すると下記エラーが表示されたのでデバッグ

```bash
OSError: Python library not found: Python3, Python, libpython3.10.dylib, .Python, libpython3.10m.dylib
    This means your Python installation does not come with proper shared library files.
    This usually happens due to missing development package, or unsuitable build parameters of the Python installation.

    * On Debian/Ubuntu, you need to install Python development packages:
      * apt-get install python3-dev
      * apt-get install python-dev
    * If you are building Python by yourself, rebuild with `--enable-shared` (or, `--enable-framework` on macOS).
```

## 参考

[pip install pyinstaller](https://www.insource.co.jp/python-gakuin/mail-backnumber/vol18.html)

[python \- Using tkinter with Catalina, how to avoid deprecation warning? \- Ask Different](https://apple.stackexchange.com/questions/376165/using-tkinter-with-catalina-how-to-avoid-deprecation-warning)

[Mac環境でpyinstallerを使ってOSError: Python library not found: libpython3\.9m\.dylib, Python, Python3, libpython3\.9\.dylib,というエラーが出た場合の対処方法 \- at backyard](https://shinshin86.hateblo.jp/entry/2021/12/15/133636)

[enable\-sharedオプションで入れろと怒られた時にやったこと \- Qiita](https://qiita.com/osorezugoing/items/98369819e815a68c13c5)
