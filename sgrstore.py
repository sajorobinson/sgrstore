import sys
from lib import DbOperations

def userInterface():

    print("# SGRSTORE 1.0")

    userInterface = True

    while userInterface is True:
        
        userActionChoice = input(
            "> Would you like to ADD, CHECK, SEARCH, LISTALL or EXIT? "
        )

        userActionChoice = userActionChoice.upper()

        if userActionChoice == "ADD":

            DbOperations.recordAdd()

        elif userActionChoice == "CHECK":

            DbOperations.recordCheck()

        elif userActionChoice == "SEARCH":

            DbOperations.recordSearch()

        elif userActionChoice == "LISTALL":

            DbOperations.listAll()

        elif userActionChoice == "EXIT":
            DbOperations.dbConnection.close()
            sys.exit("> Goodbye!")

        else:

            print("> Please provide a valid option. ")

userInterface()
