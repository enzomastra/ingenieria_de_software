from flask import Blueprint, jsonify, request
from app.services.client_services import ClientService
from app.mapping.client_schema import ClientSchema
from werkzeug.security import check_password_hash

schema = ClientSchema()
client=Blueprint('client',__name__)    

@client.route('/', methods=['GET'])
def index():
    return {"message": "Client service is running"}, 200

@client.route('/client/login/', methods=['POST'])
def login_client():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    client = ClientService().find_by_email(email)
    if client is None:
        return {"error": "Client not found"}, 404
    if check_password_hash(client.password, password):
        return {"message": "Login successful"}, 200
    else:
        return {"error": "Incorrect password"}, 400

@client.route('/client/<string:client_id>', methods=['GET'])
def get_client(client_id):
    client = ClientService().find_by_id(client_id)
    return jsonify(schema.dump(client)), 200

@client.route('/client/email/<string:email>', methods=['GET'])
def get_client_by_email(email):
    client = ClientService().find_by_email(email)
    return jsonify(schema.dump(client)), 200

@client.route('/client/all', methods=['GET'])
def get_all_clients():
    clients = ClientService().find_all()
    return jsonify(schema.dump(clients, many=True)), 200

@client.route('/client/create', methods=['POST'])
def create_client():
    client = ClientService().create(schema.load(request.json))
    return {"client":schema.dump(client)}, 201

@client.route('/client/update/<string:client_id>', methods=['PUT'])
def update_client(client_id):
    updated_client = ClientService().update(schema.load(request.json), client_id)
    if updated_client is None:
        return {"error": "Client not found"}, 404
    else:
        return jsonify(schema.dump(updated_client)), 200

@client.route('/client/delete/<string:client_id>', methods=['DELETE'])
def delete_client(client_id):
    return jsonify(ClientService().delete(client_id)), 200