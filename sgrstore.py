import sys
from lib import DbOperations

def userInterface():

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

userInterface()
