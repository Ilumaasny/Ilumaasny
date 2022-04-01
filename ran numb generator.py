import random

print("Welcome to the Python random number generator")
print("What is the smallest number you would like to generate")
a= int(input())

print("What is the larges number you would like to generate")
b= int(input())

n= random.randint(a,b)
print(n)
