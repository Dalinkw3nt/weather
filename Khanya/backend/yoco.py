import json
import boto3
import os
import requests

YOCO_SECRET_KEY = os.getenv("YOCO_SECRET_KEY")
dynamodb = boto3.resource('dynamodb')
sales_table = dynamodb.Table("RetailEdgeSales")

def lambda_handler(event, context):
    body = json.loads(event['body'])
    token = body['token']
    sale_id = body['saleId']
    amount = body['amount']

    headers = {
        "Authorization": f"Bearer {YOCO_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "token": token,
        "amountInCents": amount * 100,
        "currency": "ZAR"
    }

    response = requests.post("https://online.yoco.com/v1/charges/", headers=headers, json=data)
    
    if response.status_code == 200:
        sales_table.put_item(Item={"saleId": sale_id, "amount": amount, "status": "Paid"})
        return {"statusCode": 200, "body": json.dumps({"message": "Payment successful!"})}
    else:
        return {"statusCode": 400, "body": json.dumps({"error": "Payment failed!"})}

