# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

# answer1
# def generate_ngrams(token, n):
#     ngrams = zip(*[token[i:] for i in range(2)])
#     ngram = [''.join(ngram) for ngram in ngrams] # n-gramを要素とするリスト ['A B', 'B C']
#     # ngram = [list(ngram) for ngram in ngrams] # 各n-gramのリストを要素とするリスト [['A', 'B'], ['B', 'C']]
#     return ngram

def generate_ngrams(text, n_gram=2, unit='word'):
    if unit == 'word':
        text = text.split(' ')
        ngrams = zip(*[text[i:] for i in range(n_gram)])
        return [' '.join(ngram) for ngram in ngrams]
    elif unit == 'char':
        ngrams = zip(*[text[i:] for i in range(n_gram)])
        return [''.join(ngram) for ngram in ngrams]

# answer2
def n_gram(text, n_gram=2, unit='word'):
    if unit == 'word':
        text = text.split(' ')
        return [text[idx:idx + n_gram] for idx in range(len(text) - n_gram + 1)]
    elif unit == 'char':
        return [text[idx:idx + n_gram] for idx in range(len(text) - n_gram + 1)]


text = 'I am an NLPer'


print('Method 1 :')
print(generate_ngrams(text, n_gram=2, unit='word'))
print(generate_ngrams(text, n_gram=2, unit='char'))

print('Method 2 :')
print(n_gram(text, n_gram=2, unit='word'))
print(n_gram(text, n_gram=2, unit='char'))
