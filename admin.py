import pandas as pd
import os
from volunteer import Volunteer
from emergency import Emergency
import datetime


class Admin:
    if os.path.exists("admin.csv"):
        admins = pd.read_csv("admin.csv")
    else:
        admins = pd.DataFrame()

    def __init__(self, login, password):
        self.username = login
        self.password = password
        self.status = "admin"

        admin = {"username": self.username, "password": self.password, "status": self.status}
        df = pd.DataFrame([admin])
        Admin.admins = pd.concat([Admin.admins, df], ignore_index=True)
        # save df to csv file
        Admin.admins.to_csv('admin.csv', index=False)

    @staticmethod
    def register_volunteer(username, password, firstName, lastName, phone, camp, avail_startDate, avail_endDate):
        return Volunteer(username, password, firstName, lastName, phone, camp, avail_startDate, avail_endDate)

    @staticmethod
    def deactivate_volunteer(username):  # tested
        df = pd.read_csv("volunteers.csv")
        if username in df.username.values:
            df.loc[df.username == username, 'active'] = False
            df.to_csv("volunteers.csv", index=False)
            return True
        else:
            return False  


    @staticmethod
    def activate_volunteer(username):  # tested
        df = pd.read_csv("volunteers.csv")
        if username in df.username.values:
            obtained = df.loc[df.username == username, 'active']
            if obtained.item() == False:

                while True:
                    if Admin.update_renew_enddate(username, df):
                        break
                return True
      
                            
        else:
            return False

    @staticmethod
    def update_renew_enddate(username,df):
        start_date = df.loc[df.username == username, 'avail_startDate'].values[0]
        formatted_start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
        while True:
            input_date = input('Enter a new end date (mm/dd/yyyy): ')
            try:
                new_Enddate = datetime.datetime.strptime(input_date, '%d/%m/%Y')
                if formatted_start_date < new_Enddate:
                    new_Enddate = new_Enddate.strftime("%d/%m/%Y")
                    df.loc[df.username == username, 'avail_endDate'] = new_Enddate
                    df.loc[df.username == username, 'active'] = True
                    df.to_csv("volunteers.csv", index=False)
                    print(f"Update is completed : {new_Enddate}")
                    break
                else:
                    print("The end Date should be greater than the start Date. Please input again: ")
            except Exception:
                print('Your input Date is in the wrong format. Please input again: ')
        return True

    @staticmethod
    def create_emergency(kind, desc, area):
        return Emergency(kind.lower(), desc.lower(), area.lower())

    @staticmethod
    def close_emergency(index, date):
        df = pd.read_csv("emergencies.csv")
        df.loc[index, "endDate"] = date
        df.loc[index, "active"] = False
        df.to_csv("emergencies.csv", index=False)
