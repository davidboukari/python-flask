# python-flask

## To run 
```
# Create the venv
python3 -m venv ../venv 
source ../venv/bin/activate
pip install -r requirement.txt

# Run the app
python app/bin/app_srv.py
```

## To test
```
# List
curl http://localhost:5000/myservice/api/v0/tasks

# Add 
curl -H  "Content-type: application/json" --request POST     --data '{"title": "title 1", "description": "my description 1"}'     http://localhost:5000/myservice/api/v0/tasks

# Delete
curl --request DELETE http://localhost:5000/myservice/api/v0/task/

# Update
curl -H  "Content-type: application/json" --request PUT     --data '{"title": "title 2 --", "description": "my description 2---"}'     http://localhost:5000/myservice/api/v0/tasks/2
```
