import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    try:
        response = ec2.run_instances(
            ImageId='ami-05ffe3c48a9991133',  # Replace with your AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',  # Optional
            SecurityGroupIds=['sg-0448bbdf46e863a4d'],  # Replace with your security group
            SubnetId='subnet-0e0c7a7dea7bed927',  # Replace with your subnet
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'Lambda-Launched-Instance'
                        }
                    ]
                }
            ]
        )
        
        instance_id = response['Instances'][0]['InstanceId']
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Instance launched successfully',
                'instance_id': instance_id
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }