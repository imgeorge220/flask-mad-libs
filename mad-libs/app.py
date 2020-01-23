from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories_list


app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)


@app.route('/')
def index():

    return render_template('index.html', story_list=stories_list)
    

@app.route('/inputs')
def input_words():
    """Form for creating madlibs"""
    story_choice = request.form
    import pdb; pdb.set_trace()
    for story in stories_list:
        if story.template == story_choice:
            my_story = story

    return render_template('form.html', story=my_story)


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