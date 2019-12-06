import re

str="5349 124 8494 8 823"


#1 get  list of nnumbers

lst=re.findall("\d+",str)
print(lst)
lst=re.split("\s+",str)
print(lst)

#2 get list of all 3 digit numbers


lst= re.findall(r"\b\d{3}\b",str)
print(lst)


# 3. remove  single digit from list

lst= re.sub(r"\b\d{1}\b","",str)
print(lst)

#4 search string contain 4 digit followed by 3 digit
lst= re.search("\d{4} \d{3}",str)
print(lst.group())