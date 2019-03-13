import sys, sqlite3, getpass
from prettytable import PrettyTable

# Connection with the database

dbConnection = sqlite3.connect(r"C:\\Users\\samjo\\documents\\sqlite\\SgrStore.db")

dbCursor = dbConnection.cursor()

# Get the username from environment variables (only for modifying update records)

currentUser = getpass.getuser()

# For search queries, this receives all of the results from the database and prints them on the screen


def resultsParse():

    results = dbCursor.fetchall()

    if results != []:

        tableFormat = PrettyTable(
            [
                "ItemId",
                "RowId",
                "BinId",
                "Description",
                "Create date",
                "Create user",
                "Update date",
                "Update user",
                "Status",
            ]
        )

        for item in results:

            tableFormat.add_row(item)

        print(tableFormat)

    elif results == []:

        print("> No results found!")

    else:

        print("> No results found!")


# This adds row, bin, or item records to the database


def recordAdd():

    itemName = str(input("> Insert an item name: "))

    itemBin = str(
        input("> Insert the bin number of the item (where you will store the item): ")
    )

    itemRow = str(
        input("> Insert the row number of the bin (where the bin is stored): ")
    )

    dbConnection.execute(
        "INSERT INTO item (RowId, BinId, Description, CreateDate, CreateUser, Status) VALUES (?,?,?,CURRENT_TIMESTAMP,'sajorobinson','1')",
        (itemRow, itemBin, itemName),
    )

    try:

        dbConnection.commit()

    except:

        print("> ERROR: Failed to add item record. ")


# This checks out or checks in records on the database by changing the status column


def recordCheck():

    userCheckQuery = input("> Do you want to check OUT or check IN? ")

    userCheckQuery = userCheckQuery.upper()

    if userCheckQuery == "OUT":

        dbCursor.execute("SELECT * FROM item WHERE Status = 1 ORDER BY RowId")

        results = dbCursor.fetchall()

        if results != []:

            tableFormat = PrettyTable(
                [
                    "ItemId",
                    "RowId",
                    "BinId",
                    "Description",
                    "Create date",
                    "Create user",
                    "Update date",
                    "Update user",
                    "Status",
                ]
            )

            for item in results:

                tableFormat.add_row(item)

            print(tableFormat)

            itemQuery = input(
                "> Which item do you want to check out? Provide the ItemId (on the far left): "
            )

            dbConnection.execute(
                "UPDATE item SET STATUS = '2', UpdateDate = CURRENT_TIMESTAMP, UpdateUser = '"
                + currentUser
                + "' WHERE ItemId = '"
                + itemQuery
                + "'"
            )

            try:

                dbConnection.commit()

            except:

                print(
                    "> ERROR: Failed to check out record. Please leave a physical note so the record can be updated later. "
                )

        elif results == []:

            print("> No items available to check out!")

        else:

            print("> No results found!")

    elif userCheckQuery == "IN":

        dbCursor.execute("SELECT * FROM item WHERE Status = 2 ORDER BY RowId")

        results = dbCursor.fetchall()

        if results != []:

            tableFormat = PrettyTable(
                [
                    "ItemId",
                    "RowId",
                    "BinId",
                    "Description",
                    "Create date",
                    "Create user",
                    "Update date",
                    "Update user",
                    "Status",
                ]
            )

            for item in results:

                tableFormat.add_row(item)

            print(tableFormat)

            itemQuery = input(
                "> Which item do you want to check in? Provide the ItemId (on the far-left) "
            )

            dbConnection.execute(
                "UPDATE item SET STATUS = '1', UpdateDate = CURRENT_TIMESTAMP, UpdateUser = '"
                + currentUser
                + "' WHERE ItemId = '"
                + itemQuery
                + "'"
            )

            try:

                dbConnection.commit()

            except:

                print(
                    "> ERROR: Failed to check in record. Please leave a physical note so the record can be updated later. "
                )

        elif results == []:

            print("> No items available to check in!")

        else:

            print("> No results found!")

    else:

        print("> Please provide a valid option. ")


# This searches the item table for a key word


def recordSearch():

    userSearchQuery = input("> Search for a term: ")

    dbCursor.execute(
        "SELECT * FROM item WHERE Description LIKE '%" + userSearchQuery + "%'"
    )

    resultsParse()


# This lists all items in the item table


def listAll():

    orderInput = input("> Order items by ROW, BIN, ITEM, or STATUS? ")

    orderInput = orderInput.upper()

    if orderInput == "ROW":

        dbCursor.execute("SELECT * FROM Item ORDER BY RowId")

        resultsParse()

    elif orderInput == "BIN":

        dbCursor.execute("SELECT * FROM item ORDER BY BinId")

        resultsParse()

    elif orderInput == "ITEM":

        dbCursor.execute("SELECT * FROM item ORDER BY ItemId")

        resultsParse()

    elif orderInput == "STATUS":

        dbCursor.execute("SELECT * FROM item ORDER BY Status")

        resultsParse()

    else:

        print("> Please provide a valid option. ")
