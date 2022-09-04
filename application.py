from flask import Flask, jsonify, request, Response

app = Flask(__name__)

USERS = {"Ping" : 'Pong!'}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return 'Index Page'
if __name__ == "__main__":
    app.run()
