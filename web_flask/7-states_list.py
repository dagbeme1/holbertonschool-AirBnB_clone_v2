#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays a HTML page with a list of all State objects present in DBStorage
    """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_session(exception):
    """
    Removes the current SQLAlchemy Session after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

