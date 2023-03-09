from flask import Flask, render_template, request, jsonify

#declare Flask Object app 
app = Flask(__name__)

# root path
@app.route("/")
def index():
    return jsonify({"message": "This is the root path"}), 200

# return hello name
@app.route("/hello/<name>")
def hello(name):
    if len(name) < 5:
        return jsonify({"message": "Name must be at least 5 characters"}), 400
    else:
        return jsonify({"message": "Hello " + name}), 200

if __name__ == "__main__":
    app.run(debug=True)