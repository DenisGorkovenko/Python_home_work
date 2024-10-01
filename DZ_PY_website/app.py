import psycopg2
from flask import Flask, render_template, request, redirect, abort
from flask_mail import Mail, Message

from models.contact import ContactMessage


app = Flask(__name__)
mail = Mail(app)
mail.init_app(app)

app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 8025


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = (request.form['name'], request.form['email'], request.form['message'], request.form['title'])
        cursor.execute('''INSERT INTO contact(name, email, message, title) VALUES(%s, %s, %s, %s)''', data)
        msg_send = Message(subject=request.form['message'], sender=request.form['email'], recipients=['test@test.com'])
        # для теста используем вывод print
        print(msg_send)
        # mail.send(msg_send)

        conn.commit()
        return redirect('/')
    elif request.method == 'GET':
        return render_template('contact.html')


@app.route('/messages', methods=['POST'])
def get_messages():
    email = request.form['email']
    cursor.execute('''SELECT * FROM contact WHERE email=%s ORDER BY answer_message, contact_id DESC''', (email,))
    data = cursor.fetchall()
    msgs = []
    for row in data:
        msgs.append(ContactMessage(id=row[0], name=row[1], email=row[2], msg=row[3], title=row[4], answer=row[5]))
    return render_template('index.html', messages=msgs)


@app.route('/message')
def message_detail():
    msg_id = request.args.get('id')
    if not msg_id or not msg_id.isdigit():
        abort(404)
    cursor.execute('''SELECT * FROM contact WHERE contact_id=%s''', (msg_id,))
    data = cursor.fetchone()
    if data:
        msg = ContactMessage(id=data[0], name=data[1], email=data[2], msg=data[3], title=data[4], answer=data[5])
    else:
        abort(404)
    return render_template('message.html', message=msg)


if __name__ == '__main__':
    conn = psycopg2.connect(dbname='library',
                            user='postgres',
                            password='postgres',
                            host='localhost',
                            port=5432)
    cursor = conn.cursor()

    app.run(debug=True)

    cursor.close()
    conn.close()
