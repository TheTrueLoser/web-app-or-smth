from flask import Flask, session, request, render_template, redirect, url_for, jsonify
from random import randint
from main_db_controll import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/')
def index():
    """Display the main page and start a new quiz session."""
    max_quiz = 3
    session['quiz'] = randint(1, max_quiz)
    session['last_question'] = 0
    return render_template('main.html')

@app.route('/test', methods=['POST'])
def test():
    """Handle form submissions and update the database."""
    if request.method == 'POST':
        try:
            obj = request.form.to_dict()
            db.add_data(obj)
            info = db.get_data()
            return render_template('answer.html', data=info)
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": "Failed to process the data."}), 500

    return 'Only POST requests are allowed', 405

@app.route('/result')
def result():
    """Display a result page."""
    return "That's all folks!"

if __name__ == '__main__':
    app.run(debug=True)
