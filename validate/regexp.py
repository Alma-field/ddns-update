# source: https://qiita.com/TakamiChie/items/95ab9ae401879de90231
# (一部改変)
from re import compile

class Regexp(object):
  # バリデーションのためのクラス
  def __init__(self, pattern):
    # 初期化
    self.raw = pattern
    self.pattern = compile(pattern)

  def __contains__(self, val):
    # マッチ処理を行う
    return self.pattern.match(val)

  def __iter__(self):
    # エラー時にコンソールに表示される(invalid choice: 値 (choose from なんとか)
    # print_help()のmetavarでも表示されるので、metaverオプションを使って隠す
    return iter(("str", self.raw))
