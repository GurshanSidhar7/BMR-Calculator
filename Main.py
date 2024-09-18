print()
#Import
from functions import bmr_calc_Man, bmr_calc_Woman

#Introduction Prompt
print("""It seems you've come to calculate your BMR! Wether you're apporaching your journey into 
fitness in the hopes of losing weight, or putting on some muscle the BMR is essential in acheiving your
goals. Don't fret on crunching any numbers, you let us handle that!""")

#Spacer
n= 5
for i in range(n):
    print("-")

#Gender Check:
gender= input("Are you a Man or Woman(M or W): ")

#Inputs
weight= float(input("What is your weight in KG?: "))
height= float(input("What is your height in CM?: "))
age= int(input("What is your age in years?: "))

if gender == "M" or gender == "m":
    calc=  bmr_calc_Man(weight, height, age)
    print(calc)
else:
    calc= bmr_calc_Woman(weight, height, age)
