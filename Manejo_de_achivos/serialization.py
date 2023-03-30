import pickle

name_list=["Pedro","Ana","Paco","Maria"]
binary_archive=open("name_list","wb")

pickle.dump(name_list,binary_archive)

binary_archive.close()

archive=open("name_list","rb")

list=pickle.load(archive)
print(list)