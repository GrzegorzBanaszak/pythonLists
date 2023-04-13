def bmi(weight, height):
    user_bmi = weight / height ** 2

    if user_bmi < 18.5:
        print("Masz niedowagę")
    elif user_bmi > 18.5 and user_bmi < 24.99:
        print("Twoja waga jest prawidłowa")
    else:
        print("Masz nadwagę!!!")


bmi(90, 1.75)
