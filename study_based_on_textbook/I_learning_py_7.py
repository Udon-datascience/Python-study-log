#集合演算練習
even={2,4,6,8,10}
odd={1,3,5,7,9}
prime={2,3,5,7}

print(even | prime) #｜は∪
print(even&prime) #＆は∩
print(even-prime) #差集合
print(even^prime) #対象差　（A∪B）ー（A∩B）　
