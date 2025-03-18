from db.execute import execute_query

def generate_tables():
    # laudo table
    execute_query('''CREATE TABLE IF NOT EXISTS laudo (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    study_iuid VARCHAR(250) NOT NULL)''')