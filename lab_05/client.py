import requests

url = "http://127.0.0.1:5000/"

while True:
    command = input()
    if command == "Sanity check":
        x = requests.get(url)
        print(x.status_code)
    
    elif command == "Add":
        id = input("Enter task ID: ")
        name = input("Enter employee name: ")
        description = input("Enter task description: ")
        status = input("Enter task status: ")

        task_data = {
            "id": id,
            "name": name,
            "description": description,
            "status": status
        }

        response=request.post(url=url + "/add",json=task_data)

    elif command == "Print":
        response = requests.get(url + "/print")
        if response.status_code == 200:
            print(response.json())
        else:
            print("Error:", response.status_code)

    elif command == "Print Employee Tasks":
        name = input("Enter employee name: ")
        response = requests.get(url + "print/" + name)
        if response.status_code == 200:
            print(response.json())
        else:
            print("Error:", response.status_code)
            
    elif command == "Print Pending Tasks":
        response = requests.get(url + "print/pending")
        if response.status_code == 200:
            print(response.json())
        else:
            print("Error:", response.status_code)
            
    elif command == "Print Completed Tasks":
        response = requests.get(url + "print/completed")
        if response.status_code == 200:
            print(response.json())
        else:
            print("Error:", response.status_code)
            
    elif command == "Delete":
        id = input("Enter task ID to delete: ")
        response = requests.delete(url + "delete/" + id)
        if response.status_code == 200:
            print("Task deleted successfully.")
        else:
            print("Error:", response.status_code)
            
    elif command == "Delete All":
        response = requests.delete(url + "delete/all")
        if response.status_code == 200:
            print("All tasks deleted successfully.")
        else:
            print("Error:", response.status_code)
            
    elif command == "Complete Task":
        id = input("Enter task ID to mark as completed: ")
        response = requests.post(url + "update/" + id)
        if response.status_code == 200:
            print("Task status updated successfully.")
        else:
            print("Error:", response.status_code)
            
    elif command == "Change Task Assignee":
        id = input("Enter task ID: ")
        name = input("Enter new employee name: ")
        response = requests.post(url + "update/" + id + "/" + name)
        if response.status_code == 200:
            print("Task assignee updated successfully.")
        else:
            print("Error:", response.status_code)
            
    elif command == "Save":
        response = requests.post(url + "save")
        if response.status_code == 200:
            print("Database saved successfully.")
        else:
            print("Error:", response.status_code)
            
    elif command == "Load":
        response = requests.post(url + "load")
        if response.status_code == 200:
            print("Database loaded successfully.")
        else:
            print("Error:", response.status_code)
            
    elif command == "Exit":
        break