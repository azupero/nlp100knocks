# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
def temperature_announce(x, y, z):
    return print('{}時の{}は{}'.format(x, y, z))

temperature_announce(12, '気温', 22.4)