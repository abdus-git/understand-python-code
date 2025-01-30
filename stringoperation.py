#Concatenation
str1="Hello"
str2="World"
result=str1+" "+str2
r= str1+str2
print(result)
print(r)

#Repetition
print(str1*3)
print(str2*3)

#Membership
text ="Python is awesome"
print("Python" in text)
print("Java"not in text)
print(text.lower())

test ="python is amazing"
print(test.upper())
print(test.strip())
print(text.strip())

joinedstr =" ".join(text)
print(joinedstr)
replacestr = test.replace("python", "java")
print(replacestr)
print(text.find("python"))
print(text.startswith("python"))
print(text.endswith("python"))

str3="Abdus"
str4="sami"
n=str3+str4
print(n)

print(n[0])
print(n[3])
print(n[6])
print(n[8])