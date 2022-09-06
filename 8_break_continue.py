shopping_list = ["milk", "pasta", "egg", "spam", "bread","rice"]

for item in shopping_list:
    if item=="spam":
        continue
    print("Buy " + item)    #when the conditon expression is matched, then it skipped the remaining block and restart form for loop.


print("*"*80)

  #BREAK CONDITION
shopping_list = ["milk", "pasta", "egg", "spam", "bread","rice"]
item_to_find="spam"
found_at=None

for index in range(len(shopping_list)):
    if shopping_list[index] =="spam":
        found_at =index
        break
if found_at is not None:
 print("Item found at position {} ".format(found_at))
else:
    print("item {} not found".format(item_to_find))