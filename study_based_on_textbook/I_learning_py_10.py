#第３章

food=input('あなたの好きな食べ物は？>>')
if food=='うどん':
    print('香川しか勝たん')
else:
    print('相容れぬな……')


score=input('点数を入力してください')
score=int(score)
if score==100:
    print('おめでとう。フルスコアね。')
elif 80<=score<100:
    print('惜しい')
else:
    print('不合格')


food=input('好きな食べ物は？')
if 'うどん'in food:
    print('分かってるね。')
else:
    print('ふーん。')



scores={'koku':90,'suu':100,'ei':80}
key=input('追加する科目を入力してください')
if key in scores:
    print('すでに追加されています。')
else:
    date=int(input('得点を入力>>'))
    scores[key]=date
print(scores)


score=int(input('試験の点数を入力'))
print(score>=60)


score=int(input('点数を入力してください>'))
if score<=100 and score>=60:
    print('合格')


score=()
if score:
    print('true')
else:
    print('false')



score=3
if score==2:
    print('true')
else:
    pass




score=input('得点を入力してください。>>')
check=type(score)
if check!='int':
    print('エラー：得点を正しく入力してください。')
elif score<0 or score>100:
    print('正常な得点を入力してください。')
else:
    print('確認しました。')



initial='K'
if initial=='K':
    print('yes')
else:
    print('no')


80<=point<256
(bmi<20)or(bmi>25)

amari=year%4
if amari==0:
    print('割り切れます')


day=20
if not((day==28) or(day==30)):
    print('ok')
else:
    print('no')



#3-3
if (Error==False)and(n<100):
    print('valid')


number=int(input('数を入力してください。>>'))
amari=number%2
if amari==0:
    print('偶数です。')
else:
    print('奇数です。')


word=input('会話してみましょう！>>')
if 'こんにちは'in word:
    print('ようこそ！')
elif '景気は？' == word:
    print('ぼちぼちです。')
elif 'さようなら' in word:
    print('お元気で！')
else:
    print('どうしました？')



number=int(input('数を入力してください。>>'))
div='偶数'if number%2==0 else'奇数'
print(f'{div}です。')



#第４章
count=0
while count<4:
    count += 1
    print(f'ひつじが{count}匹')
print('おやすみなさい。')


count=0
while count<4:
    print(f'ひつじが{count}匹')
print('おやすみなさい。')



#4-4
is_awake=True
count=0
while is_awake==True:
    count+=1
    print(f'羊が{count}匹')
    state=input('もう眠りそうですか？>> y/n')
    
    if state=='y':
        is_awake=False
    else:
        pass
print('おやすみなさい。')



#4-5
count=0
student_num=int(input('学生の数を入力>>'))
score_list=list()
while count<student_num:
    count+=1
    score=int(input(f'{count}人目の試験の点数を入力>>'))
    score_list.append(score)
print(score_list)
total=sum(score_list)
print(f'平均点は{total/student_num}点です。')



#4.2
for cat in range(3):
    print('chipi')


for num in range(3):
    print('chipi')



#4.3
ages=[28,30,51,60,34,22,33]
limited_ages=[]
count=0
while count<len(ages):
    if 30<=ages[count]<40:
        limited_ages.append(ages[count])
    count+=1
print(limited_ages)



#4.3
ages=[28,30,51,60,34,22,33,37,22,35]
num=3     #集めたいサンプル数
samples=list()
for age in ages:
    if 30<=age<40:
        if len(samples)<num:
            samples.append(age)
        else:
            break
print(samples)


space=['chipi','happy','dubi','huh']
great_cats=[]
for cat in space:
    if 'a' in cat:
        great_cats.append(cat)
    else:
        pass
print(great_cats)



space=['chipi','happy','dubi','huh']
great_cats=[]
for cat in space:
    if 'a' in cat:
        great_cats.append(cat)
    else:
        break
print(great_cats)




#自作練習プログラム
samples={'a':13,'b':43,'c':25,'d':46,'e':24,'f':35,'g':47,'h':24,'i':14,'j':46}
teenager={}
for key, value in samples.items():
    if 10<value<20:
        teenager[key]=value
    else:
        pass
