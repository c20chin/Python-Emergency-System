import os, sys, time, datetime, pandas as pd
from admin import Admin
from volunteer import Volunteer
from emergency import Emergency
from createcamp import Create_Camp
from updatecamp import Update_Camp
from message import Message

class Session:
    def __init__(self):
        self.mode = None
        self.username = None
        self.active = None

    def print_logo(self):
        """Print the introduction of the system."""
        print('******************************************************************************')
        print("                    _____                                \n                   | ____|_ __ ___   ___ _ __ __ _ _   _ \n                   |  _| | '_ ` _ \\ / _ \\ '__/ _` | | | |\n                   | |___| | | | | |  __/ | | (_| | |_| |\n                   |_____|_| |_| |_|\\___|_|  \\__, |\\__, |\n                                             |___/ |___/ \n")
        print('******************************************************************************')

    def start(self):
        try:
            while True:
                print('------------------------------------------------------------------------------')
                choice = input(
                    "             Welcome to Emergy, your emergency management system.\n\n                        Please select your action:\n                                  [1] Login\n                             [CTRL+C] "
                    "Quit Program\n\n""(Note: KeyboardInterrupt Ctrl+C will work in terminal.) \n(If you are using IDEs like Pycharm, remember to adjust your settings accordingly.)")
                if choice != '1':
                    print("Invalid choice. Please try again.")
                elif choice == '1':
                    self.verify_user()
                    loading = "\n                     =====█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀=====                     \n                     =====█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█=====                     "
                    bar = "                     ████████████████████████████████████"
                    print(loading)
                    for c in bar:
                        time.sleep(0.02)
                        print(c, end="", flush=True)
                    print("\n\n")
                if self.mode == "admin":
                    self.display_admin_menu()
                elif self.mode == "volunteer":
                    self.display_volunteer_menu()
        except KeyboardInterrupt:
            print("\n# Program Quit #############################################################")
            print("\n############################################################################")

    def verify_user(self):
        if os.path.exists("admin.csv"):
            df1 = pd.read_csv("admin.csv")
            if fileexist:=os.path.exists("volunteers.csv"):
                df2 = pd.read_csv("volunteers.csv")
                df2['login'] = False
                df2.to_csv("volunteers.csv", index=False)
            while True:
                print("\n============================𝖤𝖭𝖳𝖤𝖱 𝖸𝖮𝖴𝖱 𝖫𝖮𝖦𝖨𝖭 𝖣𝖤𝖳𝖠𝖨𝖫𝖲==========================")
                username = input("                            Username: ")
                password = input("                            Password: ")
                if fileexist and len(df1[df1.username == username])>0 or len(df2[df2.username == username])>0:
                    if len(df1[df1.username == username])>0 and str(df1.loc[df1['username'] == username,'password'].values.item()) == password:
                        d2 = df1[df1.username == username]
                        self.mode = d2['status'].values[0]
                        self.username = d2['username'].values[0]
                        return
                    elif len(df2[df2.username == username])>0 and str(df2.loc[df2['username'] == username,'password'].values.item()) == password:
                        d2 = df2[df2.username == username]
                        self.mode = d2['status'].values[0]
                        self.active = d2['active'].values[0]
                        self.username = d2['username'].values[0]
                        Volunteer.edit_info(self.username, "login", True)
                        return
                    else:
                        print('\nInvalid password. Please try again or press 𝗖𝗧𝗥𝗟 + 𝗖 to exit: \n')
                else:
                    print('\nAccount doesn’t exist. Please try again or press 𝗖𝗧𝗥𝗟 + 𝗖 to exit: \n')

    def logout(self):
        if self.mode == "volunteer":
            Volunteer.edit_info(self.username, "login", False)
        self.mode = None
        self.username = None
        self.active = None
        print("\n==============================YOU ARE LOGGED OUT===============================")

    def display_admin_menu(self):
        admin_menu={1:"Create, update or close emergency plan", 2:"Display emergency",
                    3:"Register volunteer", 4:"Deactivate volunteer", 5:"Activate volunteer", 
                    6:"Delete volunteer", 7:"Create/update camps", 8:"Message board", 
                    9:"Log out"}
        while True:
            try:
                print("\n=================█░█ █▀▀ █░░ █░░ █▀█ ░   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█==================\n=================█▀█ ██▄ █▄▄ █▄▄ █▄█ █   █▀█ █▄▀ █░▀░█ █ █░▀█==================")
                print("\n=====================================𝖬𝖤𝖭𝖴=====================================")
                for k,v in admin_menu.items(): print(f"[{str(k)}]",v)  
                Session.check_volunteer_endDate()
                choice = input("Please choose an option: ")
                if choice == '1':
                    self.admin_create_emergency()
                elif choice == '2':
                    if os.path.exists("emergencies.csv"):
                        self.admin_display_emergency()
                    else:
                        print("No records available.")
                elif choice == '3':
                    self.admin_register_volunteer()
                
                elif choice == '4':
                    if os.path.exists("volunteers.csv"):
                        self.admin_deactivate_volunteer()
                    else:
                        print("No volunteers are currently registered.")
                elif choice == '5':
                    self.admin_activate_volunteer()
                elif choice == "6":
                    self.admin_delete_volunteer()
                elif choice == '7':
                    try:
                        print("\n========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ===========================")
                        print("Would you like to:\n"
                              "[1] Create Camp\n"
                              "[2] Update Camp \n")
                        if (enter:=input("Please choose an option: "))=="1":
                            Create_Camp()
                        elif enter=="2":
                            Update_Camp()
                        else:
                            print("Invalid Choice. Back to menu.")
                    except KeyboardInterrupt:
                        print("\n############################################################################")
                elif choice == "8":
                    self.message_board()
                elif choice == '9':
                    confirm = input("Are you sure you want to log out? (Y/N)\n")
                    if confirm.lower() == 'y':
                        self.logout()
                        return
                else:
                    print("Invalid choice. Please try again: \n")
            except KeyboardInterrupt:
                print("\n############################################################################")
                self.logout()
                return
    
    def display_volunteer_menu(self):
        while True:
            try:
                if not self.active:
                    print("Your account has been deactivated. Please contact the administrator.")
                    return
                else:
                    vdf = pd.read_csv("volunteers.csv")
                    campinfo=vdf.loc[vdf['username'] == self.username,'camp'].values[0]
                    endinfo=vdf.loc[vdf['username'] == self.username,'avail_endDate'].values[0]
                    print("\n=======================█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀========================\n=======================▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄========================")
                    print("\n====================================𝖬𝖤𝖭𝖴=====================================")
                    print("[VOLUNTEER INFO] ","Username:",self.username," Camp:",campinfo, " Available Until:",endinfo,"\n")
                    print("[1] Update your information\n"
                          "[2] Add refugees\n"
                          "[3] Update camp details\n"
                          "[4] Message board\n"
                          "[5] Log out\n")
                    choice = input("Please choose an option: ")
                    if choice == '1':
                        self.volunteer_edit_info()
                    elif choice == '2':
                        self.volunteer_create_profile()
                    elif choice == '3':
                        try:
                            print("\n========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ===========================")
                            Update_Camp()
                        except:
                            print("\n############################################################################")
                    elif choice == "4":
                        self.message_board()
                    elif choice == '5':
                        confirm = input("Are you sure you want to log out? (Y/N)\n")
                        if confirm.lower()=='y':
                            self.logout()
                            return
                    else:
                        print("Invalid choice.\n")
            except KeyboardInterrupt:
                print("\n############################################################################")
                self.logout()
                return


