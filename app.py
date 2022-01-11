from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("dbtable.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/users", methods=["GET", "POST"])
def users():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor= conn.execute("SELECT * FROM Employees")
        dbtable= [
            dict(id=row[0], name=row[1], salary=row[2])
            for row in cursor.fetchall()
        ]
        if dbtable is not None:
            return jsonify(dbtable)



    if request.method == "POST":
        new_name = request.form["name"]
        new_salary = request.form["salary"]


    sql = """INSERT INTO Employees (name, salary)
                VALUES (?, ?)"""
    cursor = cursor.execute(sql, (new_name, new_salary))
    conn.commit()
    return f"Employee with the id: {cursor.lastrowid} created successfully", 201



@app.route("/Employees/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_employee(id):
    conn = db_connection()
    cursor = conn.cursor()
    Employees = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM Employees WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
          Employees = r
        if Employees is not None:
            g= jsonify(Employees)
            print(g)
            return jsonify(Employees), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """ UPDATE Employees SET name=?, salary=? WHERE id=? """
        name = request.form["name"]
        salary = request.form["salary"]
        
        updated_employees = { 
            "id": id,
            "name": name,
            "salary": salary
                 }
        conn.execute(sql, (name, salary, id))
        conn.commit()
        p= jsonify(updated_employees)
        print(p)
        return jsonify(updated_employees)

    if request.method == "DELETE":
        sql = """ DELETE FROM Employees WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The employee with id: {} has been deleted.".format(id), 200



if __name__ == "__main__":
    app.run(port = 5001, debug=True)