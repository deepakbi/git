import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 2000,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