#Start of Admin Menu Functions
    @staticmethod
    def check_volunteer_endDate():
        current_Date = datetime.datetime.today()
        df = pd.read_csv("volunteers.csv")
        list_of_endDate = list(set(df['avail_endDate']))
        if len(list_of_endDate) != 0:
            alertmsg=""
            for i in list_of_endDate:
                if datetime.datetime.strptime(i, '%d/%m/%Y') < current_Date:
                    query = df[(df['avail_endDate'] == i) & (df['active'] == True)]
                    for incorrect_status_username in list(set(query['username'])):
                            alertmsg+=f" {incorrect_status_username} "
            if len(alertmsg)!=0:
                print("\033[1;34;50m ALERT:\033[1;0;50m")
                print("\033[1;34;50m Please note that the following volunteers are no longer available. You may wish to confirm/deactivate. \033[1;0;50m")
                print(f"\033[1;34;50m {alertmsg} \033[1;0;50m\n")

        edf = pd.read_csv("emergencies.csv")
        valid_endDate = edf['endDate'].notnull()
        if any(valid_endDate):
            query = edf[(pd.to_datetime(edf['endDate'], format='%d/%m/%Y')<current_Date) & (edf['status'] == "open")]
            if len(query)!=0:
                print("\033[1;34;50m ALERT:\033[1;0;50m")
                print("\033[1;34;50m Please note that the following emergencies' end dates are in the past. You may wish to confirm/deactivate. \033[1;0;50m")
                print(f"\033[1;34;50m {query} \033[1;0;50m\n")

        cdf = pd.read_csv("Camp.csv")
        messages = ""
        for index, row in cdf.iterrows():
            camp = row['camp']
            subset = cdf.iloc[[index]].to_string()
            if "poor" in subset.lower() or "needed" in subset.lower() or "few" in subset.lower() or "none" in subset.lower():
                messages+= f" {camp} "
            
        if len(messages) > 0:
            print("\033[1;34;50m URGENT:\033[1;0;50m")
            print("\033[1;34;50m The following Camps are in need of additional resources. \033[1;0;50m")
            print(f"\033[1;34;50m {messages} \033[1;0;50m\n")

    def admin_create_emergency(self):  # tested
        while True:
            try:
                print("\n========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ===========================")
                print("Please specify what function you would like: \n"
                      "[1] Create emergency\n"
                      "[2] Update or Close emergency\n")
                choice = input("Please choose an option: ")
                if choice == '1':
                    try:
                        print("\n=========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ============================")
                        kind = input("Enter the type of the emergency: ")
                        desc = input("Enter description: ")
                        area = input("Enter the affected area: ")
                        Admin.create_emergency(kind, desc, area)
                    except KeyboardInterrupt:
                        print("\n############################################################################")
                elif choice == '2':
                    try:
                        Emergency.update_emergencyPlan()
                    except KeyboardInterrupt:
                        print("\n############################################################################")
                else:
                    print("Please input a valid number.\n")
            except KeyboardInterrupt:
                print("\n############################################################################")
                return  

    def admin_display_emergency(self):
        while True:
            try:
                print("\n=========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ============================")
                print("Would you like to:\n"
                      "[1] Display all emergencies\n"
                      "[2] Display chosen emergencies\n")
                choice = input("Please choose an option: ")
                if choice == "1":
                    df = pd.read_csv("emergencies.csv")
                    print(df.to_string())
                    self.admin_emergency_sum()
                elif choice == "2":
                    kind = input("Enter a type of the emergency: ").lower()
                    area = input("Enter the affected area: ").lower()
                    df = pd.read_csv("emergencies.csv")
                    res = df[df['kind'].str.contains('.*' + kind + '.*')]
                    results = res[res['area'].str.contains('.*' + area + '.*')]
                    if results.empty:
                        print("No such record found.")
                    else:
                        print(results.to_string())

                else:
                    print("Invalid choice. Please try again\n")
            except KeyboardInterrupt:
                print("\n############################################################################")
                return

    def admin_emergency_sum(self):
        while True:
            try:
                emer_index = int(input("\n>>>>> Enter an emergency index for its specific summary or 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back: "))
                df = pd.read_csv("emergencies.csv")
                df2 = pd.read_csv("Camp.csv")
                df_v = pd.read_csv("volunteers.csv")
                
                if emer_index not in df.index:
                    print("The index you entered is invalid. Please try again.")
                else:
                    summary = [['Camp','Num of Refugees','Num of Volunteers']]
                    data = []
                    df3 = df2.loc[df2['emergency_index'] == emer_index, ['camp']]
                                        
                    
                    for i in df3['camp']:
                        data.append(i)
                        camp_ind = df2[df2["camp"] == i].index[0]
                        data.append(df2.at[camp_ind, "nums"])
                        data.append(len(df_v.loc[df_v['camp'] == i]))
                        summary.append(data)
                        data = []
                    output = pd.DataFrame(summary)
                    print("Here is your summary:\n")
                    print(df.iloc[emer_index])
                    print(output)

            except KeyboardInterrupt:
                print("\n############################################################################")
                return
            except ValueError:
                print('The index you entered is invalid. Please try again.')

    def admin_register_volunteer(self):
        while True:
            try:
                print("\n========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ===========================")
                username = input("Enter username of the new volunteer: ")
                if Volunteer.volunteers.empty or not any(Volunteer.volunteers['username'] == username):
                    print("The username is available. Please continue entering necessary information")
                    password = input("Enter their password: ")
                    first_name = input("First name: ")
                    last_name = input("Last name: ")
                    while True:
                        phone = input("Phone number (Numbers Only): ")
                        if phone.isdigit():
                            break
                        else:
                            print("Incorrect phone number format. Please try again")
                    df1 = pd.read_csv("Camp.csv")
                    while True:
                        camp = input("Camp: ")
                        if (df1['camp'] == camp).any():
                            break
                        else:
                            print("Camp not recognized. Please try again")
                    avail_startDate = "{0:%d/%m/%Y}".format(datetime.datetime.today())
                    while True:
                        try:
                            input_endDate = datetime.datetime.strptime(input("End Date in the form: DD/MM/YYYY "), '%d/%m/%Y')
                            avail_endDate = input_endDate.strftime('%d/%m/%Y')
                            if datetime.datetime.today() > input_endDate:
                                print('End Date is in the past. Please input End Date again.')
                            else:
                                print('\n \033[1m' + 'Volunteer created.' + '\033[0m')
                                Admin.register_volunteer(username, password, first_name, last_name, phone, camp,
                                                         avail_startDate, avail_endDate)
                                break
                        except:
                            print("Input Date is in the wrong format. Please input End Date again:")
                else:
                    print('The username already exists')
            except KeyboardInterrupt:
                print("\n############################################################################")
                return

    def admin_deactivate_volunteer(self):
        while True:
            try:
                print("\n=========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ============================")
                user = input("Enter the username of the volunteer: ")
                if Admin.deactivate_volunteer(user): #This is one of the few function examples that is properly constructed and called
                    print("Account was deactivated.")
                else:
                    print("User not found. Please try again.\n")
            except KeyboardInterrupt:
                print("\n############################################################################")
                return

    def admin_activate_volunteer(self):
        while True:
            try:
                print("\n=========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ============================")
                user = input("Enter the username of the volunteer: ")
                if Admin.activate_volunteer(user):
                    print("Account was activated.")
                else:
                    print("User not found. Please try again\n")
            except KeyboardInterrupt:
                print("\n############################################################################")
                return
    
    def admin_delete_volunteer(self):
        while True:
            try:
                print("\n=========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ============================")
                vol_username = input("Enter the username of volunteer:")
                df = pd.read_csv("volunteers.csv")
                user_query = df[df.username == vol_username]
                if user_query.empty:
                    print("No such volunteers found.")
                else:
                    res = df[df.username != vol_username]
                    res.to_csv("volunteers.csv",index=False)
                    print(f"{vol_username} is deleted successfully")
            except KeyboardInterrupt:
                print("\n############################################################################")
                return

    def message_board(self):
        while True:
            try:
                print("\n========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ===========================")
                df = Message.messages
                if df.empty:
                    print("No messages.")
                else:
                    # Get public messages from the last week
                    today = datetime.datetime.today()
                    week_ago = today - datetime.timedelta(days=7)
                    new_messages = df[(pd.to_datetime(df['time'], format='%d/%m/%Y %H:%M')>week_ago) & (df['private'] == False)]
                    if new_messages.empty:
                        print("There are no new messages.")
                    else:
                        for index, row in new_messages.iterrows():
                            author = row["author"]
                            time = row["time"]
                            text = row["text"]
                            print(f"{author} ({time}): {text}")

                choice = input("[1] Leave a public board message\n[2] See your private messages\n[3] Send a private message\n") 
                try:
                    if choice == "1":
                        new_mess = input("Enter the message: ")
                        Message(self.username, new_mess)
                    elif choice == "2":
                        private = df[(df['to'] == self.username) & (df['private'] == True)]
                        if private.empty:
                            print("You have no messages.")
                        else:
                            for index, row in private.iterrows():
                                author = row["author"]
                                time = row["time"]
                                subject = row['subject']
                                text = row["text"]
                                print(f"From: {author}\nOn: {time}\nSubject line: {subject}\n{text}")
                                print()
                    elif choice == "3":
                        if not os.path.exists("volunteers.csv"): #Needed?
                            print("No volunteers are currently registered.")
                        else:
                            receiver = input("Username of the addressee: ")
                            # checking if receiver exists in volunteers.csv
                            vdf = pd.read_csv("volunteers.csv")
                            adf = pd.read_csv("admin.csv")
                            if receiver not in vdf['username'].values and receiver not in adf['username'].values:
                                print("No such person in the contact book.")
                            else:
                                subject = input("Subject line: ")
                                text = input("Message: ")
                                Message(self.username, text, to=receiver, subject=subject, private=True)
                    else:
                        print("Invalid choice.")
                except KeyboardInterrupt:
                    print("\n############################################################################")
            except KeyboardInterrupt:
                print("\n############################################################################")
                return
