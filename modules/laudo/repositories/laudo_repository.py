from db.execute import execute_query

def create_laudo_repository(data):    
    return execute_query('INSERT INTO laudo (study_iuid) VALUES (?)', params=(data['study_iuid'],))

def get_laudo_repository(study_iuid):
    return execute_query('SELECT * FROM laudo WHERE study_iuid = ?', params=(study_iuid,), fetch_one=True)

def delete_laudo_repository(study_iuid):
    return execute_query('DELETE FROM laudo WHERE study_iuid = ?', params=(study_iuid,))