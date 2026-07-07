
file = open("C:\\Users\\muham\\OneDrive\Desktop\\Hoja Python Practical\\File Handling\\notes.txt", "r")
for f in file:
    print(f.strip())
file.close()