while True:
    x = int(input("Tek çift kontrol için sayı girin veya çıkış için 0 giriniz.\nDeğer giriniz: "))
    if x == "0":
        print("işlem durdu.".center(50,"-"))
        break
    elif x %2 == 0:
        print(f"{x} sayısı Çift tır".center(50,"-"))
    elif x % 2 == 1:
        print(f"{x} sayısı Tek tır".center(50,"-"))




