from flask import Flask, render_template, request 
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def questions():
    prompts = story.prompts
    return render_template('question.html', prompts=prompts)

@app.route('/story')
def story_reader():
    
    text = story.generate(request.args)

    return render_template('stories.html', text=text)