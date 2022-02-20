#!/usr/bin/env python3
monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures)

monday_temperatures.append(8.1)
print(monday_temperatures)

print(monday_temperatures.index(8.1))

monday_temperatures.append(101.1)
monday_temperatures.append(88.3)
print(monday_temperatures)
print(monday_temperatures[1:4])
print(monday_temperatures[-4:-1])

my_hello_list = ['hello']
print(my_hello_list[0])
print(my_hello_list[-1])
print(my_hello_list[:3])

my_second_list = ['how', 'are', 'you', 'hello']
my_hello_list.extend(my_second_list)
print(my_hello_list)
print(my_hello_list.count('hello'))

x = my_hello_list.copy()

print(x)
print(x.count('how'))
print(x.index('hello'))

my_hello_list.insert(len(my_hello_list), 'Bob')
print(my_hello_list[-1])
