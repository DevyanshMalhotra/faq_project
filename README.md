# bharatfd-assessment
## Multilingual FAQ Django Project

### Installation

```bash
git clone <repository-url>
cd faq_project
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

