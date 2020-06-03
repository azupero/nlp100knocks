# “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

text2 = text.replace('.', '').split(' ')

one_word_idx = (1, 5, 6, 7, 8, 9, 15, 16, 19)
word_idx = [i+1 for i in range(len(text2))]

words = []
for i, j in enumerate(text2):
    if i+1 in one_word_idx:
        words.append(j[0]) # j[:1]
    else:
        words.append(j[:2])

print(dict(zip(words, word_idx)))