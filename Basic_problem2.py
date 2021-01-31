print("Hello worls")
#In this question we use conditional statments:
num1 =  float(input('Please enter the first number'))
num2 = float(input('Please enter the second number'))

if num1<0:
    num1 *= 2

else:
    num1 *=3

if num2<0:
    num2 *= 2

else:
    num2 *=3

print("The result is",num1*num2)

#write code for function getspecialNum using try and expect block

def getspecialNum():
     while 1:
        try:
            num1 = float((input("Enter the number greater than 10:\n")))
            
            if(num1 > 10):
                print("Thank you")
                break
            else:
                print("Number is less tahn 10")

        except(ValueError):
            print("This is not the number")

getspecialNum()


 
