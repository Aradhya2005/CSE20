import re
text = "Pete’s phone number is 831-234-5678\
and Anna’s phone number is 831-901-2345"
p = re.compile(r"\b\d{3}-?\d{3}-?\d{4}")
m = p.search(text)
print ( m.group() )
m2 = p.findall(text)
print(m2)
m3 = p.match(text)
if m3:
    print(m3.group())
else: 
    print("no exact match")
