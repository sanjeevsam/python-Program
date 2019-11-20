# author ---- sanjeevsam
# date ------ 20/11/2019
# factorial of number using simple function
def fact_number(x):
    fact=1
    if x<0:
        print('invalid input ,please input positive value')
    elif x>0:
        for i in range(1,(x+1)):
            fact*=i
        print(f"factorial of {x} is {fact}")
    else:
        print("factorial of 0 is 1")


   
        
number=int(input('enter a number for factorial :'))
fact_number(number)


