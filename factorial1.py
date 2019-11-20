# author ---- sanjeevsam
# date ------ 20/11/2019
def fact_number(x):
    if x>0:
        return x*fact_number(x-1)
    elif x<0:
        return 'invalid input,please give positive value'
    else:
        return 1
        
number=int(input('enter a number for factorial :'))
print(f"factorial of {number} is {fact_number(number)}")

