from flask import Flask, render_template, request, redirect, url_for

#Initialize Flask instance
app = Flask(__name__)

example_data = [
    {"name": "Cat sleeping on a bed", "source": "cat.jpg"},
    {"name": "Misty forest", "source": "forest.jpg"},
    {"name": "Bonfire burning", "source": "fire.jpg"},
    {"name": "Old library", "source": "library.jpg"},
    {"name": "Sliced orange", "source": "orange.jpg"}
]

#Use "query" variable from the URL. If no variable is given,
#use empty string instead. GET and POST methods are allowed.
@app.route("/search", defaults={"query": ""}, methods=["GET", "POST"])
@app.route("/search/<query>", methods=["GET", "POST"])
def search(query):

    if request.method == "POST":
        #Get query from the POST form.
        query = request.form["query"]
        
        #Redirect to the same page with the query in the url.
        #ALWAYS REDIRECT AFTER POSTING!
        return redirect(url_for("search", query=query))

    matches = []

    #If an entry name contains the query, add the entry to matches.
    if query != "":
        for entry in example_data:
            if query.lower() in entry["name"].lower():
                matches.append(entry)
 
    #Render index.html with matches variable. 
    return render_template("index.html", matches=matches)

