from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('login.html')

@app.route("/data.html")
def data():
    return render_template('data.html')

@app.route("/supplier_login", methods=['POST'])
def supplier_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "1":
            cursor.execute("SELECT * FROM mytest")
            return f"{cursor.fetchall()}"
        else:
            return "Invalid Login"


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


if __name__ == "__main__":
    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-19f8d195-meiliboxi-a85c.aivencloud.com",
        password="AVNS_xib9vXI_vgJ6wC8cERs",
        read_timeout=timeout,
        port=14698,
        user="avnadmin",
        write_timeout=timeout,
    )
    cursor = connection.cursor()
    app.run(debug=True)