# DeploymentWorkshopMaterials
Tensorflow with simple dataset, deployment with flask and pickle 

### install dependencies
`pip install fastapi[all]` or `pip install "fastapi[all]"`
`pip install uvicorn`

commands for windows:
`python -m uvicorn main:app --reload`


### For AWS deployment on ec2
1. create a new instance (free tier)
2. connect to instance
3. Install git and clone the repo `sudo yum install git` and `git clone <url>`
4. Python is already installed, install flask `pip install flask`