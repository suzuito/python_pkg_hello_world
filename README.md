Package備忘録
====

https://docs.python.org/3/tutorial/modules.html#packages

PythonのPackageについて思い出す。

# Moduleとは

Moduleとは、再利用するためのコード（関数、クラス、変数、etc...）が書かれたファイル。

例えば、以下はModuleである。

```python:hello_world.py
class Person:
    def __init__(self, name: str):
        self.name = name

    def say(self) -> str:
        return 'Hello world'


kenshiro = Person('ケンシロウ')


def hello(p: Person):
    print('{}: {}'.format(p.name, p.say()))

```

## Moduleを使う

我々は、Moduleをimportすることで、Moduleの中のコードを実行できる。
importの方法は、以下のように様々だ。

### Moduleをimportし、実行する

```bash
% python
>>> import hello_world
>>> hello_world.hello(hello_world.kenshiro)
ケンシロウ: Hello world
```

### Moduleの中の特定のコードだけをimportし、実行する

```bash
% python
>>> from hello_world import kenshiro
>>> kenshiro.say()
'Hello world'
```

### Moduleの中の全てのコードをimportし、実行する

```bash
% python 
>>> from hello_world import *
>>> kenshiro.say()
'Hello world'
>>> hello(kenshiro)
ケンシロウ: Hello world
```

### Moduleをimportし、別名をつけて、実行する

```bash
% python
>>> import hello_world as hw
>>> hw.hello(hw.kenshiro)
ケンシロウ: Hello world
```

### Moduleの中の特定のコードだけをimportし、別名をつけて、実行する

```bash
% python
>>> from hello_world import kenshiro as ken
>>> ken.say()
'Hello world'
```

## Moduleの探索

我々は、`sys.path`変数に格納されているディレクトリの配下にあるModuleをimportできる。

```bash
% python
>>> import sys
>>> sys.path
['', '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7']
```

`sys.path`がカレントディレクトリ（`''`）含むので、我々はhello_world.pyをimportできるのだ。`sys.path`からカレントディレクトリを除去するとどうなるのか？当然、importできなくなる。

```bash
% python
Python 3.7.4 (default, Jul  9 2019, 18:13:23) 
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path = []
>>> import hello_world
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'hello_world'
```

# Packageとは

Pythonにおいて、Packageは複数の意味を持つ。

1. Packageとは、ディレクトリであり、複数のModuleがその配下にある。
2. 再配布するためのコードを集めて、それらを圧縮し、1つのファイルにしたもの。`pip install`コマンド等を使ってインストールできる。

ここでは、1を対象とする。2について知りたければ、[こちら](https://packaging.python.org/)を読むと良いだろう。

先ほどのコードをPackageにする。

```bash
% ls -lR
hello_world

./hello_world/__init__.py
./hello_world/person

./hello_world/person/__init__.py
./hello_world/person/anime.py
./hello_world/person/movie.py
```

ポイントは

* Packageの配下にディレクトリを作ると、そのディレクトリはPackage（Subpackage）となる。
* Packageは`__init__.py`を含まなければならない。

このパッケージをimportし、コードを実行してみよう。

```bash
% python
>>> import hello_world
>>> import hello_world.person.anime
>>> hello_world.hello(hello_world.person.anime.kenshiro)
ケンシロウ: Hello world
```
