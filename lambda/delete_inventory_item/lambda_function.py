import boto3
import json
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Inventory')

    if 'pathParameters' not in event or 'id' not in event['pathParameters']:
        return {
            'statusCode': 400,
            'body': json.dumps("Missing 'id' path parameter")
        }

    item_id = event['pathParameters']['id']

    # Look up the item first to get its location_id (required for composite key)
    result = table.query(
        KeyConditionExpression=Key('id').eq(item_id)
    )
    items = result.get('Items', [])
    if not items:
        return {
            'statusCode': 404,
            'body': json.dumps("Item not found")
        }

    location_id = int(items[0]['location_id'])  # ← pulled automatically

    try:
        table.delete_item(
            Key={
                'id': item_id,
                'location_id': location_id
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f"Item with ID {item_id} deleted successfully.")
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error deleting item: {str(e)}")
        }
