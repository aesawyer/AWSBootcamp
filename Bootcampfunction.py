import boto3
import os
import json
import io

def pullARN(lambdaclient):
    response = lambdaclient.get_function(
        FunctionName=(os.environ['Lambda_NAME']),
    )

    responseRaw = json.dumps(response)
    jsonResponse = json.loads(responseRaw)
    arnResponse = jsonResponse['Configuration']['FunctionArn']

    return arnResponse

def constructOutput(myBucket, LambdaARN):
    name = myBucket.split('-')
    stringRaw = ('Lambda ARN- ' + LambdaARN+ '\n\nCongratulations ' + name[0].capitalize() + ' on completing your lab!')
    body = (stringRaw)
    return body

def outputFile(s3client, myBucket, outputBody):
    s3client.put_object(
        Bucket=myBucket,
        Key='outputlog.txt',
        Body=outputBody #not outputing newlines
    )
    print(outputBody)

def main(event, context):
    s3client = boto3.client('s3')
    lambdaclient = boto3.client('lambda')
    myBucket = os.environ['S3_NAME']

    lambdaARN = pullARN(lambdaclient)
    outputBody = constructOutput(myBucket, lambdaARN)
    outputFile(s3client, myBucket, outputBody)

