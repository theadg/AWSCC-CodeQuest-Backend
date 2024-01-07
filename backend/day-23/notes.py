from flask import Blueprint, request, jsonify

notesBp = Blueprint('main', __name__)

from rest import baseUrl, tasks

# Route to get all Tasks
@notesBp.route('/', methods=['GET'])
def index():
    return jsonify(
        {
            'tasks': tasks
        }
    ), 200

# Route to get a new task
@notesBp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    if 'title' in data:
        task = {
            'title': data['title']
        }
        tasks.append(task)
        return jsonify(
            {
                'message': 'Task Created Successfully'
            },
            201
        )
    else:
        return (
            {
                'message': 'Title is required'
            },
            400
        )
    

# Route to get a new task
@notesBp.route('/<int:taskId>', methods=['GET'])
def show(taskId):
    if taskId < len(tasks):
        return jsonify(
            {
                'title': tasks[taskId]['title']
            }
        )
    else:
        return (
            {
                'message': 'Task not found'
            },
            400
        )

# Route to update a task
@notesBp.route("/<int:taskId>", methods=['PUT'])
def update(taskId):
    if taskId < len(tasks):
        data  = request.get_json()
        if 'title' in data:
            tasks[taskId]['title'] = data['title']
            return jsonify(
                {
                    'message': 'Task Updated Successfully'
                },
                200
            )
        else:
            return (
                {
                    'message': 'Title is required'
                },
                400
            )
    else:
        return jsonify(
            {
                'message': 'Task not found'
            }, 
            404
        )
    
# Route to delete a task
@notesBp.route("/<int:taskId>", methods=['DELETE'])
def delete(taskId):
    if taskId < len(tasks):
        del tasks[taskId]
        return jsonify(
            {
                'message': 'Task deleted successfully'
            },
            200
        )
    else: 
        return jsonify(
            {
                'message': 'Task not found'
            }, 
            404
        )