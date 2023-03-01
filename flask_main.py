from flask import Flask, render_template, request
import pickle 
from flask_cors import CORS

pickled_model = pickle.load(open('deploymentWorkshopModel.pkl', 'rb'))

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return {"message": "Hello World"}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        numbers = request.get_json()['X']
    except:
        return "Error, no input received"
    
    # try:
    #     # return a numpy.ndarray object
    #     res = pickled_model.predict(numbers)
    #     # convert into list then take the first element
    #     return {"res": res.tolist()[0]}
    # except:
    #     return {"res": "error"}
            # return a numpy.ndarray object
    res = pickled_model.predict([numbers])
    # convert into list then take the first element
    return {"res": res.tolist()[0]}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

