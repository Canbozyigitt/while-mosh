i=0
while(i<3):
    print("oyuna hoşgeldiniz")
    print("start - to star to car")
    print("stop - to stop to car")
    print("quit - to exit")
    cevap=input("Hangisini yapmak istiyorsanız yazınız: ")
    if(cevap=="start"):
        print("to star to car")
        break
    elif(cevap=="stop"):
        print("to stop to car")
        break
    elif(cevap=="quit"):
        print("to exit")       
        break
    else:
        print("I don't understand that ...")         