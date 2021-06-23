# Kasus 4 - IPK ( 20 Point )

print('\n')

z = float(input("Nilai IPK : "))
g = ' Dengan Pujian / Cumlaude'
h = ' Sangat memuaskan / Very Good'
i = ' Memuaskan / Good'
j = ' Kurang Memuaskan / Bad '
print('\n')

if z >= 3.5 :
    print(g)
elif 3.0 <= z < 3.5:
    print(h)
elif 2.75 <= z < 3.0:
    print(i)
else:
    print(j)
    
print('\n' , '---------------------------------------' , '\n')