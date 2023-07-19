with open("files/data.txt", "a+") as datarw:
    datarw.seek(0)
    content = datarw.read()
    datarw.write(content*2)
