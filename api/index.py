from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Konfigurasi Supabase
url = os.environ.get("https://pnjygyusrduossxouvav.supabase.co")
key = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBuanlneXVzcmR1b3NzeG91dmF2Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3OTQzMDI2MCwiZXhwIjoyMDk1MDA2MjYwfQ.3wV66UBat1J_SPdbpuUlNIbPeb9lPwk1ragXkuftIKg")
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
