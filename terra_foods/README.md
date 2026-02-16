# Terra Foods - Fresh Organic Groceries Delivery

Terra Foods is a modern e-commerce platform for ordering fresh, organic groceries with AI-powered assistance and WhatsApp integration.

## Features

-  Browse fresh organic products (Vegetables, Fruits, Herbs, Spices, Oils)
-  AI Shopping Assistant (Coming Soon)
-  WhatsApp Order Integration (Coming Soon)
-  Shopping Cart & Checkout
-  Product Reviews
-  Mobile-Responsive Design
-  SEO Optimized

## Tech Stack

**Backend:**
- Django 5.0
- Django REST Framework
- PostgreSQL (Production) / SQLite (Development)
- Python 3.11+

**Frontend:**
- HTML5, CSS3, JavaScript
- Tailwind CSS
- Alpine.js

**Infrastructure:**
- Redis (Caching)
- Cloudflare (CDN)
- Celery (Background Tasks)

## Installation

### Prerequisites
- Python 3.11 or higher
- pip
- Virtual environment

### Setup

1. Clone the repository:
```bash
git clone https://github.com/dankwakye/terra-foods-website.git
cd terra-foods-website
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

Edit `.env` and add your secret keys.

5. Run migrations:
```bash
python manage.py migrate
```

6. Load sample data:
```bash
python manage.py load_simple_categories
python manage.py load_simple_products
```

7. Create superuser:
```bash
python manage.py createsuperuser
```

8. Run development server:
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## Project Structure
```
terra-foods-website/
├── terra_foods/          # Main project settings
├── products/             # Products app
├── orders/               # Orders app (Coming Soon)
├── ai_agent/             # AI Assistant (Coming Soon)
├── users/                # User management (Coming Soon)
├── templates/            # HTML templates
├── static/               # CSS, JS, Images
├── media/                # User uploads
└── manage.py
```

## Security

 **NEVER commit:**
- `.env` file
- `db.sqlite3`
- `media/` folder
- Secret keys or passwords

All sensitive data is stored in environment variables.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is proprietary and confidential.

## Contact

Terra Foods Team - info@terrafoods.com

Project Link: https://github.com/dankwakye/terra-foods-website