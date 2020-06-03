# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
text1 = 'パトカー'
text2 = 'タクシー'

# answer1
print(''.join([t1+t2 for (t1, t2) in zip(text1, text2)]))

# answer2
ans = ''
for i in range(len(text1)):
    ans += text1[i]
    ans += text2[i]

print(ans)