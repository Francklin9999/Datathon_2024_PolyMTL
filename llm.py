import boto3
import json

bedrock = boto3.client(
  service_name='bedrock-runtime', 
  region_name="us-west-2"
)

prompt = """
Write a medium blog post on how to use 
Amazon Bedrock to write an article on how to use Bedrock.
"""

body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "prompt": prompt,
    "max_tokens": 1000,
    "temperature": 0.75,
    "p": 0.01,
    "k": 0,
})

modelId = 'anthropic.claude-3-sonnet-20240229-v1:0'
accept = 'application/json'
contentType = 'application/json'

response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())

print(response_body['generations'][0]['text'])