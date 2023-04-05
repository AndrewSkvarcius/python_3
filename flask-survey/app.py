from flask import Flask, request, render_template, redirect, flash, session, make_response
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys as surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


""" key names used to store things in session"""
RESPONSES_KEY = "responses"
CURRENT_KEY = "current_survey"

@app.route('/')
def survey_show():
    """Survey Selection"""
    return render_template('choice.html', surveys=surveys)

@app.route("/", methods=["POST"])
def choose_survey():
    survey_id = request.form["survey_code"]

    if request.cookies.get(f"completed_{survey_id}"):
        return render_template("already_fin.html")
    
    survey = surveys[survey_id]
    session[CURRENT_KEY] = survey_id

    return render_template("survey_home.html", survey=survey)



@app.route('/begin', methods=["POST"])
def survey_start():
    """Clear Session of responses """
    session[RESPONSES_KEY] = []

    return redirect("/questions/0")

@app.route("/answer", methods=["POST"])
def answer_question():
    """Saves response & redirects to next ? """

    """ Response Choice"""
    choice = request.form['answer']
    text = request.form.get("text", "")

    """Add Response to list in session"""
    responses = session[RESPONSES_KEY]
    responses.append({"choice":choice, "text": text})

    """ Add Response to session"""
    session[RESPONSES_KEY]= responses
    survey_code = session[CURRENT_KEY]
    survey = surveys[survey_code]
    
    """ They have finished survey"""
    if (len(responses) == len(survey.questions)):
        return redirect("/finished")

    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/questions/<int:qid>")
def show_question(qid):
    """"Show current question"""
    responses = session.get(RESPONSES_KEY)
    survey_code = session[CURRENT_KEY]
    survey = surveys[survey_code]

    if (responses is None):
        return redirect("/")

    if (len(responses)== len(survey.questions)):
        return redirect("/finished")

    if (len(responses) != qid):
        flash(f"Invalid qustion: {qid}. ")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]
    
    return render_template("question.html", question_num=qid, question=question)


@app.route("/finished")
def finished_survey():
    survey_id = session[CURRENT_KEY]
    survey = surveys[survey_id]
    responses = session[RESPONSES_KEY] 
    
    page = render_template("finished.html", survey=survey, responses=responses)

    response = make_response(page)
    response.set_cookie(f"completed_{survey_id}", "yes", max_age=60)
    return response