def even(my_list):
    list2=[]
    for x in my_list:
        if x%2==0:
            list2.append(x)
    return list2

def odd(mylist):
    list1=[]
    for x in mylist:
        if x%3==0:
            list1.append(x)
    return list1
