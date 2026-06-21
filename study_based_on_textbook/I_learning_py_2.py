price=input('金額を入力してください>>')
number=input('人数を入力してください>>')
price=int(price)
number=int(number)
per_price=price/number
per_price=int(per_price)
print('一人当たりの金額は',per_price,'円です。')

per_price=str(per_price)
print('一人当たりの金額は'+per_price+'円です。')