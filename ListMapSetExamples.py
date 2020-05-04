#list sample

#create list
a=[1,2,3,4,5]

#add item in list
a.append(12)
#remove item from list
a.remove(1)
#print items in list
for i in a:
    print(i)

#retrieve item from list using index
print(a.__getitem__(1))

#filter list to get items divisible by 2
divlist=[]
for j in a:
    if j%2==0:
        divlist.append(j)
print(divlist)
#filter list like streams in java in a single line
divlist2=[k for k in a if k%2==0]
print(divlist)

#using set to remove duplicates from string

dupstring="chandan"
resultString=""
dupStringToChar=list(dupstring)
print(dupStringToChar)
uniqueChars=set(dupStringToChar)
print(uniqueChars)
for i in uniqueChars:
    resultString=resultString+i

print("result string is "+resultString)

print(divlist)

#hashmap sample

map1={"name":"chandan","age":20}
print(map1["name"])
print(map1["age"])

#add item in map
map1.__setitem__("phone",8285408005)
print(map1["phone"])

#remove item in map
map1.__delitem__("phone")

#print key, values in map

for key,value in map1.items():
    print("key is:"+key+ " and value is:"+str(value))

#print character count in word

word="chandan"
charmap={}
for i in word:
    if(charmap.keys().__contains__(i)):
        charmap.__setitem__(i,charmap[i]+1)
    else:
        charmap.__setitem__(i,1)


print(charmap)


#map with list as values

list1=[1,2,3,4,5]
list2=[1,2,3,4,6]

mapWithList={"marks1":list1,"marks":list2}

print(mapWithList)