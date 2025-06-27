import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get instance ID from event or use your hardcoded ID
    instance_id = event.get('instance_id', 'i-098c00fecc44e5634')
    
    try:
        response = ec2.terminate_instances(
            InstanceIds=[instance_id]  # Fixed: removed quotes and added proper variable
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Instance terminated successfully',
                'instance_id': instance_id,  # Fixed: removed quotes, added proper variable
                'current_state': response['TerminatingInstances'][0]['CurrentState']['Name']
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }