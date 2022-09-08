from email import message
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET', 'POST'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)
       
    
@app.route("/users", methods=['GET', 'POST'])
def show_all_user_and_add():
    if request.method == 'POST':
        username = list(request.json.keys())[0]
        user_details = USERS.get(username)
        if (len(username) > 0) and not user_details:
            USERS.update({username : list(request.json.values())[0]})
            return jsonify(message = "Created user")
        else:
            return jsonify(message = "User already exists") 
    elif request.method == 'GET':
        return jsonify(USERS)
        
if __name__ == "__main__":
    app.run()
