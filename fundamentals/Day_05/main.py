import random

print("Number Guessing Game")
print("1 və 100 intervalında ədəd təxmin edin. 7 haqqınız var.")

play = input("Oynamaq istəyirsiniz? (yes/no): ").strip().lower()

if play == 'yes':
    number = random.randint(1, 100)
    max_guesses = 7
    guesses_taken = 0
    previous_distance = None

    while guesses_taken < max_guesses:
        guess = int(input(f"Təxmininiz nədir? ({max_guesses - guesses_taken} haqqınız qaldı): "))
        guesses_taken += 1
        
        if guess == number:
            print(f"Təbriklər! Ədədi {guesses_taken} cəhddə tapdınız.")
            break
            
        # İsti-Soyuq məntiqi
        current_distance = abs(number - guess)
        
        if previous_distance is not None:
            if current_distance < previous_distance:
                print("İstiləşdi (Daha yaxınsınız).")
            elif current_distance > previous_distance:
                print("Soyudu (Daha uzaqlaşdınız).")
            else:
                print("Eyni məsafə.")
        else:
            print("Yanlışdır.")
            
        previous_distance = current_distance
        
        # Əlavə ipucu
        if guess > number:
            print("Daha kiçik ədəd təxmin edin.")
        else:
            print("Daha böyük ədəd təxmin edin.")
            
    else:
        # Bu 'else' while dövrünə aiddir. Yalnız break işləmədikdə (haqq bitdikdə) icra olunur.
        print(f"Haqqınız bitdi. Uduzdunuz. Gizli ədəd: {number}")
else:
    print("Oyun bitdi.")