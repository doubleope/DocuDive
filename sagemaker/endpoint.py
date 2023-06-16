import boto3
from sagemaker import get_execution_role
import time

sm_client = boto3.client(service_name='sagemaker')
runtime_sm_client = boto3.client(service_name='sagemaker-runtime')

account_id = boto3.client('sts').get_caller_identity()['Account']
region = boto3.Session().region_name

#not really used in this use case, use when need to store model artifacts (Ex: MME)
s3_bucket = 'models-for-demos'

role = "arn:aws:iam::617247433180:role/service-role/AmazonSageMaker-ExecutionRole-20230615T112868"

model_name = 'hermes-model-2'
model_url = "https://models-for-demos.s3.amazonaws.com/ggml-v3-13b-hermes-q5_1.bin" ## MODEL S3 URL
container = "617247433180.dkr.ecr.us-east-1.amazonaws.com/sagemaker-endpoint:latest"
instance_type = 'ml.p3.2xlarge'

print('Model name: ' + model_name)
print('Model data Url: ' + model_url)
print('Container image: ' + container)

container = {
    'Image': container
}

create_model_response = sm_client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = role,
    Containers = [container])

print("Model Arn: " + create_model_response['ModelArn'])

endpoint_config_name = 'hermes-model-config-2'
print('Endpoint config name: ' + endpoint_config_name)

create_endpoint_config_response = sm_client.create_endpoint_config(
    EndpointConfigName = endpoint_config_name,
    ProductionVariants=[{
        'InstanceType': instance_type,
        'InitialInstanceCount': 1,
        'InitialVariantWeight': 1,
        'ModelName': model_name,
        'VariantName': 'AllTraffic'}])

print("Endpoint config Arn: " + create_endpoint_config_response['EndpointConfigArn'])

endpoint_name = 'hermes-model-endpoint-2' 
print('Endpoint name: ' + endpoint_name)

create_endpoint_response = sm_client.create_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName=endpoint_config_name)
print('Endpoint Arn: ' + create_endpoint_response['EndpointArn'])

resp = sm_client.describe_endpoint(EndpointName=endpoint_name)
status = resp['EndpointStatus']
print("Endpoint Status: " + status)

print('Waiting for {} endpoint to be in service...'.format(endpoint_name))
waiter = sm_client.get_waiter('endpoint_in_service')
waiter.wait(EndpointName=endpoint_name)