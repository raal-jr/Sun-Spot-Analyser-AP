from flask import Flask, request, jsonify

app = Flask(__name__)

grids = {}
grid_id = 1


@app.route('/')
def welcome():
    return 'Welcome to the Sun Spot Analyser API'


@app.route('/sun-spot-analyser-api/grid', methods=['POST'])
def create_grid():
    global grid_id
    size = int(request.form['size'])
    values = list(map(int, request.form['values'].split(',')))

    grid = {
        'id': grid_id,
        'size': size,
        'values': values
    }

    grids[grid_id] = grid
    grid_id += 1

    return jsonify({'id': grid['id']}), 200


@app.route('/sun-spot-analyser-api/scores', methods=['GET'])
def get_scores():
    grid_id = int(request.args.get('id'))
    if grid_id in grids:
        grid = grids[grid_id]
        scores = calculate_scores(grid['size'], grid['values'])
        return jsonify({'scores': scores}), 200
    else:
        return jsonify({'error': 'Grid not found'}), 404


@app.route('/sun-spot-analyser-api/cell', methods=['GET'])
def get_cell():
    grid_id = int(request.args.get('id'))
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    if grid_id in grids:
        grid = grids[grid_id]
        cell_value = get_cell_value(grid['size'], grid['values'], x, y)
        if cell_value is not None:
            return jsonify({'x': x, 'y': y, 'value': cell_value}), 200
        else:
            return jsonify({'error': 'Invalid cell coordinates'}), 400
    else:
        return jsonify({'error': 'Grid not found'}), 404


@app.route('/sun-spot-analyser-api/top', methods=['GET'])
def get_top_values():
    grid_id = int(request.args.get('id'))
    limit = int(request.args.get('limit', 5))
    if grid_id in grids:
        grid = grids[grid_id]
        top_values = get_top_values(grid['values'], limit)
        return jsonify({'top_values': top_values}), 200
    else:
        return jsonify({'error': 'Grid not found'}), 404


def calculate_scores(size, values):
    scores = []
    # Perform the score calculation logic here based on the grid size and values
    # This is just a dummy implementation
    for i, value in enumerate(values):
        x = (i % size) + 1
        y = (i // size) + 1
        score = value * 2
        scores.append({'x': x, 'y': y, 'score': score})
    return scores


def get_cell_value(size, values, x, y):
    index = (y - 1) * size + (x - 1)
    if 0 <= index < len(values):
        return values[index]
    else:
        return None


def get_top_values(values, limit):
    sorted_values = sorted(values, reverse=True)
    return sorted_values[:limit]


if __name__ == '__main__':
    app.run()
