import ast
'''#case1
# x = u'["A","B","C"," D"]'
x = '["A","B","C"," D"]'
x = ast.literal_eval(x)
print(x)
x = [n.strip() for n in x]
print(x)
print(x[0])
'''
'''
#case2
a = ['1','1','2']
b = ['2','3','4']
print(a+b)'''
'''
#case3
a = ['1','1','2']
b = ['2','3','4']
a.extend(b)
print(a)
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    print(unique_list)
    # print list
unique(a)
'''
'''
#case4
# function to get unique values 
def unique(list1): 
      
    # insert the list to the set 
    list_set = set(list1) 
    # convert the set to the list 
    unique_list = (list(list_set)) 
    print(unique_list)


a = ['1','1','2']
b = ['2','3','4']
a.extend(b)
print(a)
unique(a)
'''