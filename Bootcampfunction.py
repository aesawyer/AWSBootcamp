import boto3
import os

def constructOutput(myBucket, LambdaARN):
    name = myBucket.split('-')
    body = ('Lambda ARN- ' + LambdaARN + '\nS3 Bucket- ' + myBucket + '\nCongratulations ' + name[0].capitalize() + ' on completing your lab!')
    return body

def outputFile(s3client, myBucket, outputBody):
    s3client.put_object(
        Bucket=myBucket,
        Key='outputlog.txt',
        Body=outputBody  # not outputting newlines
    )
    print(outputBody)

def main(event, context):
    s3client = boto3.client('s3')
    myBucket = os.environ['S3_NAME']
    lambdaARN = context.invoked_function_arn

    outputBody = constructOutput(myBucket, lambdaARN)
    outputFile(s3client, myBucket, outputBody)