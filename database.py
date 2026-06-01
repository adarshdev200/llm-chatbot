import sqlite3
from datetime import datetime


class ChatDatabase:
    def __init__(self, db_path="chatbot.db"):
        # TODO 1: Store db_path as self.db_path
        self.db_path = db_path
        # TODO 2: Create a connection: self.conn = sqlite3.connect(db_path)
        self.conn = sqlite3.connect(db_path)
        # TODO 3: Create a cursor: self.cursor = self.conn.cursor()
        self.cursor = self.conn.cursor()
        # TODO 4: Call self._create_tables() to set up tables
        self._create_tables() 
    
    def _create_tables(self):
        # TODO 5: Execute CREATE TABLE IF NOT EXISTS for conversations
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            system_prompt TEXT,
            title TEXT
        ) """)
        # TODO 6: Execute CREATE TABLE IF NOT EXISTS for messages
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            conversation_id INTEGER,
            content TEXT,
            role TEXT,
            FOREIGN KEY (conversation_id) REFERENCES conversations(id))
            """)

        # TODO 7: self.conn.commit() to save the schema
        self.conn.commit()
    
    def create_conversation(self, title, system_prompt):
        """Creates a new conversation. Returns the new conversation_id."""
        # TODO 8: INSERT a new row into conversations
        self.cursor.execute("""
                            INSERT INTO conversations (title, system_prompt)
                            VALUES (?, ?)
                            """, (title, system_prompt))

        self.conn.commit()

        return self.cursor.lastrowid


    def save_message(self, conversation_id, role, content):
        """Saves a single message to the database."""
        # TODO 11: INSERT a new row into messages

        self.cursor.execute("""
                            INSERT INTO messages (conversation_id, role , content)
                            VALUES (?, ?, ?)
                            """, (conversation_id, role,content))

        self.conn.commit()

    
    def get_conversation_messages(self, conversation_id):
        """Returns all messages for a given conversation, ordered by time."""
        # TODO 13: SELECT all messages WHERE conversation_id = ?
        self.cursor.execute("""
                            SELECT * FROM messages WHERE conversation_id = ?
                            ORDER BY created_at 
                            """ , (conversation_id,))
        
        return self.cursor.fetchall()
       

    def list_conversations(self):
        """Returns all conversations, newest first."""
        # TODO 16: SELECT id, title, created_at FROM conversations
        self.cursor.execute("""
                            SELECT id,title,created_at FROM conversations
                            ORDER BY created_at DESC
                            """)
        return self.cursor.fetchall()
        
    
    def close(self):
        # TODO 19: self.conn.close()
        self.conn.close()

    def delete_conversation(self, conversation_id):
    # TODO 1: Delete all messages WHERE conversation_id = ?

        self.cursor.execute("""
                        DROP * FROM messages WHERE conversation_id =?
                            """ , (conversation_id,))
        
        self.cursor.execute("""
                            DROP * FROM conversation WHERE id=?
                            """, (conversation_id,))
        self.conn.commit()


    # TODO 2: Delete the conversation WHERE id = ?
    # TODO 3: self.conn.commit()
    pass



    