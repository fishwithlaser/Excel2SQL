# converter of geochemical data for "endmembers" of specific to GHG rocks
# author:  thomas kosciuch 
# contact: thomas@kosciuch.ca
# affilite: University of Toronto - Earth Sciences

# 1. Directory Structure
#
#   python code
#           /XSLX/
#               xlsx files
# 

import sqlite3
from sqlite3 import Error

# 1. create empty db

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == '__main__':
    create_connection("mineralEndmembers.db")





