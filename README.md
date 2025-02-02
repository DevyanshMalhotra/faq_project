# bharatfd-assessment
## Multilingual FAQ Django Project

### Installation

```bash
git clone https://github.com/DevyanshMalhotra/faq_project.git
cd faq_project
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

### Docker-Commands

```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
