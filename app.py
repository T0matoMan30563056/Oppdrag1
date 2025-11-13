from flask import Flask, render_template, request, redirect, session, url_for
from functools import wraps
import mysql.connector

app = Flask(__name__)
app.secret_key = "supersecretkey"
def get_db():
    return mysql.connector.connect(
        host="10.200.14.25",
        user="TheGoat",
        password="SixSeven",
        database="TheTalk"
    )

@app.route('/login', methods=['GET', 'POST'])
def login():                                  
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']

        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        db.close()

        if user:
            session['username'] = username
            # Redirect to MainPage.html
            return redirect(url_for('mainpage'))
        else:
            return "Invalid username or password"

    return render_template('Login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():                                  
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['Password']

        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            return "Account created! You can now log in."
        except mysql.connector.IntegrityError:
            return "Username already exists."
        finally:
            db.close()

    return render_template('Register.html')

@app.route('/mainpage')
def mainpage():
    return render_template('MainPage.html')




#  + ------------------------------------ +
#  | Users / Commnets Databses Code Below |
#  + ------------------------------------ +

@app.route('/Usersdb', methods=['POST', 'GET'])
def Users():
    db = get_db()
    mycursor = db.cursor()
    mycursor. execute("SELECT * FROM Users")
    result = mycursor.fetchall()
    db.close()
    return render_template('Usersdb.html', Users=result)

@app.route('/Usersdb/add', methods=['POST', 'GET'])
def add_User():
    name = request.form['username']
    password = request.form['password']
    db = get_db()
    mycursor = db.cursor()
    mycursor.execute("INSERT INTO Users (username, password) VALUES (%s, %s)", (name, password))
    db.commit()
    db.close
    return redirect('/Usersdb')

@app.route('/Usersdb/delete/<int:id>', methods=['POST', 'GET'])
def delete_customer(id):
    db = get_db()
    mycursor = db.cursor()
    mycursor.execute("DELETE FROM Users WHERE id = %s", (id,))
    db.commit()
    db.close()
    return redirect('/Usersdb')



if __name__ == "__main__":
    app.run(debug=True)