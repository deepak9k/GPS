# Coding started for the new web project.


from sqlite3 import dbapi2 as sq
from flask import Flask, request, session, url_for, redirect, render_template, \
     g, flash, _app_ctx_stack, jsonify
# create application

app = Flask('agps')
app.config.from_object(__name__)
app.config.from_envvar('WEB_SETTINGS', silent=True)


#Flask object
app = Flask(__name__)


#Data entries
record = [
    {
        'id': 1,
        'north': 28.602834,
        'east':  77.1986838

    },
    {
        'id': 2,
        'north': 28.602834,
        'east':  77.1986838

    }
]


@app.route('/<int:bus_id>', methods=['GET'])
def get_location(bus_id):
    error=None
    north=0
    east=0
    for task in record:
        if task['id']==bus_id:
           north = task['north']
           east =  task['east']

           print("done if")
    print("done for")
    return render_template('map.html', north=north, east=east)

@app.route('/5466/<int:bus_id>', methods=['POST'])
def set_location(bus_id):

    flag=0
    test=request.form['north']
    for task in record:
        if task['id']==bus_id:
            flag=1
            task['north']=request.form['north']
            task['east']=request.form['east']
    if flag==1:
        task = {
        'id': request.form['bus_id'],
        'north': request.form['north'],
        'east': request.form['east']
            }
        record.append(task)

    return jsonify({"north": test}), 201


if __name__=="__main__":
    app.run()
