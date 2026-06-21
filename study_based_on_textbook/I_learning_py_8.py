#練習問題2.7

#練習2.2
scores=[
    int(input('国語の点数を入力してください>>')),
    int(input('数学の点数を入力してください>>')),
    int(input('理科の点数を入力してください>>')),
    int(input('社会の点数を入力してください>>')),
    int(input('英語の点数を入力してください>>'))
]

total=sum(scores)
ave=total/len(scores)

print(total)
print(ave)

print('chipi')
