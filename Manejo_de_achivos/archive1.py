from io import *

archive_text=open("archive.txt","w")
frase="Great day to program in python"
archive_text.write(frase)
archive_text.close()

archive_text=open("archive.txt","r")
text=archive_text.read()
archive_text.close()

print(text)

archive_text=open("archive.txt","a")
archive_text.write("\nIt is always a good occasion to program in python")
archive_text.close()

archive_text=open("archive.txt","r")
text=archive_text.read()
archive_text.close()

print(text)

archive_text.seek(len(archive_text.read())/2)
print(archive_text.read())

