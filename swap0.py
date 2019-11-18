# Author-----Sanjeevsam
#Date----18/11/2019

def swap(c,d):   #swaping using third variable
    temp=c
    c=d
    d=temp
    print(f"after swap number a={c} and b={d}")


a=int(input('enter first integer: \n'))
b=int(input('enter second integer: \n'))
print(f"before swap number a={a} and b={b}")

swap(a,b)
print(f"after swap number a={a} and b={b}") 
# last print func.  gonna print original value of a and b
# because you send copy of a and b to swap funtc.

