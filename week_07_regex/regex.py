
#Mr. Z - I am sorry I was only able to read some of the Medium article
#a(b|c) matches a string that has a followed by b or c (and captures b or c)
#.matches any character
# ^The matches any string that starts with The
# end$ matches a string that ends with end
# ^The end$ exact string match (starts and ends with The end)
#roar matches any string that has the text roar in it

import re


def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    result = re.findall(pattern,line)

    pattern = r"(^The)(October|Oct|November|Nov)( \d{1,2}, \d{4})"
    result = result + re.findall(pattern,line)
    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)