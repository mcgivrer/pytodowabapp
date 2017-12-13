import sqlite3
import markdown
import os
from bottle import route, run, debug, template, request, error, static_file

@route('/css/<file:path>', method='GET')
def files(file):
    print (os.path.abspath(__file__))
    print ('/css/%s' % file)
    return static_file( '/css/%s' % file,root=os.path.abspath(__file__))

@route('/')
@route('/todo')
@route('/tasks')
def tasks_list(msg=""):
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT id, description, status, priority FROM task order by priority DESC, status ASC")
    result = c.fetchall()

    c.close()
    return template("templates/tasks_list",rows = result , msg="")

@route('/new', method='GET')
def new_task():
    return template('templates/task_create.tpl')


@route('/new', method='POST')
def new_save():
    description = request.POST.description.strip()
    priority = request.POST.priority.strip()

    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("INSERT INTO task (description,status, priority) VALUES (?,?,?)", (description,0,str(priority)))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return tasks_list('<p>The new task was inserted into the database, the ID is %s</p>' % new_id)

@route('/task/<id:int>', method='GET')
def edit_task(id):
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT id,description,status,priority FROM task WHERE id LIKE ?", (str(id),))
    cur_data = c.fetchone() 

    c.close()
    return template('templates/task_edit', old=cur_data, no=id)

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

@route('/task', method='POST')
def save():

    id = request.POST.id.strip()
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
    c.execute("UPDATE task SET description = ?, status = ?, priority = ? WHERE id LIKE ?", (description, status, priority, id))
    conn.commit()

    c.close()
    return tasks_list('<p>The new task was inserted into the database, the ID is %s</p>' % id)

@route('/done/<id:int>', method='GET')
def task_done(id):

    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE task SET status = 1 WHERE id = ?", (str(id),))
    conn.commit()

    c.close()
    return tasks_list('<p>The new task was inserted into the database, the ID is %s</p>' % id)


@route('/todo/<id:int>', method='GET')
def task_done(id):

    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("UPDATE task SET status = 0 WHERE id = ?", (str(id),))
    conn.commit()

    c.close()
    return tasks_list('<p>The new task was inserted into the database, the ID is %s</p>' % id)


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


debug(True)
run(host='localhost', port=8080, reloader=True)
