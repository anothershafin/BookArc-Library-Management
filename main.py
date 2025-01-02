from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database_name"
)
cursor = db.cursor()

# Routes for existing features
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template('catalog.html', books=books)

@app.route('/admindashboard')
def admin_dashboard():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template('admindashboard.html', books=books)

@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        isbn = request.form['isbn']
        book_name = request.form['book_name']
        author = request.form['author']
        availability = request.form['availability']
        rating = request.form['rating']

        query = "INSERT INTO books (isbn, book_name, author, availability, rating) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (isbn, book_name, author, availability, rating))
        db.commit()

        return redirect('/admindashboard')
    return render_template('add_book.html')

@app.route('/delete_book', methods=['POST'])
def delete_book():
    isbn = request.form['isbn']
    query = "DELETE FROM books WHERE isbn = %s"
    cursor.execute(query, (isbn,))
    db.commit()
    return redirect('/admindashboard')

@app.route('/lend_book', methods=['POST', 'GET'])
def lend_book():
    if request.method == 'POST':
        isbn = request.form['isbn']
        user_email = request.form['user_email']
        admin_email = request.form['admin_email']
        lend_date = request.form['lend_date']

        query = "UPDATE books SET availability = 0 WHERE isbn = %s"
        cursor.execute(query, (isbn,))
        db.commit()

        # You can add more logic to track lending details if required.
        return redirect('/admindashboard')
    return render_template('lend_book.html')

# New Code for Reservation System

@app.route('/reserve_book', methods=['POST'])
def reserve_book():
    isbn = request.form['isbn']
    user_email = request.form['user_email']
    
    # Insert the reservation request into the database with 'Pending' status
    query = "INSERT INTO reservations (isbn, user_email, status) VALUES (%s, %s, 'Pending')"
    cursor.execute(query, (isbn, user_email))
    db.commit()

    return redirect('/reserve')

@app.route('/reserve')
def reserve():
    # Fetch pending reservation requests
    query = """
        SELECT b.book_name, b.author, r.isbn, r.user_email
        FROM reservations r
        JOIN books b ON r.isbn = b.isbn
        WHERE r.status = 'Pending'
    """
    cursor.execute(query)
    reservations = cursor.fetchall()
    return render_template('reserve.html', reservations=reservations)

@app.route('/approve_reservation', methods=['POST'])
def approve_reservation():
    isbn = request.form['isbn']
    user_email = request.form['user_email']

    # Update the reservation status to 'Approved' and mark the book as unavailable
    query1 = "UPDATE reservations SET status = 'Approved' WHERE isbn = %s AND user_email = %s"
    query2 = "UPDATE books SET availability = 0 WHERE isbn = %s"
    cursor.execute(query1, (isbn, user_email))
    cursor.execute(query2, (isbn,))
    db.commit()

    return redirect('/reserve')

@app.route('/reject_reservation', methods=['POST'])
def reject_reservation():
    isbn = request.form['isbn']
    user_email = request.form['user_email']

    # Remove the reservation request
    query = "DELETE FROM reservations WHERE isbn = %s AND user_email = %s"
    cursor.execute(query, (isbn, user_email))
    db.commit()

    return redirect('/reserve')

if __name__ == '__main__':
    app.run(debug=True)
