#小数点以下N桁を表示するプログラム
num=3.141592
print(f'{num:.2f}')

#もしくはround(数値,小数点以下の桁数)
print(round(3.141592,2))



#copy関数
scores1=[10,20,23,45,20,80]
scores2=scores1.copy()
scores2[0]=99
print(scores1)
print(scores2)



#listをコピーするとき（copy関数とほぼ同じなのでcopy関数でいい）
scores1=[10,20,23,45,20,80]
scores2=scores1[:]



#ディクショナリ中のkeyのみ、valueのみを取り出す
scores={'国語':28,'数学':14,'英語':60}
print(scores.keys())    #keyのみ
print(scores.values())    #valueのみ
print(scores.items())    #両方
print(scores['国語'])    #keyから値を取り出す

for k,v in scores.items():           #itemsは取り出したとき、('国語',28)のようにタプルになっている。k,vと書くことで、kには国語が、vには28が分配される。
    if v==60:   #特定のvalueのkeyを取り出す
        print(k)
    else:
        pass







#pyを作る実験(改行のコツ)
newfile=open('trial.py','a')
newfile.write(
    '#trial for learning' + '\n' +
    "print('Hello world')" + '\n'       #pythonが'を誤解しないように、適宜改行したり、"を使ったりするみたい
)
newfile.close()




#外部ライブラリのダウンロード(下記を実行するだけ)
# pip install matplotlib
# pip install requests




#ライブラリ（道具箱一覧が並べられた棚） ＞ モジュール（ファイル一個単位・道具箱） ＞ 変数、関数
#パッケージ（フォルダ・自己流でいくつかの道具箱を選んでパッキングしたもの） ＞ モジュール（ファイル一個単位・道具箱）





'''
#文字に色を付ける
ANSIエスケープシーケンス一覧

print("\033[  文字コード  m  文字列  \033[0m")
#上記コードは空白は除く。関数を埋め込むならfを忘れずに。


| 色    | コード |

| 黒    | 30  |
| 赤    | 31  |
| 緑    | 32  |
| 黄    | 33  |
| 青    | 34  |
| マゼンタ | 35  |
| シアン  | 36  |
| 白    | 37  |


| 装飾   | コード |

| リセット | 0   |
| 太字   | 1   |
| 下線   | 4   |
| 反転   | 7   |
'''

#例コード
print("\033[34m青\033[0m")
print("\033[134m青\033[0m")
print("\033[034m青\033[0m")









'''
if each_char[i] in 'ABCDEFGHIJKLMN':
if each_char[i] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']:

上記は同じ意味。
'''



'''
for i in range(len(lists)):
    print(lists[i])

for element in lists:
    print(element)

上記は同じ意味。後者のほうがpythonらしくてスマート。
'''





'''
githubで作ったリポジトリをクローンする方法

PS C:\Users\natsu\Python-study-log-1> cd..
PS C:\Users\natsu> git clone https://github.com/Udon-datascience/Python-machine-learning-study-log
Cloning into 'Python-machine-learning-study-log'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (4/4), done.
PS C:\Users\natsu> 
'''