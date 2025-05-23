print("Welcome to the BMI Calculator!")

# Prompt for weight with validation
while True:
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        if weight <= 0:
            print("Weight must be a positive number. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Prompt for height with validation
while True:
    try:
        height = float(input("Please enter your height in meters: "))
        if height <= 0:
            print("Height must be a positive number. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Calculate BMI and round to 2 decimal places
bmi = weight / (height ** 2)
rounded_bmi = round(bmi, 2)

# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Display the result
print(f"Your BMI is {rounded_bmi}, which is classified as {category}.")
