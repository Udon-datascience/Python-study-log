#第8章

#8.1.2
import urllib.request

url='https://blog.python.org/'
req=urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body=str(res.read())

if 'security' in body or 'vulnerability' in body:
    print('セキュリティに関する記述があります。')
    print('https://blog.python.org/を確認してください。')
else:
    print('調査対象のセキュリティ用語はありませんでした。')





#8.1.3
import sqlite3

with sqlite3.connect('sample.db') as conn:
    cursor =conn.cursor()
    cursor.execute('''
    CREATE TABLE EMPLOYEES(
        ID INTEGER,
        NAME TEXT
    )
    ''')
    cursor.execute("INSERT INTO EMPLOYEES VALUES(1,'Tanaka')")
    cursor.execute("INSERT INTO EMPLOYEES VALUES(2,'Suzuki')")






import sqlite3

with sqlite3.connect('sample.db') as conn:
    cursor =conn.cursor()
    cursor.execute('SELECT ID, NAME FROM EMPLOYEES')
                    
    for row in cursor.fetchall():
        print(row[0]);print(row[1])



#ボタン付きウィンドウの作成
import tkinter as tk
root=tk.Tk()
root.geometry('240x240')
root.title('GUI Sample')
button=tk.Button(root,text='Hello,world')
button.pack()
root.mainloop()



import tkinter as tk
root=tk.Tk()
root.geometry('240x240')
root.title('GUI Sample')
button=tk.Button(root,text='会員登録')
button=tk.Button(root,text='検索')
button.pack()
root.mainloop()





#A-3
try:
    price=int(input('料金を入力>>'))
    number=int(input('人数を入力>>'))
    print(f'一人当たり金額は{price/number:.1f}です。')
except ValueError:
    print('料金と人数は整数を入力してください。')
except ZeroDivisionError:
    print('人数には0を入力できません。')

print('プログラムを終了します。')




