from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "cs_record"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

def data_fetch(query, params=None):
    cur = mysql.connection.cursor()
    cur.execute(query, params)
    data = cur.fetchall()
    cur.close()
    return data

@app.route("/block_record", methods=["GET"])
def get_block_record():
    data = data_fetch("""SELECT * FROM block_record""")
    return make_response(jsonify(data), 200)

@app.route("/program_record", methods=["GET"])
def get_program_record():
    data = data_fetch("""SELECT * FROM program_record""")
    return make_response(jsonify(data), 200)

@app.route("/year_record", methods=["GET"])
def get_year_record():
    data = data_fetch("""SELECT * FROM year_record""")
    return make_response(jsonify(data), 200)

@app.route("/student_block", methods=["GET"])
def get_student_block():
    data = data_fetch("""SELECT * FROM student_block""")
    return make_response(jsonify(data), 200)

@app.route("/student_program", methods=["GET"])
def get_student_program():
    data = data_fetch("""SELECT * FROM student_program""")
    return make_response(jsonify(data), 200)

@app.route("/student_year", methods=["GET"])
def get_student_year():
    data = data_fetch("""SELECT * FROM student_year""")
    return make_response(jsonify(data), 200)

@app.route("/student_record", methods=["GET"])
def get_student_record():
    data = data_fetch("""SELECT * FROM student_record""")
    return make_response(jsonify(data), 200)


@app.route("/student_program/<int:student_id>/", methods=["GET"])
def get_student_program_by_ids(student_id):
    query = """
        SELECT program_record.*
        FROM student_program
        INNER JOIN program_record ON student_program.program_id = program_record.program_id
        WHERE student_program.student_id = %s
    """
    data = data_fetch(query, (student_id,))
    return make_response(jsonify(data), 200)

@app.route("/student_block/<int:student_id>/", methods=["GET"])
def get_student_block_by_ids(student_id):
    query = """
        SELECT block_record.*
        FROM student_block
        INNER JOIN block_record ON student_block.block_id = block_record.block_id
        WHERE student_block.student_id = %s
    """
    data = data_fetch(query, (student_id,))
    return make_response(jsonify(data), 200)

@app.route("/student_year/<int:student_id>/", methods=["GET"])
def get_student_year_by_ids(student_id):
    query = """
        SELECT year_record.*
        FROM student_year
        INNER JOIN year_record ON student_year.year_id = year_record.year_id
        WHERE student_year.student_id = %s
    """
    data = data_fetch(query, (student_id,))
    return make_response(jsonify(data), 200)

@app.route("/year_students/<int:year_id>", methods=["GET"])
def get_students_under_year(year_id):
    query = """
        SELECT student_record.student_id
        FROM student_year
        INNER JOIN student_record ON student_year.student_id = student_record.student_id
        WHERE student_year.year_id = %s
    """
    data = data_fetch(query, (year_id,))
    return make_response(jsonify(data), 200)


@app.route("/student_record", methods=["POST"])
def add_student_record():
    cur = mysql.connection.cursor()
    info = request.get_json()
    Studentid = info["Studentid"]
    Name = info["Name"]
    Email = info["Email"]
    Year = info["Year level"]
    cur.execute(
        """INSERT INTO student_record (student_id, name, email, year) VALUES (%s, %s, %s, %s)""",
        (Studentid, Name, Email, Year)
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
    Name = info["Name"]
    Email = info["Email"]
    Year = info["Year level"]
    cur.execute(
        """UPDATE student_record SET name = %s, email = %s, level = %s WHERE student_id = %s""",
        (Name, Email, Year, id),
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
