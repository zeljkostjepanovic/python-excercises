filenames = ['doc.txt','report.txt','presentation.txt']

for file in filenames:
    with open(file,'w') as fw:
        fw.write("Hello")
