enter_price = 1000

tralling_price = enter_price*(1 - 1/10)
tralling_s_l = enter_price - ((enter_price - tralling_price)/2)

print(tralling_price, tralling_s_l)