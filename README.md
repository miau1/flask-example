# Flask example

## [Install Flask](http://flask.pocoo.org/docs/1.0/installation/)

We will install Flask in a virtual environment to contain it.

Create a project folder and a virtual environment `venv`:

```
mkdir myproject
cd myproject
python3 -m venv venv
```

Activate the environment:

```
. venv/bin/activate
```

Install Flask:

```
pip install Flask
```

## Run this Flask example application

Make sure you are in your `myproject` directory.

Clone this git repository:

```
git clone https://github.com/miau1/flask-example
```

Set `FLASK_APP` variable:

```
export FLASK_APP=flaskdemo.py
```

Set development mode on:

```
export FLASK_ENV=development
```

Run the app:

```
flask run
```

Go to `localhost:5000` in you browser to see the website.
