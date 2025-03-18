from flask import jsonify
from modules.laudo.repositories.laudo_repository import create_laudo_repository, get_laudo_repository, delete_laudo_repository

def create_laudo_service(data):    
    if not data['study_iuid']:
        return jsonify({'error': 'Campo study_iuid em falta'}), 400

    try: 
        create_laudo_repository(data)
    except Exception as e:
        return jsonify({'error': f'Erro ao criar laudo: {str(e)}'}), 500
    
    return jsonify({'message': 'Item created successfully'}), 201

def get_laudo_service(study_iuid):
    try:
        return get_laudo_repository(study_iuid)
    except Exception as e:
        return jsonify({'error': f'Erro ao buscar laudo: {str(e)}'}), 500
    
def delete_laudo_service(study_iuid):
    try:
        delete_laudo_repository(study_iuid)
    except Exception as e:
        return jsonify({'error': f'Erro ao deletar laudo: {str(e)}'}), 500
    
    return jsonify({'message': 'Item deleted successfully'}), 200