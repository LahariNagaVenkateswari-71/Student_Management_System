import pandas as pd
import os
CSV_File = 'students.csv'

def data():
    if not os.path.exists(CSV_File):
        print(f"{CSV_File} does not exsist in this folder")
        df = pd.DataFrame(columns = ['Roll_NO','Name','Branch', 'Year', 'Gender', 'Age', 'Attendance_%','Mid1_Marks', 'Mid2_Marks', 'Quiz_Marks', 'Final_Marks'])
        df.to_csv(CSV_File, index = False)
        return df
    return pd.read_csv(CSV_File)



#clerck Methods
def Add_Student(Students_df):
    print("---------Adding Student--------")
    roll_no = input("Enter Student roll no: ")
    if roll_no not in Students_df['Roll_No'].astype(str).values:
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
            'Quiz_Marks' : [int(input("Enter Quiz marks"))],
            'Final_Marks' : [int(input("Enter final marks"))]
        }
        new_row_df = pd.DataFrame(Student_details)
        new_row_df.to_csv()
        Students_df = pd.concat([Students_df, new_row_df],ignore_index = True)
        Students_df.to_csv(CSV_File, index = False)
        print("Student add to file")
    else:
        print("Error Same student alreary in this File")
        return
    
def Delete_Student(Students_df):
    print("---------Deleting Student---------")
    roll_no = input("Enter Student reg no you want to delete: ")
    if roll_no not in Students_df['Roll_No'].astype(str).values:
        print("Student does not exsist in the Register")
        return
    else:
        Matching_rows = Students_df['Roll_No'].astype(str).values == roll_no
        if Matching_rows.any():
            Index = Students_df[Matching_rows].index
            Students_df = Students_df.drop(Index)
            Students_df.to_csv(CSV_File, index = False)
            print("student deleted from file")

def Exit():
    print("----------Exit---------")
    exit()


def Clerk(Students_df):
    while True:
        print(""" 1) Add student \n 2) Delete student \n 3) Exit""")
        choice = int(input("Enter option"))
        if choice == 1:
            Add_Student(Students_df)
            break
        elif choice == 2:
            Delete_Student(Students_df)
            break
        elif choice==3:
            Exit()
        else:
            print("Invalid Choice")




Students_df = data()
print("****** Student Management System ******")
print("select your role")
print("1) Clerk")
print("2) Teacher")
print("3) HOD")
print("4) Exit")
while True:
    role = int(input("Enter your choice: "))
    if role == 1:
        Clerk(Students_df)
        break
    elif role == 2:
        pass
    elif role == 3:
        pass
    elif role == 4:
        pass
    else:
        print("Please Enter valid choice")