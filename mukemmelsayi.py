sayi= int(input("Sayi giriniz: "))

toplam=0

for i in range(1,sayi):
    if(sayi%i == 0):
     toplam += i

if(sayi == toplam):
   print("Tebrikler mükemmel sayi.")
else:
    print("Mükemmel sayi değil.")