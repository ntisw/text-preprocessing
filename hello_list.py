import ast
x = u'["A","B","C"," D"]'
x = ast.literal_eval(x)
print(x)
x = [n.strip() for n in x]
print(x)
print(x[0])