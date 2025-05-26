# 🧠 Wiki – CS50 Web Project 1

This is a Wikipedia-like online encyclopedia built with Django.

## 📚 Features

- View encyclopedia entries written in Markdown
- Convert and display Markdown content as HTML
- Search entries (exact and partial match)
- Create new entries with validation
- Edit existing entries
- Visit a random entry
- Delete entries

## ⚙️ Technologies Used

- Python 3
- Django
- Markdown2 (for Markdown-to-HTML conversion)
- HTML/CSS (Django templating)

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wiki.git
   cd wiki
2. Create and activate a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
4. Install dependencies
   ```bash
   pip install -r requirements.txt
6. Run the server
   ```bash
   python manage.py runserver
8. Visit the app at http://127.0.0.1:8000/.

## 📝 Notes
- Entries are stored as .md files in the /entries/ directory.
- Markdown is parsed and converted using the markdown2 library.
