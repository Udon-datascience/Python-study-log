#セット練習
sosuu={3,7,5,2,3}
print(sosuu)
print(len(sosuu))
print(list(sosuu))
print(tuple(sosuu))
key=['a','b','c','d']

sosuu=dict(zip(key,sosuu)) #チャパ子はこの関数変換をいつも忘れるからダメだよねぇ
print(sosuu)
print(sosuu['a'])



#dict in dict
neego_member={'まふゆ','瑞希','奏','絵名'}
dasyo_member={'司','えむ'}
unit={
    'ニーゴ':neego_member,
    'ダショ':dasyo_member
}
print(unit)
print(neego_member)


odd=[1,3,5]
even=[2,4,6]
natural=[odd,even]
print(odd)
print(natural[0])   #oddが表示される
print(natural[1])   #evenが表示される
print(natural[1][0])


chara={
   'まこ':{'面白い','かわいい','変人'},
   'こう':{'かわいい','優しい','お人よし'}
}
common_chara=chara['まこ']&chara['こう']
print(common_chara)