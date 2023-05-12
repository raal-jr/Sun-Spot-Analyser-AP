from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create a new database and table to store grids
conn = sqlite3.connect('sun_spot.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS grids
             (id INTEGER PRIMARY KEY, size INTEGER, values TEXT)''')
conn.commit()

# Endpoint to create a new grid
@app.route('/sun-spot-analyser-api/grid', methods=['POST'])
def create_grid():
    # Parse request body
    data = request.get_json()
    size = data['size']
    values = list(map(int, data['values'].split(',')))
    
    # Generate a new ID for the grid
    c.execute('INSERT INTO grids (size, values) VALUES (?, ?)', (size, ','.join(map(str, values))))
    grid_id = c.lastrowid
    conn.commit()
    
    # Return the ID of the grid
    return jsonify({'id': grid_id})

# Endpoint to get the scores for a grid
@app.route('/sun-spot-analyser-api/scores', methods=['GET'])
def get_scores():
    # Parse query parameter
    grid_id = request.args.get('id')
    
    # Retrieve the size and values of the grid from the database
    c.execute('SELECT size, values FROM grids WHERE id=?', (grid_id,))
    result = c.fetchone()
    size = result[0]
    values = list(map(int, result[1].split(',')))
    
    # Generate a 2D array to represent the grid
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            grid[i][j] = values[i * size + j]
    
    # Calculate the scores for each cell in the grid
    scores = []
    for i in range(size):
        for j in range(size):
            score = grid[i][j]
            if i > 0:
                score += grid[i-1][j]
            if i < size-1:
                score += grid[i+1][j]
            if j > 0:
                score += grid[i][j-1]
            if j < size-1:
                score += grid[i][j+1]
            scores.append({'x': j+1, 'y': i+1, 'score': score})
    
    # Sort the scores in descending order
    scores.sort(key=lambda x: x['score'], reverse=True)
    
    # Return the scores as a JSON object
    return jsonify({'scores': scores})

if __name__ == '__main__':
    app.run(debug=True)
