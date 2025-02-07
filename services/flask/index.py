from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)

# Connexion à Redis
r = redis.StrictRedis(host=redis_host, port=redis_port, db=0, decode_responses=True)

@app.route('/')
def home():
    return "Bienvenue sur le site Flask connecté à Redis!"

@app.route('/set', methods=['POST'])
def set_key():
    # Récupérer la clé et la valeur depuis la requête
    key = request.json.get('key')
    value = request.json.get('value')

    if not key or not value:
        return jsonify({"error": "key and value are required"}), 400

    # Ajouter la clé et la valeur dans Redis
    r.set(key, value)
    return jsonify({"message": f"Key '{key}' set with value '{value}'"}), 200

@app.route('/get/<key>', methods=['GET'])
def get_key(key):
    # Récupérer la valeur d'une clé depuis Redis
    value = r.get(key)
    if value:
        return jsonify({"key": key, "value": value}), 200
    else:
        return jsonify({"error": f"Key '{key}' not found"}), 404

@app.route('/all', methods=['GET'])
def get_all_keys():
    # Récupérer toutes les clés présentes dans Redis
    keys = r.keys('*')
    return jsonify({"keys": keys}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
