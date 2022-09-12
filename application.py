from email import message
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET', 'PUT', 'DELETE'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)
    elif request.method == 'PUT':
        user_details = USERS.get(username)
        if user_details:
            USERS.pop(username)
            username = list(request.json.keys())[0]
            USERS.update({username:{'name' : list(request.json.values())[0]}})
            return jsonify(USERS.get(username))
        else:
            return Response(status=404)
    elif request.method == 'DELETE':
        user_details = USERS.get(username)
        if user_details:
            USERS.pop(username)
            return jsonify(message = "User Deleted")
        else:
            return Response(status=404)

       
    
@app.route("/users", methods=['GET', 'POST'])
def show_all_user_and_add():
    if request.method == 'POST':
        username = list(request.json.keys())[0]
        user_details = USERS.get(username)
        if (len(username) > 0) and not user_details:
            USERS.update({username:{'name' : list(request.json.values())[0]}})
            return jsonify(message = "Created user")
        else:
            return jsonify(message = "User already exists") 
    elif request.method == 'GET':
        return jsonify(USERS)
        
if __name__ == "__main__":
    app.run(debug=True)
