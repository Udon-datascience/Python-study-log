

#練習2.3

a_hobby={input('Aの趣味1'),input('Aの趣味2'),input('Aの趣味3'),input('Aの趣味4')}
b_hobby={input('Bの趣味1'),input('Bの趣味2'),input('Bの趣味3'),input('Bの趣味4')}
input('心の準備ができたらEnterキーを押してください')
same=len(a_hobby&b_hobby)/len(a_hobby|b_hobby)*100
print(f'相性度は{float(same):.1f}％です。')


