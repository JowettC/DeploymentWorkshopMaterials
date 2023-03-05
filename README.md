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
- You can try running Flask with `python3 flask_main.py`
5. Create a service file `sudo nano /etc/systemd/system/myflaskapp.service`
6. Paste the following code into the file
```
[Unit]
Description=My Flask App
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/DeploymentWorkshopMaterials
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
```
7. Start the service `sudo systemctl start myflaskapp`