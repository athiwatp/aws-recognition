import json
import base64
import boto3
import datetime
from aws_secrets import BUCKET_NAME

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodebytes(data)
    
def lambda_handler(event, context):
    # TODO implement
    #return decode_base64(event['picture'].split(',')[1])
    data = decode_base64(event['picture'].split(',')[1].encode('ascii'))
    s3 = boto3.resource('s3')
    rekognition = boto3.client('rekognition','eu-west-1')
    filename = datetime.datetime.now().isoformat() + ".png"
    object = s3.Object(BUCKET_NAME, filename)
    object.put(Body=data)
    response = rekognition.detect_faces(Image={'S3Object':{'Bucket':BUCKET_NAME,'Name':filename}},Attributes=['ALL'])
    return response