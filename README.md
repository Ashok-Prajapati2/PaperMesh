# PaperMesh - E-commerce Website

## How to Run the Project

### Prerequisites
- Python 3.x installed
- Django installed
- Virtual environment (recommended)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Ashok-Prajapati2/PaperMesh
   cd PaperMesh
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the website:
   - Homepage: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

### Project Structure
- `PaperMesh/`: Main project directory
  - `settings.py`: Django settings
  - `urls.py`: Main URL routing
  - `views.py`: Main views handling
  - `wsgi.py`: WSGI configuration
  - `asgi.py`: ASGI configuration
- `manage.py`: Django management script

### Available Routes
- Homepage: `/`
- Contact: `/contact/`
- Electronics: `/electronic/`
- About Us: `/about-us/`
- Product Details: `/prodectdetals/`
- Category: `/category/`
