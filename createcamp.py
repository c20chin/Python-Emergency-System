import pandas as pd
from emergency import Emergency
class Create_Camp:
    def __init__(self):
        tonext = True
        #start a new camp
        if input("\nIs this the first camp? (Y/N)").lower() == "y" and input("\nThis will wipe any existing camp records! Are you sure? (Y/N)").lower()== "y":
            df=None
              
        else:
            df = pd.read_csv('Camp.csv')
            print("\nHere are the EXISTING CAMPS: \n")
            print(df)
            Create_Camp.rtot(df)
        
        while True:
            self.camp = input("\nNew Camp name? ")
            if any(df['camp'] == self.camp):
                print("This camp name already exists. Please retry.")
            else:
                break
        
        while True:
            print(Emergency.emergencies)
            self.emergency_index=input("Please input the corresponding index of the emergency to associate this new camp with:")
            if not self.emergency_index.isdigit() or int(self.emergency_index)>len(Emergency.emergencies):
                print("Invalid Index. Try again.")
            else:
                break
        
        self.loc = input("Location? ")
        self.nums = 0
        self.food = input("Food/water? ")
        self.shelter = input("Shelters? ")
        self.blankets = input("Blankets? ")
        self.comms = input("Communications? ")
        self.access = input("Access? ")
        self.toilets = input("Toilet facilities? ")
   
        newCamp={
            'camp':[self.camp],
            'loc': [self.loc],
            'nums': [self.nums],
            'food': [self.food],
            'shelter': [self.shelter],
            'blankets': [self.blankets],
            'comms': [self.comms],
            'access': [self.access],
            'toilets': [self.toilets],
            'emergency_index':[self.emergency_index]
        }
        dfNewCamp = pd.DataFrame(newCamp)
        dfNewCamp.to_csv('NewCamp.csv', index=False)
        df = pd.concat([df, dfNewCamp])
        df.to_csv('Camp.csv',index=False)
        print("\nUpdated CAMPS: \n")
        print(df)
        df = pd.read_csv('Camp.csv')
        Create_Camp.rtot(df)
        
        while tonext:
            choice = input("\nWould you like to:\n\n[1] Edit details?\n [Q] Go back\n")
            #edit data
            if choice == '1':
                row=int(input("Type in the index of the row you want to edit: "))
                print()
                print(df.loc[row],"\n")
                field=input("Which of these would you like to edit? \n")
                new_val=input("Please type in the new value: ")
                df.loc[row, field]=new_val
                df.to_csv('Camp.csv',index=False)
                print("\nUPDATED CAMPS: \n")
                print(df)
                df = pd.read_csv('Camp.csv')
                Create_Camp.rtot(df)  
            elif choice.lower() == 'q':
                print('---------------------------------------')
                check = input("Are you sure to go back?\n [Y] Yes, please go back. [N] No, continue.\n")
                if check == "Y" or check == "y":
                    tonext=False
                if check != "Y" and check != "y":
                    pass
            else:
                df.to_csv('Camp.csv', index=False)
                tonext = True
    def rtot(df):
        #print()
        ref_count=0
        len_df=len(df.index)
        for row in range (0,len_df):
            ref_count=ref_count+int(df.loc[row, 'nums'])
        #print("Total refugees =",ref_count)
        print("\033[1;32;50m+"+"-"*56+"+")
        print("|\t\t\t\t\t\t\t |")
        print("|  \033[1;0;50m Total refugees:\033[1;31;50m",ref_count,"\033[1;32;50m "*(35-len(str(ref_count))),"|")
        print("\033[1;32;50m|\t\t\t\t\t\t\t |")
        print("+"+"-"*56+"+\033[1;0;50m")