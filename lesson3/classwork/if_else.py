day = input("What day of the week is it?")

if day == "monday":
    print("Ugh, it's monday.")
elif day == "friday":
    print("Yay, it's almost the weekend!")
elif day == "saturday":
    print("It's the weekend!")
elif day == "sunday":
    print("It's the weekend!")
else:
    print("It's just a regular weekday.")

score = int(input("Your score out of 100: "))
if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A!")