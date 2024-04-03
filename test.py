import sqlite3

DATABASE = 'Database.db'

def print_all_games():
    game = input("What name: ")
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT name FROM game WHERE name = ?;"
        cursor.execute(sql, (game,))
        results = cursor.fetchall()
        #print nicely

        for games in results:
            print(f"Number: {games[0]} Names: {games[1]}")

if __name__=="__main__":
    print_all_games()