import json
from flask import Flask
import os
import locale
app = Flask(__name__)

@app.route("/")
def master():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "static", "index.html"
    )
    with open(file_path, "r") as file:
        return file.read()
    
@app.route("/api/<req>")
def api(req):
    if req == "blogs":
        json_path = os.path.join(
            os.path.dirname(__file__),
            "db", "blogs.json"
        )
        with open(json_path, "r", encoding="utf-8") as file:
            return file.read()
     
@app.route("/blog/<id>")
def blog(id):
    json_path = os.path.join(
        os.path.dirname(__file__),
        "db", "blogs.json"
    )
    with open(json_path, "r", encoding="utf-8") as file:
        dat = json.loads(file.read())
        print(dat)
        for i in dat["blogs"]:
            print(i["id"])
            if int(i["id"]) == int(id):
                print(i["title"])
                return '''
                    <head>
                    <style>
                        body {
                            font-family: Helvetica, Arial, Sans-Serif;
                            background-color: #000;
                            color: #fff;
                        }
                        #blogs div {
                            border: 1px dashed #fff;
                            border-radius: 8px;
                            padding: 1rem;
                            cursor: pointer;
                        }
                        #blogs div:hover {
                            background: #545454;
                        }
                    </style>
                ''' + f'''
                    <title>{i["title"]}</title>
                    </head>
                    <body style=" padding: 3rem; ">
                    <h1>{i["title"]}</h1>
                    <small>
                        {i["date"]}
                    </small><br><br>
                    <article>
                        {i["text"]}
                    </article>
                    </body>
                '''

@app.errorhandler(404)
def not_found(err):
    return f'''
        <h1>404 Not Found</h1>
        <p>{err}</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
