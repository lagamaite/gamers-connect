from flask import Flask, render_template    
import jinja2  
from player import Player

app = Flask(__name__)

@app.route("/")
def home():
    # Test player class
    p = Player("Lucy", "test@email.com", [None, None])
    print(p.name) # should print "Lucy" in terinal 

    # Test game class

    return render_template("index.html")
    
@app.route("/test")
def test():
    return "Test"
    
if __name__ == "__main__":
    app.run(debug=True)