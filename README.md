# BookArc Library Management System

BookArc is a Django-based web application for managing and exploring a library’s collection of books. Featuring user roles (Reader & Librarian), secure authentication, book searching, and book management capabilities.

---

## 🚀 Features

* **Homepage Display**: Show latest released books in a responsive card layout (cover image, title, author, genre, release date, rating).
* **User Authentication**: Sign up, log in, and log out.

  * **Sign Up**: Collect first name, last name, email, phone number, password, role selection (Reader or Librarian).
  * **Librarian Code**: Additional form field for Librarians to enter a 4-digit code.
* **Role-Based UI**:

  * Readers see a **Book Now** button on each book card.
  * Librarians additionally see an **Add Book** button to add new titles.
* **Search**: Search by book title, author name, or genre.
* **PostgreSQL**: Production-ready relational database.
* **Responsive Design**: Built with Bootstrap 5 for mobile-first layouts.

## 🛠️ Tech Stack

* **Backend**: Django 4.x
* **Database**: PostgreSQL
* **Storage**: Django’s built-in Media handling (Pillow for image uploads)
* **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript

## 🔧 Installation & Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/bookarc.git
   cd bookarc
   ```

2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**

   * Create a database named `bookarc_db`.
   * Update `bookarc/settings.py` with your DB credentials under the `DATABASES` setting.

5. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Navigate to `http://localhost:8000/` in your browser.

## 📁 Project Structure

```
bookarc/                 # Django project root
├── accounts/            # Custom user app (signup/login/logout)
├── books/               # Book management app
├── media/               # Uploaded book cover images
├── templates/           # Global templates directory
│   ├── accounts/        # Authentication templates
│   └── books/           # Book views templates
├── static/              # Static files (CSS, JS)
├── bookarc/             # Project settings & URLs
└── manage.py            # Django CLI
```

## 🎨 Usage

1. **Sign Up** as a Reader or Librarian.
2. **Log In** to access role-specific features.
3. **Browse** the homepage for the latest books.
4. **Search** for books by title, author, or genre.
5. **Book Now** (Readers) or **Add Book** (Librarians).

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/awesome-feature`).
3. Commit your changes (`git commit -m 'Add awesome feature'`).
4. Push to the branch (`git push origin feature/awesome-feature`).
5. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding!

*Built with ❤️ by the BookArc development team.*
