def square1(d1,d2,h):
  if type(d1) and type(d2) and type(h) == int:
   if d1 and d2 and h > 0:
    a=0.5*(d1**2+d2**2)**(0.5)
    s=d1*d2+4*a*h
    return s
   

print ("Найдите площадь поверхности прямой призмы, в основании которой лежит ромб с диагоналями, равными d1 и d2, и боковым ребром, равным h")
print('Чему равно d1,d2,h?')
d1=int(input())
d2=int(input())
h=int(input())
print ('s = ' + str(square1(d1,d2,h)))

assert square1(6,8,10) == 248 , " При условии {} {} {}, функция вернула {}".format(6, 8, 10, square1(6,8,10))
assert square1(-6,-8,-10) == None , " При условии {} {} {}, функция вернула {}".format(-6, -8, -10, square1(-6,-8,-10))
assert square1(0,-8,10) == None , " При условии {} {} {}, функция вернула {}".format(0, -8, 10, square1(-6,-8,-10))
assert square1([6,8,10],8,True) == None , " При условии {} {} {}, функция вернула {}".format([6,8,10], 8, True, square1([6,8,10],8,True))