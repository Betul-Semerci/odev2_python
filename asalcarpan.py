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

print(asalCarpanBulma(sayi))