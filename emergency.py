import pandas as pd
import os
import datetime


class Emergency:
    if os.path.exists("emergencies.csv"):
        emergencies = pd.read_csv("emergencies.csv")
    else:
        emergencies = pd.DataFrame()

    def __init__(self, kind, desc, area):
        self.kind = kind.lower()
        self.description = desc.lower()
        self.area = area.lower()
        self.startDate = "{0:%d/%m/%Y}".format(datetime.date.today())
        self.endDate = ""
        self.status = "Open"

        emergencyPlan = {
            'kind': self.kind,
            'description': self.description,
            'area': self.area,
            'startDate': self.startDate,
            'endDate': self.endDate,
            'status': self.status
        }
        df = pd.DataFrame([emergencyPlan])
        Emergency.emergencies = pd.concat([Emergency.emergencies, df], ignore_index=True)
        Emergency.emergencies.to_csv("emergencies.csv", index=False)
        print("Record created.\n")
        print(df)

    @staticmethod
    def update_emergencyPlan():
        emergencies = pd.read_csv("emergencies.csv")
        pd.set_option('display.max_rows', None) #As we need to choose index based on display, for now remove row limit
        while True:
            print("\n========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ===========================")
            print(emergencies)
            try:
                update_index = input("\nPlease choose the correct index corresponding to the emergency: ")
                if not update_index.isdigit():
                    print("Invalid index. Please input a correct index again.")
                    continue
                else:
                    update_index = int(update_index)
                if update_index not in emergencies.index:
                    print("Invalid index. Please input a correct index again: \n")
                    continue
                else:
                    E={"1":"kind", "2":"description","3":"area", "4":"startDate", "5":"endDate", "6":"status"}
                    while True:
                        print("Please specify what information you would like to edit:")
                        print("If you wish to close an emergency, just change the status to 'closed'.")
                        for i in E:
                            print('['+i+']',E[i])
                        choice = input("Please choose an option: ")
                        if choice in E:
                            info=E[choice]
                            break
                        else:
                            print("Invalid choice. Please try again:\n")
                            print("Please input an index again: \n")

                    if choice != "4" and choice != "5" and choice != "6":
                        new = input("Please enter update to: {} : ".format(info)).lower()
                        emergencies.iloc[update_index, emergencies.columns.get_loc(info)] = new
                        emergencies.to_csv("emergencies.csv", index=False)
                        print(emergencies)
                    elif choice == "4":
                        while True:
                            input_date = input("Please type the updated start Date in the form: DD/MM/YYYY: ")
                            try:
                                new = datetime.datetime.strptime(input_date, '%d/%m/%Y').strftime('%d/%m/%Y')
                                emergencies.iloc[update_index, emergencies.columns.get_loc(info)] = new
                                emergencies.to_csv("emergencies.csv", index=False)
                                print(emergencies)
                                break
                            except:
                                print("Your input Date is in the wrong format. Please input again:")
                    elif choice == "5":
                        start_date = emergencies.iloc[update_index, emergencies.columns.get_loc('startDate')]
                        formatted_start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y')
                        while True:
                            input_date = input("Please type the updated end date in the form: DD/MM/YYYY: ")
                            try:
                                new_enddate = datetime.datetime.strptime(input_date, '%d/%m/%Y')
                                if formatted_start_date <= new_enddate:
                                    str_new_enddate = new_enddate.strftime('%d/%m/%Y')
                                    emergencies.iloc[update_index, emergencies.columns.get_loc(info)] = str_new_enddate
                                    emergencies.to_csv("emergencies.csv", index=False)
                                    print(emergencies)
                                    break
                                else:
                                    print("The end Date should be greater than the start Date. Please input again: ")
                            except:
                                print("Your input Date is in the wrong format. Please input again: ")
                    elif choice == "6":
                        while True:
                            new = input("Please enter the status (open/closed)")
                            if new!= "open" and new!="closed":
                                print("Invalid Input. Please type 'open' or 'closed'")
                            else:
                                emergencies.iloc[update_index, emergencies.columns.get_loc(info)] = new
                                emergencies.to_csv("emergencies.csv", index=False)
                                break

            except KeyboardInterrupt:
                print("\n############################################################################")
                return

    @staticmethod
    def display_emergencyPlan():
        pd.set_option('display.max_rows', None)
        emergencies = pd.read_csv("emergencies.csv")
        print(emergencies)
