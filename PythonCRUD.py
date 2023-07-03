import pypyodbc
import db_connection as dbconn
from read import Read
from create import Create
from update import Update
from delete import Delete


def main():
    print('available options: C=create, R=Read, U=Update, D=Delete')
    choice = input('Choose your option =')

    if choice == 'C':
        createObj = Create()
        createObj.func_CreateData()
    elif choice == 'R':
        readObj = Read()
        readObj.func_ReadData()
    elif choice == 'U':
        updateObj = Update()
        updateObj.func_UpdateData()
    elif choice == 'D':
        deleteObj = Delete()
        deleteObj.func_DeleteData()
    else:
        print('Wrong choice, does not exist')


# Call the main function
main()
