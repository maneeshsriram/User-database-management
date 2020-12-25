import sqlite3 as sql


class DatabaseManage(object):

    def __init__(self):
        global connect
        try:
            connect = sql.connect("users.db")
            with connect:
                cursor = connect.cursor()
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS user(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Age INTEGER)"
                )
        except Exception:
            print("Unable to create database")

    def insert_data(self, data):
        try:
            with connect:
                cursor = connect.cursor()
                cursor.execute(
                    "INSERT INTO user(Name, Age) VALUES (?,?)", data
                )
                return True
        except Exception:
            print("Unable to insert into database")

    def display_data(self):
        try:
            with connect:
                cursor = connect.cursor()
                cursor.execute(
                    "SELECT * FROM user"
                )
                return cursor.fetchall()
        except Exception:
            print("Unable to display the data")

    def delete_data(self, ID):
        try:
            with connect:
                cursor = connect.cursor()
                cursor.execute(
                    "DELETE FROM user WHERE ID = ? ", [ID]
                )
                return True
        except Exception:
            print("Unable to delete")


def main():
    print("\n")
    print("#"*40)
    print("\n ::\t COURSE MANAGEMENT \t:: \n")
    print("#"*40)
    print("\n")

    db = DatabaseManage()

    while True:
        print('\n\nPress 1. Insert info')
        print('Press 2. Show info')
        print('Press 3. Delete info (NEED ID OF COURSE)')
        print('Press 4. Exit\n')

        choice = int(input("Enter Choice : "))

        if choice == 1:
            name = input("\n\tEnter name : ")
            age = input("\tEnter Age : ")
            if db.insert_data([name, age]):
                print("\nSuccessfully inserted\n")
            else:
                print("\nFailed to insert\n")

        elif choice == 2:
            for item in db.display_data():
                print("\n\tID is : ", item[0])
                print("\tName is : ", item[1])
                print("\tAge is : ", item[2])

        elif choice == 3:
            user_id = (input("\n\tEnter the ID : "))
            if(db.delete_data(user_id)):
                print("\nSuccessfully deleted")
            else:
                print("\nFailed to delete")

        else:
            print("\nThanks for your time !\n")
            break


if __name__ == "__main__":
    main()
