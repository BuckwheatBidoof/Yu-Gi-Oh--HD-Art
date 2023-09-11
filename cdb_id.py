import os
import sqlite3

def idlist(directory, all_cards):
    path = directory + "/EDOPro.exe"
    
    if not os.path.isfile(path): # Checks if directory is correct
        return []
    
    list = []

    path = directory + "/expansions/cards.cdb"

    # connect to database
    con = sqlite3.connect(path)
    cur = con.cursor()

    # fetch all ids
    cur.execute("SELECT id FROM 'texts'")
    data = cur.fetchall()
    con.close()

    # add ids to list
    for row in data:
        list.append(row[0])

    # add rest of ids if user checked box to add other cards
    if all_cards:
        path = directory + "/expansions/cards-rush.cdb"
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("SELECT id FROM 'texts'")
        data = cur.fetchall()
        con.close()

        for row in data:
            list.append(row[0])
        
        path = directory + "/expansions/cards-skills.cdb"
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("SELECT id FROM 'texts'")
        data = cur.fetchall()
        con.close()

        for row in data:
            list.append(row[0])

    return list