
import sqlite3

def sqlite3_connect(db_name):
    if db_name.endswith(".db") or db_name.endswith(".sqlite3") or db_name == ":memory:":
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            sqlite3_console(db_name, conn, cursor)
            conn.close()
        except Exception as e:
            print(f"\033SQLite3 error: {e}\033[0m")
        
    else:
        print("\033[31mSQLite3: Selected database is not SQLite3 database!\033[0m")

def sqlite3_console(db_name, conn, cursor):
    print("""
Q-J-R SQLite3 -> on Q-J-R 
Type .exit to exit.
""")
    while True:

        sqlite3_cmd = input("qjr_sqlite> ")

        if sqlite3_cmd == ".exit":
            break
        elif sqlite3_cmd == ".tables":
            cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
            )

            for table in cursor.fetchall():
                print(table[0])
        
        else:
            try:
                cursor.execute(sqlite3_cmd)
                conn.commit()

                if sqlite3_cmd.upper().startswith("SELECT"):
                    for row in cursor.fetchall():
                        print(row)
            
            except KeyboardInterrupt:
                print("Program Interrupted")
            
            except Exception as e:
                print(f"\033[31mSQLite3 Error: {e}\033[0m")
            
        
    
