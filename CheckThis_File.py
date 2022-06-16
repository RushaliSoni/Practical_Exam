'''

1) Read Data From File
with open(input) as f:
    s = f.read()
    print(s)

2) Write With Replace  Data on Output .json File
with open('text.json','r') as f:
    s = f.read()
    s = s.replace("+type", "+size@5+type")
with open('output.json', "w") as f:
        f.write(s)

'''
# Using Function
def find_Replace(find, replace, input, output):
    with open(input) as f:
        s = f.read()
    s = s.replace(find, replace)
    with open(output, "w") as f:
        f.write(s)


find_Replace("+type", "+size@5+type", "test.json", "output.json")