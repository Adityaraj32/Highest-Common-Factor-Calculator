'''
Author: Adityaraj Yadav 
Date: 19 January 2022
Project Name: Highest Common Factor Calculater
Purpose:For Practising Purpose
'''


print("\t\t\t\t\t\Welcome to the Highest Common Factor Calculator\n")

Num_1 = int(input("Enter the first number: "))
Num_2 = int(input("Enter the Second number: "))

# Taking the smaller number for the program because to take the HCF the smaller number is divided from the larger
if Num_2 > Num_1:
    Min = Num_1
else:
    Min = Num_2

# Running the program from one to the smaller number and dividing the number
for i in range(1, Min+1):
    if Num_1 % i == 0 and Num_2 % i == 0:
        HCF = i

print(f"The highest common factor for the {Num_1} and {Num_2} is {HCF}")
