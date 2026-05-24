from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Konfigurasi Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/api/tasks', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_tasks():
    # READ
    if request.method == 'GET':
        data = supabase.table("tasks").select("*").execute()
        return jsonify(data.data)

    # CREATE
    elif request.method == 'POST':
        item = request.json
        data = supabase.table("tasks").insert(item).execute()
        return jsonify(data.data), 201

    # UPDATE
    elif request.method == 'PUT':
        item = request.json
        data = supabase.table("tasks").update(item).eq("id", item['id']).execute()
        return jsonify(data.data)

    # DELETE
    elif request.method == 'DELETE':
        item_id = request.args.get('id')
        supabase.table("tasks").delete().eq("id", item_id).execute()
        return jsonify({"message": "Deleted"}), 200

if __name__ == '__main__':
    app.run()
