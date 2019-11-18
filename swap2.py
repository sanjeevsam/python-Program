# Author-----Sanjeevsam
#Date----18/11/2019
def swap(c,d):
    d=c^d      #swaping without third vriable using bitwise logic operator
    c=d^c
    d=d^c
    print(f"after swap number a={c} and b={d}")


a=int(input('enter first integer: \n'))
b=int(input('enter second integer: \n'))
print(f"before swap number a={a} and b={b}")

swap(a,b)