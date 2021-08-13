
total_price = 3420
price_1000 = total_price//1000
price_100 = (total_price-(price_1000*1000))//100
price_10 = (total_price-(price_1000*1000)-(price_100*100))//10

print(price_1000)
print(price_100)
print(price_10)

print("1000원 : ", price_1000)
print("100원 : ", price_100)
print("10원 : ", price_10)
print("필요한 동전의 개수 : ", (price_100+price_10))
