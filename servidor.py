from flask import Flask, request, jsonify
import sqlite3

app = Flask(_name_)

# Criação do banco
def criar_banco():
    con = sqlite3.connect("presencas.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS presencas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        horario TEXT NOT NULL
    )
    """)
    con.commit()
    con.close()