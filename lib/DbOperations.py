import sys, sqlite3

# Connection with the database

dbConnection = sqlite3.connect(r"C:\\Users\\samjo\\documents\\sqlite\\SgrStore.db")

dbCursor = dbConnection.cursor()

# Columns of the item table for the terminal

itemTableColumns = [
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

# For search queries, this receives all of the results from the database and prints them on the screen


def resultsParse():

    results = dbCursor.fetchall()

    if results != []:

        print(itemTableColumns)

        for item in results:
            print(item)

    elif results == []:

        print("No results found!")

    else:

        print("No results found!")


# This adds row, bin, or item records to the database


def recordAdd():

    userAddQuery = input("> Would you like to add a ROW, BIN, or ITEM? ")

    userAddQuery = userAddQuery.upper()

    if userAddQuery == "ROW":

        rowName = str(input("> Provide a unique row name (crafts, tools, etc.): "))

        dbConnection.execute("INSERT INTO row (Description) VALUES (?)", (rowName,))

        try:

            dbConnection.commit()

        except:

            print("ERROR: Failed to add row record. ")

    elif userAddQuery == "BIN":

        binName = str(input("> Provide a unique bin name (brushes, paper, electornics, etc.): "))

        rowName = str(input("> Provide an existing row number (where you will store the bin): "))

        dbConnection.execute(
            "INSERT INTO bin (RowId, Description) VALUES (?,?)", (rowName, binName)
        )

        try:

            dbConnection.commit()

        except:

            print("ERROR: Failed to add bin record. ")

    elif userAddQuery == "ITEM":

        itemName = str(input("> Insert an item name: "))

        itemBin = str(input("> Insert the bin number of the item (where you will store the item): "))

        itemRow = str(input("> Insert the row number of the bin (where the bin is stored): "))

        dbConnection.execute(
            "INSERT INTO item (RowId, BinId, Description, CreateDate, CreateUser, Status) VALUES (?,?,?,CURRENT_TIMESTAMP,'sajorobinson','1')",
            (itemRow, itemBin, itemName),
        )

        try:

            dbConnection.commit()

        except:

            print("ERROR: Failed to add item record. ")

    else:

        print("Please provide a valid option. ")


# This checks out or checks in records on the database by changing the status column


def recordCheck():

    userCheckQuery = input("> Do you want to check OUT or check IN? ")

    userCheckQuery = userCheckQuery.upper()

    if userCheckQuery == "OUT":

        databaseSearch = dbCursor.execute(
            "SELECT * FROM item WHERE Status = 1 ORDER BY RowId"
        )

        results = dbCursor.fetchall()

        if results != []:

            print(itemTableColumns)

            for item in results:
                print(item)

            itemQuery = input(
                "> Which item do you want to check out? Provide the ItemId (the number on the far-left) "
            )

            dbConnection.execute(
                "UPDATE item SET STATUS = '2', UpdateDate = CURRENT_TIMESTAMP, UpdateUser = 'sajorobinson' WHERE ItemId = '"
                + itemQuery
                + "'"
            )

            try:

                dbConnection.commit()

            except:

                print(
                    "ERROR: Failed to check out record. Please leave a physical note so the record can be updated later. "
                )

        elif results == []:

            print("No items available to check out!")

        else:

            print("No results found!")

    elif userCheckQuery == "IN":

        databaseSearch = dbCursor.execute(
            "SELECT * FROM item WHERE Status = 2 ORDER BY RowId"
        )

        results = dbCursor.fetchall()

        if results != []:

            print(itemTableColumns)

            for item in results:
                print(item)

            itemQuery = input(
                "> Which item do you want to check in? Provide the ItemId (the number on the far-left) "
            )

            dbConnection.execute(
                "UPDATE item SET STATUS = '1', UpdateDate = CURRENT_TIMESTAMP, UpdateUser = 'sajorobinson' WHERE ItemId = '"
                + itemQuery
                + "'"
            )

            try:

                dbConnection.commit()

            except:

                print(
                    "ERROR: Failed to check out record. Please leave a physical note so the record can be updated later. "
                )

        elif results == []:

            print("No items available to check out!")

        else:

            print("No results found!")

    else:

        print("Please provide a valid option. ")


# This searches the item table for a key word


def recordSearch():

    userSearchQuery = input("> Search for a term: ")

    databaseSearch = dbCursor.execute(
        "SELECT * FROM item WHERE Description LIKE '%" + userSearchQuery + "%'"
    )

    resultsParse()


# This lists all items in the item table


def listAll():

    orderInput = input("> Order by ROW, BIN, ITEM, or STATUS? ")

    orderInput = orderInput.upper()

    if orderInput == "ROW":

        databaseSearch = dbCursor.execute("SELECT * FROM item ORDER BY RowId")

        resultsParse()

    elif orderInput == "BIN":

        databaseSearch = dbCursor.execute("SELECT * FROM item ORDER BY BinId")

        resultsParse()

    elif orderInput == "ITEM":

        databaseSearch = dbCursor.execute("SELECT * FROM item ORDER BY ItemId")

        resultsParse()

    elif orderInput == "STATUS":

        databaseSearch = dbCursor.execute("SELECT * FROM item ORDER BY Status")

        resultsParse()

    else:

        print("Please provide a valid option. ")
