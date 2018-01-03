# aws-rekognition

This is a small demo of a face rekognition application using AWS Rekognition and AWS Lambda.

A static web site uses WebRTCs getUserMedia function, currently not supported by Safari, to take a picture from the clients webcam. This picture is send to an AWS Lambda function via an Amazon Gateway API. This function stores the picture on Amazon S3 and calls the detect faces method of Amazon Rekognition on the S3 object. The result is sent back to the client, which marks detected faces with some additional information like gender, age and emotion.

## Screenshot
![Screenshot of demo](https://raw.githubusercontent.com/mbunse/aws-recognition/master/demo_screenshot.jpg)
