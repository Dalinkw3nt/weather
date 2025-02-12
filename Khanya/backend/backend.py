import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

inventory_table = dynamodb.Table("RetailEdgeInventory")
sales_table = dynamodb.Table("RetailEdgeSales")
sns_topic_arn = os.getenv("SNS_TOPIC_ARN")

def lambda_handler(event, context):
    body = json.loads(event['body'])
    sale_id = body['saleId']
    item_id = body['itemId']
    quantity = body['quantity']

    # Store sales transaction
    sales_table.put_item(Item={
        "saleId": sale_id,
        "itemId": item_id,
        "quantity": quantity
    })

    # Update inventory
    response = inventory_table.get_item(Key={"itemId": item_id})
    if 'Item' in response:
        stock = response['Item']['stock'] - quantity
        inventory_table.update_item(
            Key={"itemId": item_id},
            UpdateExpression="SET stock = :s",
            ExpressionAttributeValues={":s": stock}
        )

        # Trigger low-stock alert
        if stock < 5:
            sns.publish(
                TopicArn=sns_topic_arn,
                Message=f"Low stock alert for Item {item_id}. Only {stock} left."
            )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Sale recorded successfully!"})
    }

