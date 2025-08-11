txt = "hello, and welcome to our course."
a = txt.capitalize()
print(a) 

txt = "I am from India and born in Maharashtra, India"
b = txt.count('India')
print(b) 

txt = "I am from India and born in Maharashtra, India"
b = txt.find('India')
print(b) 

txt = "I am from India and born in Maharashtra, India"
b = txt.split()
print(b) 

txt = 'Maharashtra123'
b = txt.isalnum()
print(b)

txt = 'Maharashtra123'
b = txt.isalpha()
print(b)

txt = '505909'
b = txt.isdigit()
print(b)

txt = ['and', 'born', 'in', 'Maharashtra']
b = ' # '.join(txt)
print(b)

txt = 'and born in Maharashtra'
b = txt.replace("born" , "live")
print(b) 

txt = 'and, born in Maharashtra'
b = txt.startswith('and')
c = txt.endswith('Maharashtra')
print(b,c)    

# thank you