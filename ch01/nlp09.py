# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）
# を与え，その実行結果を確認せよ．
import random

# answer1
def shuffleWord(word):
    if len(word) <= 4:
        return word
    else:
        start = word[0]
        end = word[-1]
        others = random.sample(list(word[1:-1]), len(word[1:-1]))
        return ''.join([start] + others + [end])

text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
ans = [shuffleWord(w) for w in text.split()]
print(ans)

# answer2
def shuffleWord2(word):
    if len(word) <= 4:
        return word
    else:
        start = word[0]
        end = word[-1]
        others = list(word[1:-1])
        random.shuffle(others)
        return ''.join([start] + others + [end])

ans = [shuffleWord2(w) for w in text.split()]
print(ans)