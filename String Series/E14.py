str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print(str_list)
for i in str_list :
    if not i :
        str_list.remove(i)

print(str_list)