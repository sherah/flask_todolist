import flask
import model
from flask import redirect, url_for, render_template
from model import app, Task

@app.route("/")
def home():
    return_str = ""
    tasks = Task.query.all()
    return render_template("list_tasks.html", tasks=tasks)


@app.route("/add", methods=["GET"])
def make_task():
    return render_template("add_tasks.html") 

@app.route("/add", methods=["POST"])
def save_task():
	task = flask.request.form["task"]
	notes = flask.request.form["notes"]
	t = model.Task(task)
	t.notes = notes
	model.add(t)
	model.save_all()
	return "Thanks for adding your task."


