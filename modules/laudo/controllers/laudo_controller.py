from flask import request, jsonify
from modules.laudo.services.laudo_service import create_laudo_service, get_laudo_service, delete_laudo_service

def initController(app):
    @app.route('/create', methods=['POST'])
    def create_laudo_controller():
        data = request.json
        print(data)
        
        create_laudo_service(data)
        
        return jsonify({'message': 'Laudo study_iuid salvo com sucesso'}), 201

    @app.route('/laudo/<study_iuid>', methods=['GET'])
    def get_laudo_controller(study_iuid):
        result = get_laudo_service(study_iuid)
        
        return result
    
    @app.route('/delete/<study_iuid>', methods=['DELETE'])
    def delete_laudo_controller(study_iuid):
        return delete_laudo_service(study_iuid)