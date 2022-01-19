import sqlite3
from flask import Flask, jsonify
import os
import pdb

app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'nhl.db'),
))

@app.route('/nhl/players')
def players():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('select * from players;')
    players = cursor.fetchall()
    return jsonify(players)

@app.route('/nhl/players/<player_id>')
def show_player(player_id):
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('select * from players where id = ?;', (player_id,))
    player_details = cursor.fetchone()
    jsonify(player_details)

app.run(debug = True)
