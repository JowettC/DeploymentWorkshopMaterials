# DeploymentWorkshopMaterials
Tensorflow with simple dataset, deployment with flask and pickle 

### install dependencies
`pip install -r requirements.txt`

commands for windows:
`python -m uvicorn main:app --reload`


### For AWS deployment on ec2
1. create a new instance (free tier)
2. connect to instance

3. Install git and clone the repo `sudo yum install git` and `git clone <url>`
4. Go into directory using `cd DeploymentWorkshopMaterials`
4. Install dependencies `pip3 install -r requirements.txt`
5. Run Flask with `python3 flask_main.py` or fast api with `python3 -m uvicorn main:app --reload`