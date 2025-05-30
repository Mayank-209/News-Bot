from flask import Blueprint, request, jsonify
import uuid
#This is the chat routes. Where the endpoints for the backend are
from app.utils.redis_client import save_message, get_session_history, clear_session
from app.services.rag_pipeline import generate_response  # You'll define this next

chat_bp = Blueprint("chat", __name__)

#When a new query is asked. This endoint is hit
@chat_bp.route("/message", methods=["POST"])
def handle_message():
    data = request.get_json()
    user_message = data.get("message")
    session_id = data.get("session_id") or str(uuid.uuid4())  # new session if none provided

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    
    save_message(session_id, "user", user_message)

    #bot response generated
    try:
        bot_response = generate_response(user_message)
    except Exception as e:
        bot_response = "Sorry, I had trouble processing that."
        print("RAG Error:", str(e))

    #saved to redis
    save_message(session_id, "bot", bot_response)

    
    history = get_session_history(session_id)

    return jsonify({
        "session_id": session_id,
        "response": bot_response,
        "history": history
    })

#endpoint to get history/chat of a particular session
@chat_bp.route("/history/<session_id>", methods=["GET"])
def get_history(session_id):
    history = get_session_history(session_id)
    return jsonify({
        "session_id": session_id,
        "history": history
    })

#endpoint to delete a chat.
@chat_bp.route("/clear/<session_id>", methods=["DELETE"])
def clear(session_id):

  
    clear_session(session_id)
    return jsonify({
        "message": f"Session {session_id} cleared."
    })
    
