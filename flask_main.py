from flask import Flask, render_template, request
import pickle 
from flask_cors import CORS

pickled_model = pickle.load(open('deploymentWorkshopModel.pkl', 'rb'))

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "GET":
        return render_template('index.html')
    
    try:
        sepalLength = int(request.form['sepalLength'])
        sepalWidth = int(request.form['sepalWidth'])
        petalLength = int(request.form['petalLength'])
        petalWidth = int(request.form['petalWidth'])

    except:
        return render_template('index.html', res= "Enter All Fields!" )
    
    res = pickled_model.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])

    return render_template('index.html', res= res.tolist()[0] )




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

