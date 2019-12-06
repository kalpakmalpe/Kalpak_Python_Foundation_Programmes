import re
str="Welcome 32 to 56 python 32"
pattern="[a-zA-Z]+"

# 1.findall
lst=re.findall(pattern,str)
print(lst)

#2 split
lst=re.split("\d+",str)
print(lst)

lst=re.split("\s+",str,2)
print(lst)


# 3. sub
s=re.sub("\s","$",str)
print(s)

# 4. nsub
s=re.subn("\d","",str)
print(s)

# 5.search

m=re.search("(\d+) (\w+)",str)

if (m):
    print("Match Found...")
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
    print(m.re)
    print(m.string)

else:
    print("Match Not Found..!")