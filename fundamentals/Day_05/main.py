import random
#random metodu ile 1-100 arasndan random eded yaratmaq 
number=random.randint(1,100)

'''  Number Guessing Game  '''

print("               Wolcame to My number guessing game!               ")

print("  RULES(I know nobody don't love rules)  ")

print(" 1 ve 100 intervalinda eded texmin ede bilersen. ")
print(" 7 texmin haqqin var ")

# play=input("DO YOU WANT TO PLAY MY GAME ?(PLEASE PLAY),YES or NO: ").lower() -> bu hisseni umumi dovru if-else blokuna elave etdikde xeta verdi 

    
while True:
    guess=int(input("texminin nedir? : "))
    guesses=1
    if guess!=number:
        print("Yanlis, 6 haqqiniz qaldi")
        if guess>number:
            print("daha kicik eded texmin edin ")
        else:
            print("daha boyuk eded texmin edin")
        guess=int(input("texmininiz nedir? : "))
        guesses+=1
        if guess!=number:
            print("Yanlis, 5 haqqiniz qaldi")
            
            if guess>number:
                print("daha kicik eded texmin edin ")
            else:
                print("daha boyuk eded texmin edin")
            guess=int(input("texmininiz nedir? : "))
            guesses+=1
            if guess!=number:
                print("Yanlis, 4 haqqiniz qaldi")
                
                if guess>number:
                    print("daha kicik eded texmin edin ")
                else:
                    print("daha boyuk eded texmin edin")
                guess=int(input("texmininiz nedir? : "))
                guesses+=1
                if guess!=number:
                    print("Yanlis, 3 haqqiniz qaldi")
                    
                    if guess>number:
                        print("daha kicik eded texmin edin ")
                    else:
                        print("daha boyuk eded texmin edin")
                    guess=int(input("texmininiz nedir? : "))
                    guesses+=1
                    if guess!=number:
                        print("Yanlis, 2 haqqiniz qaldi")
                        
                        if guess>number:
                            print("daha kicik eded texmin edin ")
                        else:
                            print("daha boyuk eded texmin edin")
                        guess=int(input("texmininiz nedir? : "))
                        guesses+=1
                        if guess!=number:
                            print("Yanlis, 1 haqqiniz qaldi")
                            
                            if guess>number:
                                print("daha kicik eded texmin edin ")
                            else:
                                print("daha boyuk eded texmin edin")
                            guess=int(input("texmininiz nedir? : "))
                            guesses+=1
                            if guess!=number:
                                print("Yanlis, 0 haqqiniz qaldi")
                                
                                if guess>number:
                                    print("daha kicik eded texmin edin ")
                                else:
                                    print("daha boyuk eded texmin edin")
                                guess=int(input("texmininiz nedir? : "))
                                if guesses>7:
                                    print(f"Haqqiniz bitdi, Uduzdunuz. Eded: {number}")
                            else:
                                print(f"Tebrikler . Eded: {number} , Texmin sayi: {guesses}")
                                break                  
                        else:
                            print(f"Tebrikler. Eded: {number} , Texmin sayi: {guesses}")
                            break
                    else:
                        print(f"Tebrikler . Eded:{number} , Texmin sayi: {guesses}")
                        break
                else:
                    print(f"Tebrikler. Eded: {number} , Texmin sayi: {guesses}")
                    break
            else:
                print(f"Tebrikler ,Eded: {number} , Texmin sayi: {guesses}")
                break
        else:
            print(f"Tebrikler ,Eded: {number} , Texmin sayi: {guesses}")
            break
    else:
        print(f"Tebrikler ,Eded: {number} , Texmin sayi: {guesses}")
        break
