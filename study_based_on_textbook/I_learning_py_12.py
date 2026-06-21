#第６章
print('association'.count('a'))

print('a')



chipi=['happy','cat']
print(id(chipi))







#identity値についての実験

scores1=[80,40,50]
scores2=[80,40,50]

scores1=scores2      #identity値の代入

scores1[0]=90     #書き換え
scores2[0]=69     #書き換え２
scores1[0]=90     #書き換え

print(scores1[0],scores2[0])





#関数による変数の破壊の実験
def rename(names):
    for i in range(len(names)):
        names[i]=names[i]+'さん'
    return names

prenames=['佐々木','田中','斎藤','今川']

postnames=rename(prenames)

print(prenames)
print(postnames)







#破壊実験　改良版A
def rename(names):
    renamed=[]
    for i in range(len(names)):
        renamed.append(names[i]+'さん')
    return renamed
prenames=['佐々木','田中','斎藤','今川']
postnames=rename(prenames)
print(prenames)
print(postnames)



#破壊実験　改良版B
def rename(names):
    renamed=names[:]
    for i in range(len(renamed)):
        renamed[i]=renamed[i]+'さん'
    return renamed
prenames=['佐々木','田中','斎藤','今川']
postnames=rename(prenames)
print(prenames)
print(postnames)





#破壊実験C
names=list()
print(f'list(変更前):{id(names)}')
names.append('チャパ子')
print(f'list(変更後):{id(names)}')

name='チャパ子'
print(f'str(変更前):{id(name)}')
name=name+'たそ'
print(f'str(変更後):{id(name)}')



#6.5練習問題
#6-1  a不変、b可変、c可変
#6-2 XYZ
#6-3 ローカル関数name,ageが引数として設定されていない。welcome(name,age)とすればよい。 








a=3
b=1+2
c=4
print(id(a),id(b),id(c))
b+=5
print(id(a),id(b),id(c))


a=[1,2]
b=[1,2]
print(a==b)
print(a is b)
print(id(a),id(b))