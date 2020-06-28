def square(v):
 if type(v) == int:
   if v > 0:
     a=v**(1/3) 
     s=6*a*a
     return s

print ("Объем куба равен v. Найдите площадь его поверхности. ")

print('Чему равно V?')
v=int(input())
print ('s = ' + str(square(v)))

assert square(8) == 24 , " При условии {}, функция вернула {}".format(8, square(8))
assert square(-8) == None , " При условии {}, функция вернула {}".format(-8, square(-8))
assert square(0) == None , " При условии {}, функция вернула {}".format(0, square(0))
assert square([0,1,2]) == None , " При условии {}, функция вернула {}".format([0,1,2], square([0,1,2]))
assert square(True) == None , " При условии {}, функция вернула {}".format(True, square(True)) 