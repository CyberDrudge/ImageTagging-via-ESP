# ImageTagging-via-ESP
An Image Tagging Game based on ESP

**Setup Build Environment**

Create a virtual environment:

```virtualenv .```

Clone this repository:

```git clone <url>```

```cd ImageTagging-via-ESP```

Install requirements:

```pip install -r requirements.txt```

Create Migrations:

```python manage.py makemigrations```

```python manage.py migrate```

Load Questions and their Choices:

`python manage.py loaddata questions/fixtures/questions.json `

Create a superuser or Admin:

`python manage.py createsuperuser`



**Run Game**

```python manage.py runserver```

Open `localhost:8000` on your browser to view and play the game.

 
