import sqlite3, sys


class DatabaseConnection:

    dbConnection = sqlite3.connect(r"C:\\Users\\samjo\\documents\\sqlite\\SgrStore.db")

    dbCursor = dbConnection.cursor()


class ItemTableColumns:

    columns = [
        "ITEM",
        "ROW",
        "BIN",
        "DESCRIPTION",
        "CREATE DATE",
        "CREATE USER",
        "UPDATE DATE",
        "UPDATE USER",
        "STATUS",
    ]


def resultsParse():

    results = DatabaseConnection.dbCursor.fetchall()

    if results != []:

        print(ItemTableColumns.columns)

        for item in results:
            print(item)

    elif results == []:

        print("No results found!")

    else:

        print("No results found!")


def userInterface():

    userInterface = True

    while userInterface is True:

        userActionChoice = input(
            "> Would you like to ADD, CHECK, SEARCH, LISTALL or EXIT? "
        )

        if (
            userActionChoice == "add"
            or userActionChoice == "Add"
            or userActionChoice == "ADD"
        ):

            recordAdd()

        elif (
            userActionChoice == "check"
            or userActionChoice == "Check"
            or userActionChoice == "CHECK"
        ):

            recordCheck()

        elif (
            userActionChoice == "search"
            or userActionChoice == "Search"
            or userActionChoice == "SEARCH"
        ):

            recordSearch()

        elif (
            userActionChoice == "listall"
            or userActionChoice == "listAll"
            or userActionChoice == "ListAll"
            or userActionChoice == "Listall"
            or userActionChoice == "LISTALL"
        ):

            listAll()

        elif (
            userActionChoice == "exit"
            or userActionChoice == "Exit"
            or userActionChoice == "EXIT"
        ):
            DatabaseConnection.dbConnection.close()
            sys.exit("> Goodbye!")


def recordAdd():

    userAddQuery = input("> Would you like to add a ROW, BIN, or ITEM? ")

    if userAddQuery == "row" or userAddQuery == "Row" or userAddQuery == "ROW":

        rowName = str(input("> Insert a row name: "))

        DatabaseConnection.dbConnection.execute(
            "INSERT INTO row (Description) VALUES (?)", (rowName,)
        )

        try:

            DatabaseConnection.dbConnection.commit()

        except:

            print("ERROR: Failed to add row record. ")

    elif userAddQuery == "bin" or userAddQuery == "Bin" or userAddQuery == "BIN":

        binName = str(input("> Insert a bin name: "))

        rowName = str(input("> Insert a row number: "))

        DatabaseConnection.dbConnection.execute(
            "INSERT INTO bin (RowId, Description) VALUES (?,?)", (rowName, binName)
        )

        try:

            DatabaseConnection.dbConnection.commit()

        except:

            print("ERROR: Failed to add bin record. ")

    elif userAddQuery == "item" or userAddQuery == "Item" or userAddQuery == "ITEM":

        itemName = str(input("> Insert an item name: "))

        itemBin = str(input("> Insert the bin number of the item: "))

        itemRow = str(input("> Insert the row number of the bin: "))

        DatabaseConnection.dbConnection.execute(
            "INSERT INTO item (RowId, BinId, Description, CreateDate, CreateUser, Status) VALUES (?,?,?,CURRENT_TIMESTAMP,'sajorobinson','1')",
            (itemRow, itemBin, itemName),
        )

        try:

            DatabaseConnection.dbConnection.commit()

        except:

            print("ERROR: Failed to add item record. ")


def recordCheck():

    userCheckQuery = input("> Do you want to check OUT or check IN? ")

    if userCheckQuery == "out" or userCheckQuery == "Out" or userCheckQuery == "OUT":

        databaseSearch = DatabaseConnection.dbCursor.execute(
            "SELECT * FROM item WHERE Status = 1 ORDER BY RowId"
        )

        results = DatabaseConnection.dbCursor.fetchall()

        if results != []:

            print(ItemTableColumns.columns)

            for item in results:
                print(item)

            itemQuery = input(
                "> Which item do you want to check out? Provide the ItemId (the number on the far-left) "
            )

            DatabaseConnection.dbConnection.execute(
                "UPDATE item SET STATUS = '2' WHERE ItemId = '" + itemQuery + "'"
            )

            try:

                DatabaseConnection.dbConnection.commit()

            except:

                print(
                    "ERROR: Failed to check out record. Please leave a physical note so the record can be updated later. "
                )

        elif results == []:

            print("No items available to check out!")

        else:

            print("No results found!")

    elif userCheckQuery == "in" or userCheckQuery == "In" or userCheckQuery == "IN":

        databaseSearch = DatabaseConnection.dbCursor.execute(
            "SELECT * FROM item WHERE Status = 2 ORDER BY RowId"
        )

        results = DatabaseConnection.dbCursor.fetchall()

        if results != []:

            print(ItemTableColumns.columns)

            for item in results:
                print(item)

            itemQuery = input(
                "> Which item do you want to check in? Provide the ItemId (the number on the far-left) "
            )

            DatabaseConnection.dbConnection.execute(
                "UPDATE item SET STATUS = '1' WHERE ItemId = '" + itemQuery + "'"
            )

            try:

                DatabaseConnection.dbConnection.commit()

            except:

                print(
                    "ERROR: Failed to check out record. Please leave a physical note so the record can be updated later. "
                )

        elif results == []:

            print("No items available to check out!")

        else:

            print("No results found!")


def recordSearch():

    userSearchQuery = input("> Search for a term: ")

    databaseSearch = DatabaseConnection.dbCursor.execute(
        "SELECT * FROM item WHERE Description LIKE '%" + userSearchQuery + "%'"
    )

    resultsParse()


def listAll():

    orderInput = input("> Order by ROW, BIN, ITEM, or STATUS? ")

    if orderInput == "row" or orderInput == "Row" or orderInput == "ROW":

        databaseSearch = DatabaseConnection.dbCursor.execute(
            "SELECT * FROM item ORDER BY RowId"
        )

        resultsParse()

    elif orderInput == "bin" or orderInput == "Bin" or orderInput == "BIN":

        databaseSearch = DatabaseConnection.dbCursor.execute(
            "SELECT * FROM item ORDER BY BinId"
        )

        resultsParse()

    elif orderInput == "item" or orderInput == "Item" or orderInput == "ITEM":

        databaseSearch = DatabaseConnection.dbCursor.execute(
            "SELECT * FROM item ORDER BY ItemId"
        )

        resultsParse()

    elif orderInput == "status" or orderInput == "Status" or orderInput == "STATUS":

        databaseSearch = DatabaseConnection.dbCursor.execute(
            "SELECT * FROM item ORDER BY Status"
        )

        resultsParse()

    else:

        print("Please provide a valid option. ")


userInterface()
