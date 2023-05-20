from flask import Flask, request, jsonify

app = Flask(__name__)
grids = {}


def calculate_score(grid, x, y):
    size = len(grid)
    score = 0

    for i in range(max(0, x - 1), min(size, x + 2)):
        for j in range(max(0, y - 1), min(size, y + 2)):
            score += grid[i][j]

    return score


@app.route('/', methods=['GET'])
def welcome():
    return """
    <h1>Welcome to the Sun Spot Analyzer API</h1>
    <p>This API allows you to analyze areas of the Sun for thermal activity.</p>
    """

@app.route('/sun-spot-analyser-api/grid', methods=['POST'])
def create_grid():
    data = request.json
    size = data['size']
    values = list(map(int, data['values'].split(',')))

    grid = []
    for i in range(size):
        row = values[i * size : (i + 1) * size]
        grid.append(row)

    grid_id = len(grids) + 1
    grids[grid_id] = grid

    return jsonify({'id': grid_id}), 200


@app.route('/sun-spot-analyser-api/scores', methods=['GET'])
def get_scores():
    grid_id = int(request.args.get('id'))
    if grid_id not in grids:
        return 'Grid not found', 404

    grid = grids[grid_id]
    size = len(grid)

    scores = []
    for i in range(size):
        for j in range(size):
            score = calculate_score(grid, i, j)
            scores.append({'x': i+1, 'y': j+1, 'score': score})

    return jsonify({'scores': scores}), 200


if __name__ == '__main__':
    app.run(debug=True)
