from time import time
from random import randint
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
from flask import Flask, send_from_directory, request
from flask_cors import CORS
from google.genai.types import Content, Part

from agent import runner, session_service

app = Flask(__name__)
CORS(app)

APP_NAME = "whos-bailey"


def generate_user_id_simple():
    """Simpler version: just concatenate timestamp and random number"""
    timestamp = int(time() * 1000)
    random_num = randint(1000, 9999)
    return f"{timestamp}{random_num}"

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/api/endpoint", methods=['POST'])
async def ask():
    data = request.get_json()
    text = data.get('text', '')

    user_id = generate_user_id_simple()

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=user_id,
    )

    responses = []

    for event in runner.run(
        user_id=user_id,
        session_id=user_id,
        new_message=Content(parts=[Part(text=text)], role="user")
    ):
        print(event.usage_metadata)
        if not event.content:
            continue

        for part in event.content.parts:
            if not part.text:
                continue

            responses.append(part.text)
    return "\n".join(responses)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8080,
    )
