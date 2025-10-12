import pandas as pd
import os

CSV_File = 'students.csv'

def data():
    if not os.path.exists(CSV_File):
        print(f"{CSV_File} does not exsist in this folder")
        df = pd.DataFrame(columns = ['Roll_No','Name','Branch', 'Year', 'Gender', 'Age', 'Attendance_%','Mid1_Marks', 'Mid2_Marks', 'Quiz_Marks', 'Final_Marks'])
        df.to_csv(CSV_File, index = False)
        return df
    return pd.read_csv(CSV_File)



#clerck Methods
def Add_Student(Students_df):
    print("---------Adding Student--------")
    while True:
        roll_no = input("Enter Student roll no: ")
        if roll_no not in Students_df['Roll_No'].astype(str).values:
            try:
                Student_details = {
                    'Roll_No' : [roll_no],
                    'Name' : [input("Enter Student Name: ")],
                    'Branch' : [input("Enter branch of the student: ")],
                    'Year' : [int(input('Enter Year of the Student: '))],
                    'Gender' : [input('Enter Gender: ')],
                    'Age' : [int(input("Enter age of the Student: "))],
                    'Attendance_%' : [input("Enter Current Attendence if the Student: ")],
                    'Mid1_Marks' : [int(input("Enter Mid1 marks: "))],
                    'Mid2_Marks' : [int(input("Enter mid2 marks: "))],
                    'Quiz_Marks' : [int(input("Enter Quiz marks: "))],
                    'Final_Marks' : [int(input("Enter final marks: "))]
                }
                new_row_df = pd.DataFrame(Student_details)
                new_row_df.to_csv()
                Students_df = pd.concat([Students_df, new_row_df],ignore_index = True)
                Students_df.to_csv(CSV_File, index = False)
                print("Student added Successfully")
                break
            except ValueError:
                print("Invalid Details!!")
                
        else:
            print("student alreary Registered")
            while True:
                print("Want to Exit(y)")
                print("Want to go to main(m)")
                print("Want to add(a)")
                choice = input("Enter option: ")
                if choice == 'y':
                    Exit()
                elif choice == 'm':
                    return
                elif choice == 'a':
                    break
                else:
                    print("Invalid choice!")

    
def Delete_Student(Students_df):
    print("---------Deleting Student---------")
    roll_no = input("Enter Student reg no you want to delete: ")
    if roll_no not in Students_df['Roll_No'].astype(str).values:
        print("Student does not exsist in the Register")
        return False
    else:
        Matching_rows = Students_df['Roll_No'].astype(str).values == roll_no #.values keep indexes with series
        if Matching_rows.any():     #.any used for boolean
            Index = Students_df[Matching_rows].index
            Students_df = Students_df.drop(Index)
            Students_df.to_csv(CSV_File, index = False)
            print("student deleted from file")
            return True

def Exit():
    print("----------Exit---------")
    exit()


def Clerk(Students_df):
    while True:
        try:
            print(""" 1) Add student \n 2) Delete student \n 3) Exit""")
            choice = int(input("Enter option: "))
            if choice == 1:
                Add_Student(Students_df)
                break
            elif choice == 2:
                Success = Delete_Student(Students_df)
                if not Success:
                    print("Deletion Failed")
                break
            elif choice==3:
                Exit()
            else:
                print("Please choose btw 1-3")
        except ValueError:
            print("Invalid Choice")

def Search_Student(Students_df):
    print("---------Finding Student----------")
    while True:
        roll_no = input("Enter Student roll no you want to search: ")
        result = Students_df[Students_df['Roll_No'].astype(str).values == roll_no] # here result is a DataFrame
        if not result.empty: #.empty checks if the dataframe is empty or not
            print("Student Found")
            print(result.iloc[0]) 
            break
        else:
            print("Student is not found")

def Update_Student(Students_df):
    print("----------Update_Student----------")
    roll_no = input("Enter Roll no of the student: ")
    if roll_no not in Students_df['Roll_No'].astype(str).values:
        print("Student not found")
        return
    Index_to_update = Students_df[Students_df['Roll_No'].astype(str) == roll_no].index # we shouldnot use .values like how we before use.that cant keep index but here we want index
    if not Index_to_update.empty:   #.empty to check if the elements is 0 or not
        while True:
            print("1)Update Mid1 marks")
            print("2)Update Mid2 marks")
            print("3)update Quiz marks")
            print("4)Exit")
            try:
                choice = int((input("Enter your choice: ")))
                if choice == 1:
                    print("----------=Updating Mid1 Marks-----------")
                    Marks = int(input("Enter marks you want to update: "))
                    Students_df.loc[Index_to_update, 'Mid1_Marks'] = Marks
                    break
                elif choice == 2:
                    print("-----------Updating Mid2 Marks---------")
                    Marks = int(input("Enter marks you want to update: "))
                    Students_df.loc[Index_to_update, 'Mid2_Marks'] = Marks
                    break
                elif choice == 3:
                    print("----------Updating Quiz Marks---------")
                    Marks = int(input("Enter marks you want to update: "))
                    Students_df.loc[Index_to_update, 'Quiz_Marks'] = Marks
                    break
                elif choice == 4:
                    Exit()
                else:
                    print("Please choose btw (1-4)!")
            except ValueError:
                print("Invalid Choice")
        print("Marks Updated!")
        Students_df.to_csv(CSV_File, index = False)

import pandas as pd

def Filter_Students(Students_df):
    print("------ Sort & Filter ------")
    while True:
        print("1. Sort by Final Marks (High to Low)")
        print("2. Filter by Attendance (Below Threshold)")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            # Sort the DataFrame by 'Final_Marks' in descending order
            sorted_df = Students_df.sort_values(by='Final_Marks', ascending=False)
            print("\nSorted by Final Marks (High to Low):")
            print(sorted_df[['Roll_No', 'Name', 'Final_Marks']].to_string(index = False))
            break
        elif choice == '2':
            try:
                threshold = int(input("Enter attendance threshold (%): "))
            
                # Filter the DataFrame to find students below the threshold
                filtered_df = Students_df[Students_df['Attendance_%'] < threshold]
            
                if not filtered_df.empty:
                    print(f"\nStudents with Attendance less than {threshold}%:")
                    print(filtered_df[['Roll_No', 'Name', 'Attendance_%']].to_string(index = False))
                else:
                    print(f"No students found with attendance less than {threshold}%.")
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            Exit()
            break
        else:
            print("Invalid choice.")


def Teacher(Students_df):
    while True:
        print("1)Search Student")
        print("2)Update Student")
        print("3)Filter Students")
        print("4)Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Search_Student(Students_df)
                break
            elif choice ==2:
                Update_Student(Students_df)
                break
            elif choice == 3:
                Filter_Students(Students_df)
                break
            elif choice == 4:
                Exit()
            else:
                print("Please choose btw (1-4)!")
        except ValueError:
            print("Invalid choice!")
            

def main():
    Students_df = data()
    print("****** Student Management System ******")
    print("select your role")
    print("1) Clerk")
    print("2) Teacher")
    print("3) HOD")
    print("4) Exit")
    while True:
        try:
            role = int(input("Enter your choice: "))
            if role == 1:
                Clerk(Students_df)
                break
            elif role == 2:
                Teacher(Students_df)
                break
            elif role == 3:
                pass
            elif role == 4:
                Exit()
            else:
                print("Please Enter(1-4)")
        except ValueError:
            print("Invalid Choice")

main()