import sqlite3
import markdown
import os
from bottle import route, run, debug, template, request, response, error, static_file

global templatePath
templatePath="default"
global theme
theme="templates/%s/%s" % (templatePath,'%s')

@route('/resources/<file:path>', method='GET')
def files(file):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return static_file( '/public/%s' % file, root=dir_path)

@route('/themes/<file:path>', method='GET')
def files(file):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return static_file( '/templates/%s' % file, root=dir_path)

@route('/')
@route('/todo')
@route('/tasks')
def tasks_list(msg="",status=2):
    todoId=1
    
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    c.execute("SELECT task.id as id, description, author.username as username, author.firstname as firstname, author.lastname as lastname, author.email as useremail, todoId, status, priority FROM task, author where task.author = author.username and status != ? order by status ASC, priority DESC, id DESC",str(status))
    tasks = c.fetchall()
    
    c.execute("SELECT id, name FROM todo where id = ?",str(todoId));
    todo = c.fetchone()

    c.close()
    print( theme % "tasks_list")

    return template(theme % "tasks_list", tasks = tasks, message = msg, todo = todo, theme=templatePath)

@route('/new', method='GET')
def new_task():
    return template(theme % 'task_create.tpl', theme=templatePath)

@route('/new', method='POST')
def new_save():
    description = request.POST.description.strip()
    priority = request.POST.priority.strip()

    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("INSERT INTO task (description,status,author, todoId, priority) VALUES (?,?,?,?,?)", (description,0,'212391884',0,str(priority)))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return tasks_list('The new task has been created (the ID is %s)' % new_id)

@route('/archives')
def archives_list():
    return tasks_list("Show archived tasks",0);


@route('/task/<id:int>', method='GET')
def edit_task(id):
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT id,description,todoId,author,status,priority FROM task WHERE id LIKE ?", (str(id),))
    cur_data = c.fetchone() 

    c.close()
    return template(theme % 'task_edit', old=cur_data, no=id, theme=templatePath)

@route('/delete/<id:int>', method='GET')
def delete_task(id):
    if id:
        conn = sqlite3.connect('todo.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute("DELETE FROM task  WHERE id = ?", (str(id),))
        conn.commit()

        c.close()
    return tasks_list("<p>the task %s has been deleted.</p>" % id)

@route('/archive/<id:int>', method='GET')
def archive_task(id):
    status=2
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE task SET status = ? WHERE id LIKE ?", (status, id))
    conn.commit()

    c.close()
    return tasks_list('The task %s has been archived.' % id)


@route('/task', method='POST')
def save():

    id = request.POST.id.strip()
    todoId = request.POST.todoId.strip()
    author = request.POST.author.strip()
    description = request.POST.description.strip()
    status = request.POST.status.strip()
    priority = request.POST.priority.strip()

    if status == 'open':
        status = 1
    else:
        status = 0

    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE task SET todoId = ?, author = ?, description = ?, status = ?, priority = ? WHERE id LIKE ?", (todoId, author, description, status, priority, id))
    conn.commit()

    c.close()
    return tasks_list('<p>The new task was inserted into the database, the ID is %s</p>' % id)

@route('/done/<id:int>', method='GET')
def task_status_done(id):

    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE task SET status = 1 WHERE id = ?", (str(id),))
    conn.commit()

    c.close()
    return tasks_list('Task # %s has been marked as DONE.' % id)

@route('/todo/<id:int>', method='GET')
def task_status_todo(id):

    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE task SET status = 0 WHERE id = ?", (str(id),))
    conn.commit()

    c.close()
    return tasks_list('Task %s has has been marked as TODO.' % id)

@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

debug(True)
run(host='localhost', port=80, reloader=True)
