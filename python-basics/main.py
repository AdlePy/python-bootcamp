from math import isclose


# Variables
# It is recommended to use snake_case while naming variables
# Names could contain _, digits and letters but not special characters
miles = 10
print(miles)
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

product_name = 'Legion S'
quantity = 1
price = 1245.24
sold = False

# To declare a constant in python use uppercase letters
PI = 3.14
SECONDS_IN_HOUR = 3600
DAYS_IN_WEEK = 7

# Python is dynamically typed language
score = 10
print(type(score))
print(id(score))

score = 'Not assigned'
print(type(score))
print(id(score))

# Builtin data types
age = 40
name = 'Dan'
is_old = True
height = 1.72
disabilities = None
grocery_list = ['milk', 'eggs', 'spaghetti']
family = {
    'wife': 'Ann',
    'son': 'Andrei',
    'mother': 'Emilie',
    'father': 'Kirk'
}

# Numbers and operators with numbers
# There are 3 types of numbers in python: int, float and complex
print(1 + 2)
print(2 - 2)
print(2 * 5)
print(10 / 5)
print(11 // 2)
print(2 ** 3)
print(8 % 5)
print(2 + 2 * 2 ** 3)

a = 2
b = 9
c = a / b
print(c)
d = a ** b
print(d)
e = a % b
print(e)
f = a * b
print(f)

distance_miles = 2806
distance_km = distance_miles * 1.609

temperature_c = 25
temperature_f = (temperature_c * 9/5) + 32
print(temperature_f)

inch = 17
cm = inch * 2.52
print(cm)

year_in_seconds = 365 * 24 * 3600
print(year_in_seconds)

# Assignments operators
num = 10

num += 2
print(num)

num -= 3
print(num)

num /= 3
print(num)

num *= 2
print(num)

num **= 3
print(num)

num %= 4
print(num)

# Math functions
quotient, remainder = divmod(14, 6)
print(quotient, remainder)

print(pow(5, 2))

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(max([1, 2, 3]))

print(round(5.32424, 4))

# Comparison operators
print(2 == 2)
print(2 > 1)
print(1 < 0)
print(2 >= 3)
print(3 <= 3)
print(1 != 0)

# Identity operators
num1, num2 = 1, 3
print(num1 is num2)

# Floating point arithmetics
print(format(1/3, '.20f'))

a = 0.1 * 3
b = 0.3
print(a == b)


x = 0.000001
y = 0.000002
print(isclose(x, y, abs_tol=0.01))

# Challenge 1
num = 1
print(num, type(num))

stock_price = 24.4
print(stock_price, type(stock_price))

is_fun = True
print(is_fun, type(is_fun))

word = 'hello'
print(word, type(word))

products = ['mouse', 'keyboard']
print(products, type(products))

# Challenge 2
my_name = 'Andrei'
value = 100
word = 'Hello'
print(word)

# Challenge 3
best_friend = 'Anne'
print('My best friend is ', best_friend)

age_var = 18
print(age_var == 18)

a, b = '10', '20'
print(a + b)

print('To comment a line of code use # symbol at the beginning of line.')

# Challenge 4
a = (16 / (2 + 6) / 2) ** 2
print(a)


# Challenge 5
ipv6_no = 2 ** 128
print('There are', ipv6_no, 'IPv6 available in the world!')

# Challenge 6
company_revenue = 45897513
relative_profit = 45897513 * 12.7 / 100
print(round(relative_profit, 2))

# Challenge 7
a = 0.1
b = 0.3
print(isclose(a * 3, b, abs_tol=0.1))