#End of Admin Menu Functions


#Start of Volunteer Menu Functions
    def volunteer_edit_info(self):
            while True:
                try:
                    print("\n=========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ============================")
                    user = self.username
                    df = pd.read_csv("volunteers.csv")
                    vol_list={1:"First name", 2:"Last name", 3:"Password", 4:"Phone number", 5:"Availability(Start Date)", 6:"Availability (End date)"}
                    print("Please specify what information you would like to edit:")
                    for k,v in vol_list.items(): print(f"[{str(k)}]",v)  
                    choice =input("\nEnter the number of your choice: ")
                    if choice == '1':
                        column = 'firstname'
                    elif choice == '2':
                        column = 'lastname'
                    elif choice == '3':
                        column = 'password'
                    elif choice == '4':
                        column = 'phone'
                    elif choice == "5":
                        column = 'avail_startDate'
                        period = "start"
                    elif choice == "6":
                        column = 'avail_endDate'
                        period = "end"
                    else:
                        print("Invalid choice.\n")
                        continue
                    if choice != '5' and choice != '6':
                        new = input("Please type the updated information: ")
                        Volunteer.edit_info(user, column, new)  # warning here
                        print("Your information has been updated.")
                    else:
                        while True:
                            input_date = input("Please type the updated date in the form: DD/MM/YYYY ")
                            try:
                                if Volunteer.date_is_valid(user, period, input_date):
                                    print("is valid")
                                    new = datetime.datetime.strptime(input_date, '%d/%m/%Y').strftime('%d/%m/%Y')
                                    Volunteer.edit_info(user, column, new)  # warning here
                                    print("Your information has been updated.")
                                    break
                                else:
                                    if choice == '5':
                                        print("The start date you have input is after end date. Please retry.")
                                    elif choice == "6":
                                        print("The end date you have input is before the start date. Please retry.")
                            except:
                                print("Input Date is in the wrong format.Please input again:")
                except KeyboardInterrupt:
                    print("\n############################################################################")
                    return

    def volunteer_create_profile(self):
        while True:
            try:
                print("\n========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ===========================")
                print("Please enter the refugee details:\n")
                firstName = input("First name of the refugee family leader: ")
                lastName = input("Last name of the family leader: ")
                data = pd.read_csv("volunteers.csv")
                camp = data.loc[data['username'] == self.username, 'camp'].values[0]
                print("Camp:", camp)
                condition = input("Please outline any health concerns: ")
                try:
                    dependants = int(input("Number of dependants, excluding the family leader: "))
                    data2 = pd.read_csv("Camp.csv")
                    num = data2.loc[data2['camp'] == camp, 'nums'].values[0]
                    data2.loc[data2['camp'] == camp, 'nums'] = num + dependants+1
                    print("New numbers at camp:", camp, ":", num + dependants+1)
                    data2.to_csv('Camp.csv', index=False)
                    Volunteer.create_profile(firstName, lastName, camp, condition, dependants)
                    ans = input("Your new record has been created. Do you want to view the refugee table? (Y/N)")
                    if ans.lower() == "y":
                        refugees = pd.read_csv("refugees.csv")
                        print(refugees)
                except ValueError:
                    print("Invalid data. Please try again\n")
            except KeyboardInterrupt:
                print("\n############################################################################")
                return
#End of Volunteer Menu Functions