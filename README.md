# Fast Fire 

A Simple Python web Server which performs basic CRUD Operation using FastAPI and Firebase.  

### Get the Code

#### Clone Repository 

```
$ mkdir fast-fire
$ cd fast-fire
$ git clone https://github.com/Arvind-4/fire-fast.git .
```
- Create Virtual Environment for Python

```
$ pip install virtualenv
$ python -m venv .
```

- Activate Virtual Environment

```
$ source bin/activate
```

- Install Dependencies

```
$ pip install -r requirements.txt
```



- Run Server 
```
$ uvicorn app.main:app --reload
```
to run it offline, Copy the Secret.json file from Firebase Console to ignored.

```
$ ls

	app
	images
	LICENSE
	poetry.lock     
	pyvenv.cfg
	bin  
	ignored  
	lib     
	notebooks  
	pyproject.toml  
	requirements.txt
```
```
$ cd ignored
$ ls
	secret.json
```

for the working of Image Upload,

```
# in app/main.py

@app.get("/")

async def home():

# file_upload() <- Comment this out

return {"message": "Hello World"}```
