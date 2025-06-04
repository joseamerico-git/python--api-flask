#Exemplo de criação de api(s) com Python e flask.
# Endpoints:
#  
# POST /tasks http://localhost:5000/tasks
#{
#  "title": "Aprender Flask",
#  "description": "Estudar a criação de APIs"
#}

# GET /tasks http://localhost:5000/tasks listar as tasks

#PUT /tasks/2 http://localhost:5000/tasks/2
#{
# "title": "Aprender Flask demais",
# "description": "Estudar a criação de APIs"
#}


#DELETE /tasks/2 http://localhost:5000/tasks/2
#{
 # "title": "Aprender Flask demais",
 # "description": "Estudar a criação de APIs"
#}


from flask import Flask 
from flask import request, jsonify, render_template

app = Flask(__name__)



# Criação da rota na raiz que retorna uma mensagem.

@app.route("/")
def home():
    return render_template('home.html')





tasks = []  # Lista para armazenar as tarefas
task_id_control = 1  # Controlador de IDs para garantir unicidade

# Rota post para salvar as tarefas 


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()  # Pega os dados enviados no corpo da requisição
    new_task = {
        "id": task_id_control,
        "title": data.get("title"),  # Obtém o título enviado
        "description": data.get("description", ""),  # Descrição opcional
        "completed": False  # Define que a tarefa começa como incompleta
    }
    tasks.append(new_task)  # Adiciona a nova tarefa à lista
    task_id_control += 1  # Incrementa o ID para a próxima tarefa
    return jsonify({"message": "Tarefa criada com sucesso!", "task": new_task}), 201


# Rota Get tasks

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks, "total": len(tasks)})

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    # Procura a tarefa pelo ID
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404

    data = request.get_json()
    # Atualiza os campos da tarefa com os dados enviados
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["completed"] = data.get("completed", task["completed"])
    return jsonify({"message": "Tarefa atualizada com sucesso!", "task": task})



@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Tarefa deletada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)