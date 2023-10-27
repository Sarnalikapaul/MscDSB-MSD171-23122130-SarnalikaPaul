''''class MSCDSB:
   
   
   
 def __init__(self):
     #DATA MEMBERS/PRPPERTIES/ATTRIBUTES
      self.name="MSCDSB"
      self.students=["A","B","C"]  


def printStudentS(self):#Member Functions
 for student in self.students:
         print(student)

obj =MSCDSB()
print(obj.name)
print(obj.students)'''

class car:
    
    def __init__(self,mfg,mdl,yer):
        self.manufacturer = mfg
        self.model= mdl
        self.year= yer

bmw = car("BMW","F Series",2020)
print(bmw.manufacturer)

ferari = car("ferari","A Series",2023)
print(ferari.model)



