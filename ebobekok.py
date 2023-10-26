sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

if (sayi1>sayi2):
    kucuksayi=sayi2
else:
    kucuksayi=sayi1
for i in range(1,kucuksayi+1):
    if(sayi1 % i==0) and (sayi2%i ==0):
        ebob = i
        ekok = (sayi1*sayi2)//ebob

print ("EBOB: ",ebob)
print ("EKOK: ",ekok)       
