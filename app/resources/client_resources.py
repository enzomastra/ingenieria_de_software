from flask import Blueprint, jsonify, request
from app.mapping.client_schema import ClientSchema

schema = ClientSchema()
client=Blueprint('client',__name__)

@client.route('/', methods=['GET'])
def index():
    return {"message":"Client is running"}, 200

@client.route('/client/<string:client_id>', methods=['GET'])
def get_client(client_id):
    from app.services.client_services import ClientService
    client = ClientService().find_by_id(client_id)
    return jsonify(schema.dump(client)), 200

@client.route('/client/name/<string:email>', methods=['GET'])
def get_client_by_name(name):
    from app.services.client_services import ClientService
    client = ClientService().find_by_name(name)
    return jsonify(schema.dump(client)), 200

@client.route('/client/all', methods=['GET'])
def get_all_clients():
    from app.services.client_services import ClientService
    clients = ClientService().find_all()
    return jsonify(schema.dump(clients, many=True)), 200

@client.route('/client/create', methods=['POST'])
def create_client():
    from app.services.client_services import ClientService
    client = ClientService().create(schema.load(request.json))
    return {"client":schema.dump(client)}, 201

@client.route('/client/update/<string:client_id>', methods=['PUT'])
def update_client(client_id):
    from app.services.client_services import ClientService
    updated_client = ClientService().update(schema.load(request.json), client_id)
    if updated_client is None:
        return {"error": "Client not found"}, 404
    else:
        return jsonify(schema.dump(updated_client)), 200

@client.route('/client/delete/<string:client_id>', methods=['DELETE'])
def delete_client(client_id):
    from app.services.client_services import ClientService
    return jsonify(ClientService().delete(client_id)), 200