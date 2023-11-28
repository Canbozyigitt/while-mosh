sayi =5
hak=3
kullanılan_hak=0

while (kullanılan_hak<hak):
    tahmin=input("bir sayi giriniz: ")
    if(tahmin!=sayi):
        print("yanlış sayi girdiniz tekrar deneyin")
        kullanılan_hak+=1
    else:
        print("doğru sayıyı bildiniz")    
        break