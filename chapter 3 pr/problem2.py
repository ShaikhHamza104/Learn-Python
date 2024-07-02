# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>'''
latter='''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name="Hamza"
date="09-05-2024"
print(latter.replace("<|Name|>",name).replace("<|Date|>",date))