print(f'十代のメンバーは{teenager}') 
print(samples.keys())
print(sum(samples.values()))


samples={'a':13,'b':43,'c':25,'d':46,'e':24,'f':35,'g':47,'h':24,'i':14,'j':46}
sum(samples.values())
teenager= []
for age in samples.values():
      if 10<age<20:
        teenager.append(age)
      else:
        pass
print(f'十代のメンバーの平均は{float(sum(teenager)/len(teenager)):.2f}歳です。')




#4.3.2　continue 模範解答
ages=[28,50,'secret',20,78,55,22,10,23,'null']
samples=list()
for data in ages:
    if not isinstance(data,int):
        continue
    if data<20 or data>=30:
        continue
    samples.append(data)
print(samples)


#4.3.2 passだと無理なことの確認
ages=[28,50,'secret',20,78,55,22,10,23,'null']
samples=list()
for data in ages:
    if not isinstance(data,int):
        pass
    if data<20 or data>=30:
        pass
    samples.append(data)
print(samples)



#4.3.2 continueなしでごり押しすると
ages=[28,50,'secret',20,78,55,22,10,23,'null']
samples=list()
for data in ages:
    if not isinstance(data,int):
        pass
    else:
        if data<20 or data>=30:
            pass
        else:
            samples.append(data)
print(samples)



#continue,breakはforの次のターンに移行することの実験
ages=[28,50,'secret',20,78,55,22,10,23,'null']
samples=list()
for data in ages:
    if not isinstance(data,int):
        print(data)
    else:
        if data<20 or data>=30:
            continue
        else:
            samples.append(data)
            print(data)
print(samples)





#4-2
count=1
apetite=0
print('カレーを召し上がれ')
while apetite!='n':
    print(f'{count}皿のカレーを食べました')
    apetite=input('おかわりはいかがですか？(y/n)>>')
    if apetite=='y':
        count+=1
    elif apetite=='n':
        break
    else:
        print('無効な入力です')
print('ごちそうさまでした')


#4-3
for num in range(10):
    print(f'{10-num}、', end='')
print('Lift off!')




#4-4(1)
for forward_num in range(9):
    for back_num in range(9):
        print(f'{forward_num+1}×{back_num+1}={(forward_num+1)*(back_num+1)}')



#4-4(2)
for forward_num in range(9):
    for back_num in range(9):
        if forward_num%2==0:
            print(f'{forward_num+1}×{back_num+1}={(forward_num+1)*(back_num+1)}　',end='')
        else:
            continue




#4-4(3)
for forward_num in range(9):
    for back_num in range(9):
        if forward_num%2==0:
            ans=(forward_num+1)*(back_num+1)
            if ans>50:
                break
            else:
                print(f'{forward_num+1}×{back_num+1}={ans}')
        else:
            continue



#4-5 (1)~(4)
temp=[7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]
for each_temp in range(len(temp)):
    print(temp[each_temp])
temp_new=temp.copy()
temp_new[5]='N/A'
print(temp)
print(temp_new)

sum=0
count=0
for each_temp2 in range(len(temp)):
    if type(each_temp2)==int or float:
        sum+=each_temp
        count+=1
    else:
        continue
print(f'日平均気温は{sum/count}')




#4-6
ans='t'
numbers=[1,1]
while ans=='t':
    before=numbers[len(numbers)-1]
    beforere=numbers[len(numbers)-2]
    numbers.append(before+beforere)
    if before*2+beforere>1000:
        ans='f'
    else:
        pass
print(numbers)



#(3)
ratios=[]
for num in range(len(numbers)):
    if num!=0:
        element=numbers[num]
        before_element=numbers[num-1]
        item=int(element/before_element*1000)
        item/=1000
        ratios.append(item)
print(ratios)


#(2)
ratios=[]
for num in range(len(numbers)):
    if num!=0:
        element=numbers[num]
        before_element=numbers[num-1]
        item=round(element/before_element,2)
        item=float(item)
        ratios.append(item)
print(ratios)



