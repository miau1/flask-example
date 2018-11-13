# Flask example

## [Install Flask](http://flask.pocoo.org/docs/1.0/installation/)

We will install Flask in a virtual environment to contain it.

Create a project folder and a virtual environment `demoenv`:

```
mkdir myproject
cd myproject
python3 -m venv demoenv
```

Activate the environment:

```
. demoenv/bin/activate
```

Install Flask:

```
pip install Flask
```

## Run this Flask example application

Make sure you are in your `myproject` directory.

Clone the git repository and move to that directory:

```
git clone https://github.com/miau1/flask-example
cd flask-example
```

Set the following environment variables:

Show flask which file to run:

```
export FLASK_APP=flaskdemo.py
```

Enable development environment to activate interactive debugger and reloader:

```
export FLASK_ENV=development
```

Set the port in which to run the application, e.g.:

```
export FLASK_RUN_PORT=8000
```

Run the app:

```
flask run
```

Go to `localhost:8000/search` in your browser to see the website.

