#お試し
cats=['chipi','happy','huh?']
print(cats)
print(cats[0])

#点数算出システム（コンテナ練習）
#国語、数学、英語
scores=[89,93,47]
total=sum(scores)
print(f'合計{total}点です。')
shrink=scores[0]/4+scores[1]+scores[2]/2
print(f'理系型入試圧縮後の点数は{shrink}です。')
ave=total/len(scores)
print(f'平均点は{float(ave):.1f}点です。')


#コンテナ練習
members=['まふゆ','瑞希','絵名','奏']
print(members)
members.append('ミク')
print(members)
members.remove('ミク')
print(members)
members[0]='まふまふもふもふ'
print(members)
print(members[2:3])
print(members[-3:-1])
print(members[-2:-3])


#点数算出システム（ディクショナリー練習）
#国語、数学、英語
scores={'koku':89,'suu':93,'ei':47}
print(scores['koku'])
scores['butu']=60
scores['ka']=74
print(scores)

del scores['koku']
print(scores)
total=sum(scores.values())
print(total)

members=('chipi',)
print(type(members))
print(members[0])