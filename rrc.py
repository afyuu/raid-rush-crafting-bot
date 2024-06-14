from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    if request.method == 'POST':
        try:
            # Get data from Roblox
            data = request.json

            # Prepare the payload for Discord webhook
            discord_data = {
                "content": "New data received from Roblox",
                "embeds": [
                    {
                        "title": "Roblox Data",
                        "description": str(data),
                        "color": 16711680  # Red color
                    }
                ]
            }

            # Send the data to the Discord webhook
            response = requests.post(DISCORD_WEBHOOK_URL, json=discord_data)

            if response.status_code == 204:
                return jsonify({'status': 'success'}), 200
            else:
                return jsonify({'status': 'failed', 'reason': response.text}), response.status_code
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    return jsonify({'status': 'invalid request method'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)