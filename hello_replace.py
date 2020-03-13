import re

text = "This is a :-) \n(cat/dog)?....but not a dog... ,,,,,,cat.dog"
#result = text.replace(")"," )")
#result = text.replace(".",". ")
#print(result)

result  = re.sub(r'\.(?=.*\.)','',text)
result  = re.sub(r'\,(?=,*\,)','',text)
print (re.sub(r'\.(?=.*\.)', '', '...'))
print (re.sub(r'\.(?=.*\.)', '', '..'))
print (re.sub(r'\.(?=.*\.)', '', '.'))
print (re.sub(r'\.(?=.*\.)', '', '.....'))