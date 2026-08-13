# BMI Calculator

print("===== BMI Calculator =====")

try:
    # User Input
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    # Input Validation
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")
    else:
        # BMI Calculation
        bmi = weight / (height ** 2)

        # BMI Classification
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display Result
        print("\n===== Result =====")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Error: Please enter valid numeric values.")