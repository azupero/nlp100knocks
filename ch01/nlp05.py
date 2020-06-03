# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

# answer1
def generate_ngrams(token, n):
    ngrams = zip(*[token[i:] for i in range(2)])
    ngram = [' '.join(ngram) for ngram in ngrams] # n-gramを要素とするリスト ['A B', 'B C']
    # ngram = [list(ngram) for ngram in ngrams] # 各n-gramのリストを要素とするリスト [['A', 'B'], ['B', 'C']]
    return ngram

text = 'I am an NLPer'
token = text.split(' ')

print(generate_ngrams(token, 2))
print(generate_ngrams(text, 2))

# answer2
def n_gram(target, n):
    return [target[idx:idx + n] for idx in range(len(target) - n + 1)]

print(n_gram(token, 2))
print(n_gram(text, 2))