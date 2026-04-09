import json
import boto3
import uuid
from decimal import Decimal

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps("Bad request. Please provide the data.")
        }

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Inventory')

    unique_id = str(uuid.uuid4())

    try:
        table.put_item(
            Item={
                'id': unique_id,
                'name': data['name'],
                'description': data['description'],
                'qty': int(data['qty']),
                'price': Decimal(str(data['price'])),
                'location_id': int(data['location_id'])
            }
        )
        return {
            'statusCode': 201,
            'body': json.dumps(f"Item with ID {unique_id} added successfully.")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error adding item: {str(e)}")
        }
