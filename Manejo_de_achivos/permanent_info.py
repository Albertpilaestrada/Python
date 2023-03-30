import pickle

class person:

    def __init__(self,name,gender,age) -> None:
        self.name=name
        self.gender=gender
        self.age=age
        print("Added new person: ",self.name)

    def __str__(self):
        return "{} {} {}".format(self.name,self.gender,self.age)
    
class person_list:

    persons=[]

    def __init__(self):
        listofpersons=open("PersonsList","ab+")
        listofpersons.seek(0)

        try:
            self.persons=pickle.load(listofpersons)
            print("{} people were loaded".format(len(self.persons)))
        except:
            print("PersonsList is empty")
        finally:
            listofpersons.close()
            del (listofpersons)

    def add_person(self,p):
        self.persons.append(p)
        self.save_persons()

    def show_persons(self):
        for p in self.persons:
            print(p)

    def save_persons(self):
        listofpersons=open("PersonsList","wb")
        pickle.dump(self.persons,listofpersons)
        listofpersons.close()
        del(listofpersons)

    def show_external_info(self):
        print("The data of external archive is:")
        for p in self.persons:
            print(p)

my_list=person_list()
p=person("Sandra","F",29)
my_list.add_person(p)
p=person("Paco","M",32)
my_list.add_person(p)
p=person("Ana","F",31)
my_list.add_person(p)

my_list.show_persons()
my_list.show_external_info()