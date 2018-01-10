import base64
import boto3
from PIL import Image
from io import BytesIO
from aws_secrets import BUCKET_NAME
import datetime
import json

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
    s3 = boto3.resource('s3')
    rekognition = boto3.client('rekognition','eu-west-1')
    filename = datetime.datetime.now().isoformat() + ".png"
    object = s3.Object(BUCKET_NAME, filename)
    object.put(Body=data)
    #object = s3.Object(BUCKET_NAME, "event_data_test")
    #object.put(Body=json.dumps(event))
    im = Image.open(BytesIO(data))    

    # run face recognition on data set
    rekognition = boto3.client('rekognition','eu-west-1')
    response = rekognition.detect_faces(Image={'Bytes':data},Attributes=['ALL'])

    # loop over recognized faces, extract face and return data url with response for displaying
    for idx, face in enumerate(response["FaceDetails"]):
        box = face["BoundingBox"]
        w,h = im.size
        faceImage = im.crop((box["Left"]*w, box["Top"]*h, (box["Left"]+box["Width"])*w, (box["Top"]+box["Height"])*h))
        # Writing image to string buffer for output to S3
        outBuffer = BytesIO()
        faceImage.save(outBuffer, "PNG")
        object = s3.Object(BUCKET_NAME, "faceid_"+str(idx)+"_"+filename)
        object.put(Body=outBuffer.getvalue())
        outdata = "image/png;base64," + base64.b64encode(outBuffer.getvalue()).decode()
        response["FaceDetails"][idx]["faceImage"] = outdata
        
    return response