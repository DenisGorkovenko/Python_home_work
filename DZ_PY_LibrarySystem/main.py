from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, login_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'library_system_12354'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:652240@localhost:5432/library'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    fines = db.Column(db.Float, default=0.0)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    available = db.Column(db.Boolean, default=True)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Неверный логин или пароль')

    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    books = Books.query.all()
    return render_template('dashboard.html', username=current_user.username, books=books, fines=current_user.fines)


@app.route('/check_book', methods=['POST'])
@login_required
def check_book():
    title = request.form['title']
    book = Books.query.filter_by(title=title).first()
    if book:
        available = "Доступна" if book.available else "Не доступна"
        flash(f"Книга {book.title} ({available})")
    else:
        flash("Книга не найдена")
    return redirect(url_for('dashboard'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
