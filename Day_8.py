# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
Mylist=[]

for line in sys.stdin:
    Mylist.append(line)

n = int(Mylist[0])
entries = Mylist[1:n+1]
queries = Mylist[n+1:]
PhoneBook = {}
for entry in entries:
    name, id = entry.split()  #This will split the name and id 
    PhoneBook[name] = id  #Assigning key to value.

for query in queries:
    new_query = query.rstrip() #This will remove the newline character while input
    if new_query in PhoneBook:
        print(new_query + "=" + str(PhoneBook[new_query]))
    else:
        print("Not found")
