weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in cm: '))
bmi_index = (weight / pow(height, 2)) * 1000
print('Your BMI:', bmi_index)
