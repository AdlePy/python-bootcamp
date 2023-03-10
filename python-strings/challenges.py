# Challenge 1
# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# print(my_str[-17:])

# Challenge 2
# print('It displayed: "You\'ve got an error!"')
# print('\\n means a new line.')
# print('\\ is known as the escape character.')

# Challenge 3
# ft = float(input('Please enter the value in ft: '))
# cm = ft * 30.48
# print(f'The value is {cm:.2f}')

# Challenge 4
#test_str = 'madam'
# print(test_str == test_str[::-1])

# Challenge 5
#test_str = 'madam'
# print(test_str.lower().strip() == test_str[::-1].lower().strip())

# Challenge 6
# sample_string = 'Hello!'
# result_string = sample_string[:2] + sample_string[-2:]
# print(result_string)

# Challenge 7
# sample_string = 'mama'
# result_string = sample_string[0] + sample_string[1:].replace(sample_string[0], '$')
# print(result_string)

# Challenge 8
# n = int(input('Enter the nth index char to remove:'))
# my_str = input('Enter the string to change:')
# first_part = my_str[0:n]
# last_part = my_str[n+1:]
# new_str = first_part + last_part
# print(new_str)

# Challenge 9
# my_str = input('Enter the string to change:')
# new_str = my_str[::2]
# print(new_str)

# Challenge 10
# radius = float(input('Enter circle radius:'))
# area = 3.1415 * radius ** 2
# print(f'The area of a circle with a radius of {radius} is {area:.4f}')

# Challenge 11
# my_str = "Welcome to Romania. romania is an awesome country, isn't it? Hello roMania!"
# sub_string = "Romania"

# convert string to lowercase
# tmp_str = my_str.lower()

# use the count function
# count = tmp_str.count(sub_string.lower())
# print(f'The substring "Romania" appears {count} times in the string.')

# Challenge 12
n = 12384756982
n_comma = f'{n:,}'

print(n_comma)

print(n_comma.replace(',', '.'))