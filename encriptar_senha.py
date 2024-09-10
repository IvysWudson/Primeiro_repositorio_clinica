import sqlite3
import bcrypt

def conect_bd():
    conn = sqlite3.connect("Login.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS login(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           user TEXT NOT NULL,
           password) """)
    usuario = 'ivys'
    senha_clara = '123123'
    encriptada = bcrypt.gensalt()
    encriptada = bcrypt.hashpw(senha_clara.encode('UTF-8'), encriptada)

    cur.execute("INSERT INTO login(user, password) VALUES (?, ?)", (usuario, encriptada))
    conn.commit()
    conn.close()