from flask import Flask, jsonify, abort, make_response, request
from flask_restplus import Namespace, Api
import ast
from waitress import serve

app = Flask(__name__)

api = Api(app)
myNamespace = Namespace("mydemo", "API list")
api.add_namespace(myNamespace)

tasks = [
  {
    'id': 1,
    'title': 'The title 1',
    'description': 'The description 1',
  },
  {
    'id': 2,
    'title': 'The title 2',
    'description': 'The description 2',
  }
]
 
@app.route('/myservice/api/v0/tasks', methods=['GET'])
def get_tasks():
  return jsonify( {'task': tasks}  ) 

@app.route('/myservice/api/v0/tasks', methods=['POST'])
def create_task():
  if not request.json or not 'title' in request.json:
    abort(400)
  task = {
    'id': tasks[-1]['id'] + 1,
    'title': request.json.get('title'),
    'description': request.json.get('description')
  }
  tasks.append(task)
  return jsonify( {'task': task} ), 201


@app.route('/myservice/api/v0/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  task = [ task for task in tasks if task['id'] == task_id ]
  print(f'task_id={task_id}')
  print(f'task={task}')
  if len(task) == 0:
    abort(404)
  tasks.remove(task[0])
  return jsonify({'result': True}) 

@app.route('/myservice/api/v0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
  print(f'task_id={task_id}')
  task = [ task for task in tasks if task['id'] == task_id ]
  print(f'task={task}')
  if len(task) == 0:
    abort(404)
  if not request.json:
    abort(400)
  if 'title' in request.json and type(request.json['title']) != str:
    abort(400)
  if 'description' in request.json and type(request.json['done']) is not str:
    abort(400)
  task[0]['title'] = request.json.get( 'title')
  task[0]['description'] = request.json.get('description')
  return jsonify({'task': task[0]})
 
@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)
 
if __name__ == '__main__':
  #app.run(debug=True)
  app.run(debug=True, host='0.0.0.0')
    
