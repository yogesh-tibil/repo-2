#Python program to find the minimum among five numbers.
'''a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
d=int(input("enter d number"))
e=int(input("enter e number"))
if a<b and a<c and a<d and a<e:
    print(a)
elif b<c and b<d and b<e:
    print(b)
elif c<d and c<e:
    print(c)
elif d<e:
    print(d)
else:
    print(e)'''

#Python program to check if a given number is prime or not.
'''num=int(input("enter the number"))
for i in range(2,num):
    if(num%i==0):
        print("Not prime number")
        break
if num<2:
    print("not prime number")
else:
        print("Prime Number")'''


#Python program to find the factorial of a number.
'''num=int(input("enter the number"))
fact_num=1
for i in range(1,num+1):
    fact_num*=i
print(fact_num)'''

# Python program to calculate the area of a triangle given its three sides.
'''import math
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
if (a+b)>c and (b+c)>a and (a+c)>b:
    s=(a+b+c)/2
    d=s*(s-a)*(s-b)*(s-c)
    res=math.sqrt(d)
    print(res)
else:
    print("sum of two side should br greater than third side.")'''

# Python program to calculate the area of a triangle given its three sides.
'''import math
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
def area_triangle(a,b,c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        s = (a + b + c) / 2
        d = s * (s - a) * (s - b) * (s - c)
        res = math.sqrt(d)
        return res
    else:
        return "sum of two side should br greater than third side."

print(area_triangle(a,b,c))'''

# Python program to swap two numbers without using a temporary variable.
'''a=int(input("enter the number"))
b=int(input("enter the number"))
a=a+b
b=a-b
a=a-b
print(a,b)'''

# Python program to swap two numbers without using a temporary variable.
'''def swap_number(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
a=int(input("enter the number"))
b=int(input("enter the number"))
swap_number(a,b)'''

# Python program to find the sum of natural numbers up to a given number.
'''num=int(input("enter the number"))
res=0
for i in range(0,num+1):
    res+=i
print(res)'''

'''def natural_number(num):
    res=0
    for i in range(0,num+1):
        res=res+i
    return res
num=int(input("enter the number"))
print(natural_number(num))'''

# Python program to check if a number is even or odd.
'''num=int(input("enter the number"))
if num%2==0:
    print("even")
else:
    print("odd")'''

# Python program to calculate the square root of a number.
'''a=int(input("enter the number"))
b=math.sqrt(a)
print(b)'''


'''def sqrt(num):
    a=math.sqrt(num)
    return a

num=int(input("enter the number"))
print(sqrt(num))'''

# Python program to calculate the average of three numbers.
'''a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
sum=(a+b+c)/3
print(sum)'''


# Python program to calculate the average of three numbers.
'''def average(a,b,c):
    sum=(a+b+c)/3
    return sum
a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
print(average(a,b,c))'''

# Python program to check if a given year is a leap year or not.
'''year=int(input("enter the number"))
if (year % 4 == 0):
    if (year%100==0):
        if(year%400==0):
            print("it is a leap year")
        else:
            print("it is not leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")
'''

# Python program to check if a given year is a leap year or not.
'''year=int(input("enter the year:"))
if(year%4==0 and year%100!=0):
    print("it is a leap year")
elif(year%400==0):
    print("it is a leap year")
else:
    print("it is not leap year")'''