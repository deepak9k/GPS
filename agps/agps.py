# Coding started for the new web project.


from sqlite3 import dbapi2 as sq
from flask import Flask, request, session, url_for, redirect, render_template, \
     g, flash, _app_ctx_stack, jsonify
# create application


#app.config.from_object(__name__)
#app.config.from_envvar('WEB_SETTINGS', silent=True)


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
    temp=0
    for task in record:
        if task['id']==bus_id:
           temp= task['north']
           temp=temp/100
           north=temp//1
           temp=temp-north
           north+=temp*1.667

           temp = task['east']
           temp = temp / 100
           east = temp // 1
           temp = temp - east
           east += temp*1.667


    return render_template('map.html', north=north, east=east)

@app.route('/5466/<int:bus_id>', methods=['POST'])
def set_location(bus_id):

    flag=0
    for task in record:
        if task['id']==bus_id:
            flag=1
            task['north']=request.json['north']
            task['east']=request.json['east']
    if flag==0:
        task = {
        'id': request.json['id'],
        'north': request.json['north'],
        'east': request.json['east']
            }
        record.append(task)
    return jsonify({'added':bus_id}), 201


if __name__=="__main__":
    app.run()
