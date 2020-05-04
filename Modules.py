
import  platform
from  methodsAndClasses import  getSum
import  json
import  re
#built in module sample

print(platform.system())

#custom modules
print(getSum(7,9))

#json module sample
#convert json to python dec

jsonString =  '{ "name":"John", "age":30, "city":"New York"}'

pydec=json.loads(jsonString)
print(pydec["name"])

#convert python to json

jpyString=json.dumps(pydec)
print(jpyString)

#regex

str="chandanc"

#check if str starts with c and ends with n

print(re.search("^c.*n$",str))

str2="chan.dan1234#"

#extract number from string

print(re.findall("[0-9,#,.]",str2))