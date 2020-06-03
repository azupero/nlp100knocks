# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
def generate_ngrams(token, n):
    ngrams = zip(*[token[i:] for i in range(2)])
    ngram = [''.join(ngram) for ngram in ngrams] # n-gramを要素とするリスト ['A B', 'B C'], 空白がいらなければ''.join()にする
    # ngram = [list(ngram) for ngram in ngrams] # 各n-gramのリストを要素とするリスト [['A', 'B'], ['B', 'C']]
    return ngram

text1 = 'paraparaparadise'
text2 = 'paragraph'

X = set(generate_ngrams(text1, 2))
Y = set(generate_ngrams(text2, 2))

union = X | Y
inter = X & Y
diff = X - Y

print(union)
print(inter)
print(diff)
print('se' in inter)