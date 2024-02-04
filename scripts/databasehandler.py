import sqlite3

class DatabaseHandler():
    def __init__(self, dbName, keepSchema: bool = True):
        self.cursor = sqlite3.connect(dbName)
        if not keepSchema:
            print('ya schema empty, yeet')
            self.create_tables()

    # create table as specified
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                album TEXT NOT NULL
            );
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS lyrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                song_id INTEGER,
                order INTEGER,
                lyric TEXT NOT NULL,
                translation TEXT NOT NULL,
                reference TEXT
            );
        """)
    
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS slides (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                song_id INTEGER,
                lyric1_id INTEGER,
                lyric2_id INTEGER
            );
        """)
        
        # you know this approach BEGS to be done in Java/Go...
        
        # CRUD song
        
        # CRUD lyrics
        
        # CRUD slides
         