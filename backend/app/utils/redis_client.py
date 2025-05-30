import os
import redis
import json
from dotenv import load_dotenv

#This is the redis client. Used to store and cache messages from a session. And also reduce redundency when same query is asked more thn once.
load_dotenv() 

#connecting to redis cloud
redis_url = os.getenv("REDIS_URL")
if not redis_url:
    raise ValueError("REDIS_URL environment variable not set.")

redis_db = int(os.getenv("REDIS_DB_INDEX", 0)) 


try:
    redis_client = redis.Redis.from_url(redis_url, db=redis_db, decode_responses=True)
    print("Successfully connected to Redis")
except Exception as e:
    print(f"Error connecting to Redis: {e}")
    raise

#saving messages with sessionId as key 
def save_message(session_id: str, role: str, content: str):
    key = f"session:{session_id}"
    message = {"role": role, "content": content}
    try:
        redis_client.rpush(key, json.dumps(message))
        print(f"Message saved for session {session_id}")
    except Exception as e:
        print(f"Error saving message for session {session_id}: {e}")

#using caching to get the messages for a session Id.
def get_session_history(session_id: str):
    key = f"session:{session_id}"
    try:
        messages = redis_client.lrange(key, 0, -1)
        return [json.loads(m) for m in messages]
    except Exception as e:
        print(f"Error fetching session history for session {session_id}: {e}")
        return []

#deleting the chat associated with a particular sessionId
def clear_session(session_id: str):
    key = f"session:{session_id}"
    try:
        redis_client.delete(key)
        print(f"Session {session_id} cleared")
    except Exception as e:
        print(f"Error clearing session {session_id}: {e}")
