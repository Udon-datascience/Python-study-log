#第7章

list=[]
list.append(1)


text=input('何を記録しますか？')
file=open('diary.txt','a')
file.write(text+'\n')
file.close()

import os
print(os.getcwd())

with open('diary.txt','a')as file:
    file.write('additional texts'+'\n')





with open('diary.txt','a')as file:
    file.write('bumbaboon'+'\n')



#wordを作る実験（失敗）
newfile=open('asap_copy.docx','a')
newfile.write('吾輩は猫である。名前はまだない。'+'\n')
newfile.close()



#pyを作る実験
newfile=open('trial.py','a')
newfile.write(
    '#trial for learning' + '\n' +
    "print('Hello world')" + '\n'       #pythonが'を誤解しないように、適宜改行したり、"を使ったりするみたい
)
newfile.close()






#モジュール練習
import math
print(f'円周率は{math.pi}です。')
print(f'小数点以下を切り捨てれば{math.floor(math.pi)}です。')
print(f'小数点以下を切り上げれば{math.ceil(math.pi)}です。')




from math import floor
from math import pi
print(f'円周率は{pi}')
print(f'小数点以下を切り捨てると{floor(pi)}')







#ライブラリ（道具箱一覧が並べられた棚） ＞ モジュール（ファイル一個単位・道具箱） ＞ 変数、関数
#パッケージ（フォルダ・自己流でいくつかの道具箱を選んでパッキングしたもの） ＞ モジュール（ファイル一個単位・道具箱）



import time
now = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", now))





#7.4 パッケージの利用
import http.client
conn=http.client.HTTPConnection('www.python.org')  #httpパッケージ ”ごと”　clientモジュールの、HTTPConnection関数　をインポートしている



from http.client import HTTPConnection
conn=HTTPConnection('www.python.org')     #httpパッケージの、clientモジュールの、HTTPConnection関数 ”のみ” を抜き出して　インポートしている






#importa実験
import string
import random

random_string = ''.join(random.choice(string.ascii_letters) 
                        for _ in range(10))
print(random_string)     # ランダムに生成された英字の文字列（実行のたびに異なります）



#ChatCPT例示
import matplotlib.pyplot as plt
scores=[19,48,27,39,92,10]
y=[2,4,6,8,10,12]
plt.plot(scores,y)
plt.show()







#matplotlib 参考書例示（jupiter notebook, google colabじゃないと動かない）
%matplotlib inline
import matplotlib.pyplot as plt
scores=[19,48,27,39,92,10]
y=[2,4,6,8,10,12]
plt.plot(scores,y)
plt.show()





#matplotlib ChatCPT例示(動く)
import matplotlib.pyplot as plt
weight=[68.4,68.0,69.5,68.6,70.2,71.4]
plt.plot(weight)
plt.show()





#外部ライブラリのダウンロード
pip install matplotlib
pip install requests



#request実験
import requests     #requestはモジュールを指定せずimportする形式
response=requests.get('https://www.python.org/downloads/')
text=response.text
print(text)




#標準ライブラリでrequestを代替する実験（ムズすぎて断念）
import http.client
conn=http.client.HTTPSConnection('www.bing.com/search?qs=HS&pq=goo&sk=CSYN1HS2&sc=13-3&pglt=297&q=google+colab&cvid=ae4daf316b7a48bba3c3c2ca88fabe1c&gs_lcrp=EgRlZGdlKgYIAhAAGEAyBwgAEAAY-QcyBggBEC4YQDIGCAIQABhAMgYIAxBFGDkyBggEEAAYQDIGCAUQLhhAMgYIBhBFGDwyBggHEEUYPDIGCAgQRRg80gEIMjQ3NmowajeoAgiwAgE&FORM=ANNTA1&PC=U531&source=chrome.ob')
conn.request('GET','/downloads/')
response=conn.getresponse()
text=response.read().decode('UTF-8')
print(text[:100])
conn.close()





#7.7 練習問題


#7-1 FTFTF
#7-2
(1)import A.func
(2)import A.func as B

#7-3
from A import func



#7-4
(1)
num_list=[]
for i in range(3):
    num=input(f'{i+1}番目の数字を入力')
    num_list.append(num)
saidai=max([num])
print(saidai)

(2)
pi=3.141592
for i in range(5):
    print(round(pi,i))




#7-5
file=open('sample.txt','r')
copied_file=file.copy()
file.close()
copied_file.close()







#7-6

from random import randint

    #(1)
print('数当てゲームを始めます。'+'\n'+'３桁の数を当ててください！')

    #(2)
answer=[]
for i in range(3):
    num=randint(0,9)
    answer.append(num)


judge=True
while judge==True:

        #(3)
    prediction=[]
    for i in range(3):
        num=int(input(f'{i+1}番目の予想>>'))
        prediction.append(num)


        #(4)
    perfectly_same=0
    set_answer=set()
    set_prediction=set()

    for i in range(3):
        if answer[i]==prediction[i]:
            perfectly_same+=1
        else:
            pass

        set_answer.add(answer[i])
        set_prediction.add(prediction[i])

    partly_same=len(set_answer & set_prediction)-perfectly_same
    print(f'{perfectly_same}ヒット！{partly_same}ボール！')


    #(5)
    if perfectly_same==3:
        print('正解です！')
        judge=False
    
    else:
        wanna=int(input('続けますか？　1:続ける　2:終了>>'))
        if wanna==1:
            continue
        elif wanna==2:
            judge=False
            print(f'正解は{answer}')
        else:
            print('無効な入力です。')




