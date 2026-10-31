"""Rule-based NFL play-type demonstration; not a trained model."""
import json


def predict(down: int, distance: int) -> dict:
    if not isinstance(down, int) or isinstance(down, bool) or not 1 <= down <= 4:
        raise ValueError('down must be an integer from 1 to 4')
    if not isinstance(distance, int) or isinstance(distance, bool) or not 1 <= distance <= 99:
        raise ValueError('distance must be an integer from 1 to 99')
    if down == 4:
        play = 'pass' if distance > 2 else 'run'
    elif distance >= 7:
        play = 'pass'
    elif distance <= 3:
        play = 'run'
    else:
        play = 'pass' if down == 3 else 'run'
    return {'prediction': play, 'down': down, 'distance': distance, 'model': 'rule-based-demo', 'disclaimer': 'Educational heuristic, not a trained ML prediction.'}


def handler(event, context):
    headers = {
        'content-type': 'application/json',
        'access-control-allow-origin': '*',
        'access-control-allow-methods': 'GET, OPTIONS',
        'access-control-allow-headers': 'content-type',
    }
    try:
        method = (event.get('requestContext', {}).get('http', {}).get('method') or 'GET').upper()
        if method == 'OPTIONS':
            return {'statusCode': 204, 'headers': headers, 'body': ''}
        if method != 'GET':
            return {'statusCode': 405, 'headers': headers, 'body': json.dumps({'error': 'GET only'})}
        params = event.get('queryStringParameters') or {}
        down = int(params.get('down', '1'))
        distance = int(params.get('distance', '10'))
        result = predict(down, distance)
        return {'statusCode': 200, 'headers': headers, 'body': json.dumps(result)}
    except (TypeError, ValueError) as exc:
        return {'statusCode': 400, 'headers': headers, 'body': json.dumps({'error': str(exc)})}


if __name__ == '__main__':
    print(json.dumps(handler({'queryStringParameters': {'down': '3', 'distance': '8'}}, None), indent=2))
