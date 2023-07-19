filenames = ['a.txt','b.txt','c.txt']

for file in filenames:
    with open(file,'r') as f:
        print(f.read())
        
        