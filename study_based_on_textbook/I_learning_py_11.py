#第５章
def hello():
    print('こんにちは。チャパ子です。')

hello()



def hello(name):
    print(f'こんにちは、{name}です。')

hello('world')
hello('chipi')



def input_scores(name):
   name=input('名前は？>>')
   print(f'{name}の試験結果を入力してください')



def calc_ave(scores):
    ave=sum(scores)/len(scores)
    print(f'平均点は{ave}です')


scores={'国語':28,'数学':14,'物理':64,'化学':24}
calc_ave(scores.values())



def plus(x,y):
    answer=x+y
    return answer

def plus(x,y):
    return x+y

cat=plus(100,50)
print(cat)



cat=print('a')
print(cat)
print(type(cat))


def cats():

    a=input('catを入力１')
    b=input('catを入力２')
    return 

print(cats())




#デフォルト引数
def eat(bf,l,de=(),di='うどん'):
    print(f'朝は{bf}、昼は{l}、夜は{di}、デザートは{de}')

eat('コーンフレーク','焼き魚',('チョコ','クッキー','ケーキ'))
eat('コーンフレーク','焼き魚',('チョコ','クッキー','ケーキ'),di='生姜焼き')



def eat(bf,l,*de,di='うどん'):
    print(f'朝は{bf}、昼は{l}、夜は{di}、デザートは{de}')

eat('味噌汁','魚','ケーキ','クッキー')





#共通テスト圧縮得点計算プログラム
def kyoute(koku,suu,ei,ri=(),sya=()):
    total=(koku/2)+suu+ei+(sum(ri)/2)+(sum(sya)/2)  
    return total

print(kyoute(180,89,94,(86,90),(86,)))



#5-23比較
name='チャッパ子'
def rename():
    global name
    name='ぷぷ'
def hello():
    print('こんにちは'+name+'さん。')
rename()
hello()




#5-23比較
name='チャッパ子'
def rename():
    global name
    name='ぷぷ'
def hello():
    print('こんにちは'+name+'さん。')
hello()



def rename():
    name='chapako'
    print(name)
name='dubi'
rename()
print(name)


name='dubi'
def rename():
    name='chapako'
    print(name)
rename()
print(name)



name='dubi'
def rename():
    global name
    name='chapako'
    print(name)
rename()
print(name)















#5-1　型　null,float,str,list,null
(1)
def weather():
    print('今日は晴れです。')


(2)
def calc_circle_area():
    radius=float(input('円の半径を入力してください>>'))
    area=3.14*radius*radius
    return area

calc_circle_area()


(3)
def nowstr(hour,minutes,second):
    return '{hour}時{minutes}分{second}秒'

(4)
def nowint(hour,minutes,second):
    return [hour,minutes,second]


(5)
def is_leapyear(year):
    if year%4==0:
        return True
    else:
        return False

print(is_leapyear(2026))










#5-2
def is_leapyear(year):
    if year%400==0:
        print('うるう年です')

        if year%4!=0:
            print('うるう年ではありません')
        elif (year%4==0)and(year%100==0):
            print('うるう年ではありません')
        else:
            print('うるう年です')



#5-3
#４行目の後にprint('疲れたら歩きます')

#5-4　　FTTTT


#5-5
(1)
def int_input():
    amount=int(input('支払総額を入力してください>>'))
    people=int(input('参加人数を入力してください>>'))
    return [amount,people]

(2)
def calc_payment(amount,people=2):   #割り勘計算プログラム
    dnum=amount/people
    if dnum%100==0:    #切り上げがないとき
        pay=dnum
    else:
        pay=100+(dnum//100)*100   #100未満を切り上げ
    payorg=amount-(pay*(people-1))     #幹事は超過分をもらう

(3)
def show_payment(pay,payorg,people=2):
    print(f'一人当たり{pay}円({people}人)、幹事は{payorg}円です')
