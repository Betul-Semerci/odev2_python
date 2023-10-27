def asalCarpanBulma(sayi):
    asalCarpanlar =[]
    carpan =2
    while carpan <= sayi:
        if sayi % carpan == 0:
            asalCarpanlar.append(carpan)
            sayi //=carpan
        else:
            carpan +=1
    return asalCarpanlar

sayi = int(input("Lütfen bir sayi giriniz: "))
#print("f{sayi} sayısının asal çarpanları: {asalCarpanBulma}")
print(asalCarpanBulma(sayi))