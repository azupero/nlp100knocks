# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

# answer1
words = text.replace(',', '').replace('.', '').split(' ')

word_len = []
for word in words:
    word_len.append(len(word))

print(word_len)

# answer2
words2 = text.replace(',', '').replace('.', '')
word_len2 = [len(word) for word in words2.split(' ')]
print(word_len2)