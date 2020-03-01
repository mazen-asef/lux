import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def create_dialogue (conn, dialogue):
    """
    Create a new dialogue in the dialogue table
    :param conn:
    :param dialogue:
    :return: dialogue id
    """
    sql = ''' INSERT INTO dialogue (tag, text, question, branches)
              VALUES (?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute (sql, dialogue)
    
    return cur.lastrowid
 
def main ():
    database = r"/home/mazen/Projects/lux/db/lux.db"
    
    # create a db connection
    conn = create_connection (database)
    
    with conn:
        print ("Dialogue Tag:\n")
        tag = input ()
        print ("Dialogue Text:\n")
        text = input ()
        print ("\nDialogue Question:\n")
        question = input ()
        print ("\nBranches:\n")
        branches = input ()
        dialogue = (tag, text, question, branches)
        
        create_dialogue (conn, dialogue)

if __name__ == '__main__':
    main()
