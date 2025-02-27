from flask import Flask, url_for, request

app = Flask(__name__)  # create Flask application object

@app.route('/')  # assign this view function to '/' (i.e., the "root: of the web site)
def home():  # define the view function
    x = request.headers.get('Content-Accept')
    other_url = url_for("other")
    count_url = url_for("count", num=5)
    person_url = url_for("person", person_name="John")
    return f"""<h1>Hello, JPMC Flask world!</h1>
    <a href="{other_url}">Go to other page</a><br/>
    <a href="{count_url}">Go to count page</a><br/>
    <a href="{person_url}">Go to person page</a><br/>
    """ # return HTML for the page to display

@app.route('/<int:num>')
def count(num):
    home_url = url_for('home')
    python_str = "PYTHON! " * num
    return f"""
<h2>{python_str}</h2>
<a href="{home_url}">Go to home page</a>
    """

@app.route('/person/<person_name>')
def person(person_name):
    home_url = url_for('home')
    return f"""
<h2>Hello {person_name}</h2>
<a href="{home_url}">Go to home page</a>
    """

@app.route('/other')
def other():
    home_url = url_for('home')
    return f"""
<h2>This is the other page</h2>
<a href="{home_url}">Go to home page</a>
    """

if __name__ == '__main__':
    app.run(debug=True) # start the development server
