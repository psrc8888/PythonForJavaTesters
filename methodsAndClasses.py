#method calling sample with generic type(any data type)
def getSum(a,b):
    return  a+b

print(getSum(4,5))
print(getSum('a','b'))
print(getSum("chandan","is my name"))
print(getSum(4.5,5.0))


#method sample for calling method with n number of data types

def getSum2(*a):
    return a[1]

print(getSum2(1,2,3))
print(getSum2(3,5,3,5))



#class and object sample

class Props:
    def __init__(self,name,age,salary):
        self.age=age
        self.name=name
        self.salary=salary
    def printDetails(self):
        print(self.salary)
        print(self.name)
        print(self.age)


objProps=Props("chandan","20","20000")
objProps.printDetails()

#change and remove value of element using object

objProps.age="30"
objProps.printDetails()
del objProps.salary


#inheritance sample

class Parent:
    def getMethod(self):
        print("this is parent")


class Child(Parent):
    def getMethod(self):
        print("This is a child")
        super().getMethod()



