kontrol = 0
while kontrol < 5:
    kontrol += 1
    sayi = int(input("Sayıyı Giriniz : "))

    if sayi > 1:

        for i in range(2, sayi):
            if (sayi % i) == 0:
                print(sayi, " Asal Sayı Değildir.")
                break
        else:
            print(sayi, " Asal Sayıdır.")

    else:
        print(sayi, " Asal Sayı Değildir.")

