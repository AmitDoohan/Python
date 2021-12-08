def my_power(a:int,b:int):
    base=a
    if (type(a) == int and type(b) == int):
       while(b!=1):
            if(b%2==0):
                a=a*a
                b=b/2
            else:
                a=a*base
                b=b-1
    else:
        print("must enter natural numbers")
    return a



print(str(my_power("fhjd",5)))


