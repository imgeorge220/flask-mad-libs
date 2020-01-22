from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """Form for creating madlibs"""

    return render_template('form.html', story=story)


@app.route('/story')
def shows_story():
    """Shows the madlib"""

    user_inputs = request.args
    story_text = story.generate(user_inputs)

    return render_template('story.html', text=story_text)

# import pdb 
# pdb.set_trace() - (python debugger)
# n + enter - (goes to next line)
# c + enter - (continue code)