#フォーマット関数

name='chapako'
age=80
height=300
print('私の名前は{}で、年齢は{}で、身長は{}cmです。'.format(name,age,height))
print(f'私の名前は{name}で、年齢は{age}で、身長は{height}cmです。')

players_name=input('あなたの名前は？>>')
print(f'あなた{players_name}っていうのね！')
print('300cm?何を言ってるの？')
print(f'{height/100}mやで。')
print('.0って？')
reheight=int(height/100)
print(f'{reheight}','mやね。')


print(f'{age}')
print(f'{age=}')