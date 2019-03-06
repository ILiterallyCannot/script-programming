shoppingList = []
i = 0
while 1:
    i+=1
    item = raw_input("Enter item %d to the list: " %i)
    if item=='print':
        break
    if item=='remove':
        item = raw_input("Enter the item you want to delete: ")
        shoppingList.remove(item)
    else:
        shoppingList.append(item)
print "That's your Shopping List"
for p in shoppingList:
    print p
