from tokenize import Name

my_list =[1,2,3,"Hello", 4.5, 1, 3]#ordered and mutuable
print(my_list)
my_tuple = (1,2,3,"Hello", 4.5, 1, 3) #ordered and immutable
print(my_tuple)
my_set= {1,2,3,4} #ordered and mutable
print(my_set)
my_dict ={ "name": "Sona","age":25} #unordered and mutable
print(my_dict)

str="An apple in a day keeps a doctor away"
print(str)
print(str.count("p"))
print((str.startswith("p")))
print(str.endswith("y"))

#Extracting initials from string
def get_initials(Full_Name):
    names=Full_Name.split(" ")
    initials="".join([name[0].upper() for name in names])
    return initials
name ="Oggy Thakur"
initials =get_initials(name)
print(initials)




