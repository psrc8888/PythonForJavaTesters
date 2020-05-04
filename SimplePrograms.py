#variable sample, in python data type is not needed
from random import randrange
import  time
import  methodsAndClasses

print(methodsAndClasses.getSum(7,8))
a=5
b=10
print(a+b)
s1="chandan"
s2="automation"
print(s1+s2)

#multi variable

a,b=5,9

#print value with string
print("sum of number is:"+s1)

#and and or sample

if(0>1 and a>b):
    print("true")


#in and not in sample

li=["chandan","raj"]

if("raj" in li):
    print("raj")
    if("raju" not  in li):
        print("no raju")
#if else sample, in python () is not needed and loops and logic statments must have : in the end
if a>b:
    print("true")
elif a<b:
    print("false")
else:
    print("error")

#for loop sample, print number till 10, range runs till length-1

for i in range(11):
    print(i)
for i in range(1,11):
    print(i)
#for each loop sample print num divided by 2

numbers=[1,2,3,4,5,12,3,4,5,4,3,3,45,5]

for i in numbers:
    if i%2==0:
        print(i)

#while sample
i=20
while i>0:
    i=i-1;
    if(i%2==0):
        i=i-2
        print(i)


#method sample ; is needed when we are returning something from method

def getSum(x,y):
    return  x+y+50;

#method calling
print(getSum(a,b))


#type casting sample

a=5;
b=float(a);
print(b)


#access chars from string array

str="my name is chandan"
print(str[1])

#Type cast ,similar to parseint,parsefloat

d=12.05
e=int(d)
print(e)

#generate random number between range
g=randrange(2000,10000)
print(g)

#generate unique timestamp
t=int(time.time())
print(t)

#java split and reverse string method sample

s="my name is chandan"
split=s.split(" ")
split.reverse()
"".join(split)
reverse=""
for i in split:
    reverse=reverse+i+" "

print(reverse,end="")
#reverse sentence sample


#taking input from user,scanner alternative

#x=input("enter a value")
#print("entered value is"+x)

#try catch example
try:
    def finddeno(x):

        return 2/x
except:
    print("error")

print(finddeno(0))
