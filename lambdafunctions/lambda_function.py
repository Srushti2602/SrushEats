import json
import boto3

def lambda_handler(event, context):
  lexClient = boto3.client('lex-runtime')
  lexResponse = lexClient.post_text(
      botName='SrushEats',
      botAlias='Food',
      userId='id',
      inputText=event['messages'][0]['unstructured']['text']
    )
  response = {
    "messages": [
      {
        "type": "unstructured",
        "unstructured": {
          "id": 1,
          "text": lexResponse['message'],
          "timestamp": "10-08-2021"
        }
      }
    ]
  }
  return response