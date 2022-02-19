import sqlite3
from flask import Flask,request, Response,json

# for creating the table
#conn = sqlite3.connect('mydb.db')
#conn.execute("CREATE TABLE Task (ID INTEGER NOT NULL PRIMARY KEY, State TEXT, Title TEXT)")
#conn.close()

#for inserting tasks in the table
#conn = sqlite3.connect('mydb.db')
#conn.execute("INSERT INTO Task (State,Title) Values (?,?)",(stateGoesHere,titleGoesHere))

# initializing a flask app
app = Flask(__name__)

# setting up the API
@app.route("/")
def home():
    return "Hello"

@app.route("/ChangeState/<int:id>",methods=["GET","PUT","POST","DELETE"])
def change_state(id):
    if request.method=="POST":
        states_priorities = {"draft": 0, "active": 1, "done": 2, "archived": 3}
        conn = sqlite3.connect('mydb.db')
        cur = conn.execute("SELECT State From Task WHERE ID= ?", [id])
        state = cur.fetchone()[0]
        wished_state = request.data.decode("utf-8")
        if wished_state not in states_priorities.keys():
            return Response("not a predefined state",500)
        elif state==wished_state:
            return Response("the state is the same",200)
        elif states_priorities[wished_state] - states_priorities[state] == 1 or wished_state == "archived":
            cur = conn.execute("UPDATE Task SET State= ? WHERE ID= ?", (wished_state, id))
            conn.commit()
            cur = conn.execute("SELECT * From Task WHERE ID= ?", [id])
            return Response(f"state changed successfully {json.dumps(cur.fetchone())}", 200)
        else:
            return Response("not valid state please respect the flow draft -> active -> done -> archived", 500)
    elif request.method=="GET":
        conn = sqlite3.connect('mydb.db')
        cur = conn.execute("SELECT * From Task WHERE ID= ?", [id])
        Task=cur.fetchone()
        return Response(json.dumps(Task),200)

    elif request.method == "PUT":
        # will only modify title as state is only modified through post request
        # for easy use afterwards as u will only
        # need to specify the state not the whole object
        # id cannot be modified
        conn = sqlite3.connect('mydb.db')
        data=request.get_json()
        cur = conn.execute("UPDATE Task SET Title= ? WHERE ID= ?", (data['Title'],id))
        conn.commit()
        cur = conn.execute("SELECT * From Task WHERE ID= ?", [id])
        return Response(json.dumps(cur.fetchone()),200)
    elif request.method=="DELETE":
        conn = sqlite3.connect('mydb.db')
        cur=conn.execute("DELETE FROM Task WHERE ID=?",[id])
        conn.commit()
        return Response("Deleted",200)

if __name__ == "__main__":
    app.run(debug=True)