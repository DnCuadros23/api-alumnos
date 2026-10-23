import boto3
import json

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    # Si no existe el alumno
    if 'Item' not in response:
        return {
            'statusCode': 404,
            'mensaje': 'Alumno no encontrado'
        }
    # Convierte Decimal a tipos normales para que se pueda devolver como json
    alumno = json.loads(json.dumps(response['Item'], default=str))
    # Salida (json)
    return {
        'statusCode': 200,
        'alumno': alumno
    }
