import sqlite3
import datetime
import json
import sqlite3

def format_values_to_dump(data):
    if not data:
        return None

    if isinstance(data, list) and len(data) > 1:
        result = []
        for row in data:
            if isinstance(row, sqlite3.Row):
                row_dict = dict(row)
                for key, value in row_dict.items():
                    if isinstance(value, datetime.datetime):
                        row_dict[key] = value.isoformat()
                    elif isinstance(value, bytes):
                        row_dict[key] = value.decode('utf-8')
                result.append(row_dict)
        return json.loads(json.dumps(result, default=str))
    elif isinstance(data, sqlite3.Row):
        row_dict = dict(data)
        for key, value in row_dict.items():
            if isinstance(value, datetime.datetime):
                row_dict[key] = value.isoformat()
            elif isinstance(value, bytes):
                row_dict[key] = value.decode('utf-8')
        return json.loads(json.dumps(row_dict, default=str))