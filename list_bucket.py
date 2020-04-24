import boto3

s3 = boto3.client('s3',aws_access_key_id='ACCESS_KEY',
                        aws_secret_access_key='SECRET_KEY')
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print('Bucket list %s' % buckets)
