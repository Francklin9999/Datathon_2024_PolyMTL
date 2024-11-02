import boto3
import json

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="uswest-2",
    aws_access_key_id="your_access_key_id",
    aws_secret_access_key="your_secret_access_key"
)

prompt = "Can you see this message"

body = json.dumps({
    "prompt": prompt,
    "max_tokens": 2048,
    "top_p": 0.8,
    "temperature": 0.7,
})

modelId = "anthropic.claude-3-sonnet-20240229-v1:0"

accept = "application/json"
contentType = "application/json"

response = bedrock.invoke_model(
    body=body,
    modelId=modelId,
    accept=accept,
    contentType=contentType,
)

print(json.loads(response.get('body').read()))