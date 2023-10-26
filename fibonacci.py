a=1
b=1

fibonacci = [a,b]

for x in range(18):
     a,b =b,a + b
     fibonacci.append(b)
print (fibonacci)


