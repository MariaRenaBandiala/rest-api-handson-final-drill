from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "record"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

@app.route("/program_student_table", methods=["GET"])
def get_program_student_table():
    data = data_fetch("""SELECT * FROM program_student_table""")
    return make_response(jsonify(data), 200)

@app.route("/program_table", methods=["GET"])
def get_program_table():
    data = data_fetch("""SELECT * FROM program_table""")
    return make_response(jsonify(data), 200)

@app.route("/st_yr_table", methods=["GET"])
def get_st_yr_table():
    data = data_fetch("""SELECT * FROM st_yr_table""")
    return make_response(jsonify(data), 200)

@app.route("/student_record", methods=["GET"])
def get_student_record():
    data = data_fetch("""SELECT * FROM student_record""")
    return make_response(jsonify(data), 200)

@app.route("/year", methods=["GET"])
def get_year():
    data = data_fetch("""SELECT * FROM year""")
    return make_response(jsonify(data), 200)

@app.route("/student_record", methods=["POST"])
def add_student_record():
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    date_of_birth = info["date_of_birth"]
    cur.execute(
        """INSERT INTO student_record (first_name, last_name, date_of_birth) VALUES (%s, %s, %s)""",
        (first_name, last_name, date_of_birth),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify({"message": "Student record added successfully", "rows_affected": rows_affected}),
        201,
    )

@app.route("/student_record/<int:id>", methods=["PUT"])
def update_student_record(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    date_of_birth = info["date_of_birth"]
    cur.execute(
        """UPDATE student_record SET first_name = %s, last_name = %s, date_of_birth = %s WHERE student_id = %s""",
        (first_name, last_name, date_of_birth, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify({"message": "Student record updated successfully", "rows_affected": rows_affected}),
        200,
    )

@app.route("/student_record/<int:id>", methods=["DELETE"])
def delete_student_record(id):
    cur = mysql.connection.cursor()
    cur.execute("""DELETE FROM student_record WHERE student_id = %s""", (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify({"message": "Student record deleted successfully", "rows_affected": rows_affected}),
        200,
    )

if __name__ == "__main__":
    app.run(debug=True)
