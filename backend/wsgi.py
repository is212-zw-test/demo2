from application import init_app

# app = Flask(__name__)

# @app.route('/api/hi')
# def heartbeat():
#     return jsonify({'message': 'Hello World'})


if __name__ == '__main__':
    app = init_app()
    app.run(host='0.0.0.0', debug=True, port=5000)
