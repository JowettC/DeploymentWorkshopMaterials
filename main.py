from fastapi import FastAPI, Request
import pickle
app = FastAPI()

pickled_model = pickle.load(open('deploymentWorkshopModel.pkl', 'rb'))



@app.get("/")
async def root():
    
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(request: Request):
    req_info = await request.json()
    # array for size 4
    try:
        # return a numpy.ndarray object
        res = pickled_model.predict([req_info["X"]])
        # convert into list then take the first element
        return {"res": res.tolist()[0]}
    except:
        return {"res": "error"}
