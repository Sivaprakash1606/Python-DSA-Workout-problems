class Student_marks:
        Name=None
        m1=None
        m2=None
        m3=None
        m4=None
        m5=None

        def total(self):
            total_marks=self.m1+self.m2+self.m3,self.m4,self.m5
            print=(f"{self.Name}:{total_marks}")



student1=Student_marks("Siva",1,2,3,4,5)
student1.total()











