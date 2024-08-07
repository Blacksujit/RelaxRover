from flask import Flask, request, jsonify, render_template
from bot_logic import handle_query, log_mood, get_mood_log, check_daily_in_check

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.json
        user_query = data.get('query', '')
        response = handle_query(user_query)
        return jsonify({
            "mistral": response.get('mistral', 'No response from Mistral'),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/log_mood', methods=['POST'])
def log_mood_route():
    try:
        data = request.json
        mood = data.get('mood', '')
        if mood:
            log_mood(mood)
            return jsonify({"message": "Mood logged successfully"})
        return jsonify({"error": "Mood is required"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_mood_log', methods=['GET'])
def get_mood_log_route():
    try:
        mood_log = get_mood_log()
        return jsonify({"mood_log": mood_log})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/daily_checkin', methods=['POST'])
def daily_checkin_route():
    try:
        check_in_status = check_daily_in_check()
        return jsonify({"checked_in": check_in_status})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=200)
