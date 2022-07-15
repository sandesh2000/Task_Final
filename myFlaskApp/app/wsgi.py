from flask import Flask,render_template
import flask
import socket
version=flask.__version__
cont_id=socket.gethostname()

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",version=version,cont_id=cont_id)

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
