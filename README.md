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

Clone this git repository:

```
git clone https://github.com/miau1/flask-example
```

Run the app:

```
python3 flaskdemo.py
```

Go to `localhost:5000/search` in your browser to see the website. To run the app in a different port, change the last line of `flaskdemo.py` before running the app, for example:

```
app.run(port=8000)
```

And go to `localhost:8000/search`.
