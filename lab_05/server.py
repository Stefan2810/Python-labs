from flask import Flask
from flask import jsonify, request
import json
from task import Task

app = Flask(__name__)
database = {}

#1
@app.route('/sanity', methods=['GET'])
def sanity():
    response = jsonify({
        "status": "ok"
    })
    response.status_code = 200
    return response

#2
@app.route('/add', methods=['POST'])
def addTask():
    # Read the json from the request
    j =  request.get_json()
    # Create Task instance
    task = Task(**j)
    # We are casting task into a dictionary.
    # We are doing this because we want to store
    # the database into a json later.
    database[task.id] = task.__dict__
    response = jsonify({
        "status": "merge"
    })
    response.status_code=200
    return response

#3
@app.route('/print', methods=['GET'])
def showTasks():
    # TO DO return database in json format
    j = json.dumps(database)
    return j

#3.1
@app.route('/print/<name>', methods=['GET'])
def showEmployeeTasks(name):
    # TO DO search for tasks that have the employyes name
    # return them in json format
    employee_tasks = [task for task in database.values() if task['name'] == name]
    return jsonify(employee_tasks)

#3.2
@app.route('/print/pending', methods=['GET'])
def showPendingTasks():
    # TO DO search for tasks that have status not done
    # return them in json format
    pending_tasks = [task for task in database.values() if task['status'] == 'not done']
    return jsonify(pending_tasks)

#3.3
@app.route('/print/completed', methods=['GET'])
def showCompletedTasks():
    # TO DO search for tasks that have status completed
    # return them in json format
    completed_tasks = [task for task in database.values() if task['status'] == 'completed']
    return jsonify(completed_tasks)
#4
@app.route('/delete/<id>', methods=['DELETE'])
def deleteTask(id):
    # TO DO delete the task that has the id id from the database
    if id in database:
        del database[id]
        return jsonify({"status": "Task deleted"}), 200
    else:
        return jsonify({"status": "Task not found"}), 404

#4.1
@app.route('/delete/all', methods=['DELETE'])
def deleteAllTasks():
    # TO DO clear database
    database.clear()
    return jsonify({"status": "All tasks deleted"}), 200

#5
@app.route('/update/<id>', methods=['POST'])
def updateTaskStatus(id):
    # TO DO change task status to completed
    if id in database:
        database[id]['status'] = 'completed'
        return jsonify({"status": "Task status updated"}), 200
    else:
        return jsonify({"status": "Task not found"}), 404

#5.1
@app.route('/update/<id>/<name>', methods=['POST'])
def updateTaskAssignee(id, name):
    # TO DO change task asignee
    if id in database:
        database[id]['name'] = name
        return jsonify({"status": "Task assignee updated"}), 200
    else:
        return jsonify({"status": "Task not found"}), 404

#6
@app.route('/save', methods=['POST'])
def saveTasks():
    # TO DO store database to a json file
    with open('database.json', 'w') as f:
        json.dump(database, f)
    return jsonify({"status": "Database saved"}), 200

#7
@app.route('/load', methods=['POST'])
def loadTasks():
    # TO DO load database from json file
    global database
    with open('database.json', 'r') as f:
        database = json.load(f)
    return jsonify({"status": "Database loaded"}), 200

