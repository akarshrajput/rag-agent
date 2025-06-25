from database.mongo import get_mongo_db

def get_clients():
    db = get_mongo_db()
    clients = []
    for client in db.clients.find():
        client['_id'] = str(client['_id'])
        clients.append(client)
    return clients

def add_client(data):
    db = get_mongo_db()
    result = db.clients.insert_one(data)
    return str(result.inserted_id)
