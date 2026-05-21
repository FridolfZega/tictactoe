from flask import Flask, render_template, request, jsonify
from game import check_winner

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check', methods=['POST'])
def api_check():
    data = request.get_json(force=True)
    board = data.get('board', [])
    winner, combo = check_winner(board)
    return jsonify({'winner': winner, 'combo': list(combo) if combo else None})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
