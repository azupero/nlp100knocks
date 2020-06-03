# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(token):
    text = ''
    for i in token:
        if i.islower():
            text += chr(219 - ord(i))
        else:
            text += i
    return text

text = 'Machine Learning.'
print(cipher(text))