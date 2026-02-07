from flask import Flask, render_template, request, jsonify
from test import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        a = float(data.get('a'))
        b = float(data.get('b'))
        operation = data.get('operation')
        
        if operation == 'add':
            result = calc.add(a, b)
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            result = calc.divide(a, b)
        elif operation == 'power':
            result = calc.power(a, b)
        elif operation == 'modulo':
            result = calc.modulo(a, b)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({'result': result, 'success': True})
    except ValueError as e:
        return jsonify({'error': str(e), 'success': False}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred: ' + str(e), 'success': False}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
