# ImageTagging-via-ESP
An Image Tagging Game based on ESP

**Setup Build Environment**

Create a virtual environment:

```virtualenv .```

Clone this repository:

```git clone <url>```

Install requirements:

```pip install requirements.txt```

Create Migrations:

```python manage.py makemigrations```

```python manage.py migrate```

Load Questions and their Choices:

`python manage.py loaddata questions/fixtures/questions.json `


**Run Game**

```python manage.py runserver```

Open `localhost:8000` on your browser to view and play the game.

 