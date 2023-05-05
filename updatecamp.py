import pandas as pd
class Update_Camp:
    def __init__(self):
        df = pd.read_csv('Camp.csv')
        while True:
            print("\n========================== 𝗣𝗿𝗲𝘀𝘀 𝗖𝗧𝗥𝗟 + 𝗖 𝘁𝗼 Go Back ===========================")
            print("\nHere are the EXISTING CAMPS: \n")
            print(df)
            choice = input("\nWould you like to:\n\n[1] Edit details?\n[Q] Go back\n")
    #edit data
            if choice == '1':
                row=input("Type in the index of the row you want to edit: ")
                print()
                if not row.isdigit() or int(row) not in df.index:
                    print("Input Not Valid. Please try again.")
                    continue
                row=int(row)
                print(df.loc[row],"\n")
                while True:
                    field=input("Which of these would you like to edit? \n")
                    if field not in df.loc[row].index:
                        print("Invalid Field. Try Again.")
                    else:
                        break
                if field=='nums' or field=="emergency_index":
                    while True:
                        new_val=input("Type in the new value:")
                        if new_val.isdigit():
                            break
                        else:
                            print("Please only input numbers.Try agin.")
                else:
                    new_val=input("Type in the new value:")
                df.loc[row, field]=new_val
                df.to_csv('Camp.csv',index=False)
                print("\nUPDATED CAMPS: \n")
                print(df)
        
            elif choice.lower() == 'q':
                print('---------------------------------------')
                check = input("Are you sure to go back?\n [Y] Yes, please go back. [N] No, continue.\n")
                if check == "Y" or check == "y":
                    return
                if check != "Y" and check != "y":
                    pass
            else:
                df.to_csv('Camp.csv', index=False)
                print("Input Not Valid. Please try again.")
