class Associate:
    def __init__(self,id,name,technology,experience):
        self.id=id
        self.name=name
        self.technology=technology
        self.experience=experience
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_technology(self):
        return self.technology
    def get_experience(self):
        return self.experience

class Solution:
    @staticmethod
    def associatesForGivenTechnology(Associate,searchTechnology):
        filtered=[]
        for associate in Associate:
            if associate.get_technology().lower()==searchTechnology.lower() and associate.get_experience()%5==0:
                filtered.append(associate)
        return filtered


if __name__ =="__main__":
    associates=[]
    for i in range(2):
        id=int(input(f"Enter id {i+1}: "))
        name=input(f"Enter name {i+1}: ")
        technology=input(f"Enter technology {i+1}: ")
        experience=int(input(f"Enter your experience {i+1}: "))
        associates.append(Associate(id,name,technology,experience))

    searchTechnology=input(f"Enter search technology: ")
    filtered_associates=Solution.associatesForGivenTechnology(associates,searchTechnology)
    print("\nFiltered associates IDs: ")
    for associate in filtered_associates:
        print(associate.get_id())





