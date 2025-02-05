weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = weight / (height ** 2)

print(f"Your BMI is: {BMI:.2f}")

if BMI > 25:
    print("You are overweight. You need to work out more and watch your diet.")
elif 18.5 <= BMI <= 25:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")
