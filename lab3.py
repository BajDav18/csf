n = 12
series = 'spam'
if series == 'fibonacci':
     a, b = 0, 1
     while b < n:
         print b
         a, b = b, a+b
elif series == 'sum':
    print range(3, (3*n), 3)
else: 
    print "invalid string" 