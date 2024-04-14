class Mentor_New2:
    
    number_of_mentor = 0
    
    def __init__(self,name,number,adhar):
        self.name= name
        # self.number = number
        self.__number = number # this make it private 
        self.__adhar = adhar
        self.company = "ineuron"
        
        Mentor_New.number_of_mentor = Mentor_New.number_of_mentor + 1
         
    def __str__(self):
        print(self.name)
        print(self.__number)
        return ""
    
    def get_mobile(self):   #getter
        print(self.__number)
        return self.__number

    def get_adhar(self):   #getter
        print("**********" + self.__adhar[-1])
    
    def set_mobile(self,newNumber,password):   #setter
        if(password == "0123"):
            self.__number = newNumber  
    
    def set_adhar(self,newAdhar):   #setter
        if(type(newAdhar) == str):
            self.__adhar = newAdhar  
        else:
            print (" please provide a string adhar")
            
            
    def __getAadharforUN(self):
        return "IND" + self.__adhar

    def __processSalary(self):
        self.__processSalaryToAccount