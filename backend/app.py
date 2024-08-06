from flask import Flask, request, jsonify, render_template
from bot_logic import handle_query

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
        
        # Check if response has expected keys
        if not isinstance(response, dict):
            raise ValueError("Response from handle_query should be a dictionary.")
        
        return jsonify({
            "llama": response.get('llama', 'No response from LLaMA'),
            "chatgpt": response.get('chatgpt', 'No response from ChatGPT')
        })
    except Exception as e:
        # Print error details to the console
        print(f"Error processing query: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=200)
