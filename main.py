from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

app = FastAPI()


tasks = [
    {
        'id': 1,
        'title': 'Do Chores',
        'status': 'inprogress'
    },
    {
        'id': 2,
        'title': 'Study Python',
        'status': 'inprogress'
    }
]

@app.post('/add/task')
async def add_task(request: Request):
    data = await request.json() #{'id': 3, 'title':'kjas'}
    tasks.append(data)
    return tasks

@app.get('/tasks')
def get_all_tasks():
    return tasks

@app.get('/task')
def get_task(task_id):
    for t in tasks:
        if t['id'] == int(task_id):
            return t
    return "No Such task"

@app.put('/task')
async def update_task(request: Request):
    data = await request.json()
    for t in tasks:
        if t['id'] == data['id']:
            t.update(data)
            return tasks
    return "No such task"

@app.delete('/task/{task_id}')
def delete_task(task_id):
    for t in tasks:
        if t['id'] == int(task_id):
            tasks.remove(t)
            return tasks
    return "No such task"