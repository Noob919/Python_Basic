#Topics Covered in this files are
#variable declaration
#how to use formatted strings
#How to get user input
#conditonal statements
# for loop 


# Problem1: Create a variable called health and give it a value of 100. Subtract 10 from it and 
# store the result in health.

health = 100
health = health - 10
print(health)

# Problem2: Prompt for age and store it in an integer variable

age =  float(input("Enter your age is years:"))
print('Your age is %i years'  %age)

# Problem3: Prompt for a distance and store it in a float variable

distance = input("Please enter the distance you have covered:")
distance = float(distance)
print("Distance you covered is %.3f km"  %distance)

# Problem4: Write a program to ask for an age in years and display the age in days 
# (assume 365 days per year)

age_in_days =  age *365
print("Your age in days is %.2f days" %age_in_days)

# Problem5:  Write a program that displays how far a bike moves, given the diameter of
# a wheel, and the number of revolutions (prompt for the two values, as floats).

diameter_of_wheel = float(input('Enter the diameter of wheel in meters:'))
number_of_revs = float(input("Enter the number of revolutions"))
distance_moved =  diameter_of_wheel*number_of_revs
print("Your bike travels around %.4fm" %distance_moved)

# Problem6: Display the integers from 1 to 10, with their squares:
# 1	1
# 2	4
# 3	9....

for num in range(1,11):
    print(num, "the square of this is",num*num)

# Problem7: Display the integers from -5 to 3
for nums in range(-5,4):
    print(nums)

# Problem8: Ask for an upper limit, and if the number entered is > 1 
# then display all the integers from 1 to that limit

upper_limit =  int(input("Enter the upper limit "))
if (upper_limit >1 ):

    for i in range(1,upper_limit+1):
        print(i)
else:
    print("Your is less than or equal to 1...Sorry")
