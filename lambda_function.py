import base64
import boto3

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
    data = decode_base64(event['picture'].split(',')[1].encode('ascii'))
    rekognition = boto3.client('rekognition','eu-west-1')
    response = rekognition.detect_faces(Image={'Bytes':data},Attributes=['ALL'])
    return response