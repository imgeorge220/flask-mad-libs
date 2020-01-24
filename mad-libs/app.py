from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories_list


app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """Form to choose your story"""

    return render_template('index.html', story_list=stories_list)


@app.route('/', methods=["POST"])
def input_words():
    """Once story is chosen, creates form for creating madlibs"""

    story_choice = request.form.get('story')
    prompts = stories_list[int(story_choice)].prompts
    my_story = stories_list[int(story_choice)].template

    return render_template('form.html', story=my_story, prompts=prompts)


@app.route('/story')
def shows_story():
    """Shows the madlib"""

    user_inputs = request.form.get('story')
    story_choice = request.form.get('story')

    breakpoint()
    
    story_text = stories_list[int(story_choice)].generate(user_inputs)

    return render_template('story.html', text=story_text)


# import pdb 
# pdb.set_trace() - (python debugger)
# n + enter - (goes to next line)
# c + enter - (continue code)