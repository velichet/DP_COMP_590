# DP_COMP_590
As part of our COMP 590 project, we will implement differential privacy for datasets.

It's recommended to run the app in a virtual environment. Below are the steps to do that.  
```
# Create virtual environment
python3 -m venv ./<name_of_virtualenv>

# Activate the virtual environment
source <name_of_virtualenv>/bin/activate 

# Use pip or pip3 to install dependencies
pip install -r requirements.txt
```

To start running the app use the following command. It should run on localhost port 8000.
```
# Start the app
python app.py
```

To connect to your MongoDB instance, create a .env file and update it with your user specific link which can be found on MongoDB when you choose to connect to a Python application. Below is what your .env file should contain. Be sure to whitelist your IP address in Mongo Atlas.

Also be sure to include the secret key for user auth.
```
MONGO_URI = <link>
SECRET_KEY = <secret>
```

Note : If you trying to execute the application on Apple M1 , PyDP package will fail and you will not be able to run the application . Issue here : https://github.com/OpenMined/PyDP/issues/402 
