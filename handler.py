import sys
import boto3
import os
import glob
import face_recognition
import pickle
from urllib import parse

db = boto3.client('dynamodb')
s3 = boto3.client('s3')

input_bucket = "cloud-computing-project-input"
output_bucket = "cloud-computing-project-output"
table_name = "student_data"


def lambda_handler(event,context):

    print(event)
    print(context)

    key = parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print("Object uploaded in S3: ", key)
    
    print("Downloading ",key," from S3...")
    s3.download_file(input_bucket, key, "/tmp/"+key)
    
    print("Converting mp4 file to frames...")
    os.system("ffmpeg -i /tmp/"+key+" -r 1 /tmp/image-%3d.jpeg")
    # os.system("ffmpeg -i test_0.mp4 -r 1 /tmp/image-%3d.jpeg")
    response=""

    # print(1)
    file = open('encoding','rb')
    encodings = pickle.load(file)
    file.close()
    result = False
    # print(2)
    for x in glob.glob('/tmp/*.jpeg'):
        
        image = face_recognition.load_image_file(x)
        # print(3)
        unknown = face_recognition.face_encodings(image)[0]
        # print(4)
        for y in range(len(encodings['encoding'])):
            result = face_recognition.compare_faces([encodings['encoding'][y]], unknown)[0]
            #print(result,y)
            if result:
                name = encodings['name'][y]
                #print(name)
                item = db.get_item(TableName=table_name, Key={'name':{'S': name}})
                major = item['Item']['major']['S']
                year = item['Item']['year']['S']
                print(name, major, year)
                
                print("Putting results in S3")
                csv_file = key[:-4]+".csv"
                #f = open("/tmp/"+csv_file, "w")
                #f.write(name+","+major+","+year)
                #f.close()
                
                s3.put_object(Body=name+","+major+","+year, Bucket=output_bucket, Key=csv_file)
                return {"name": name, "major": major, "year": year}
            # print(5)

    return {"name": name, "major": major, "year": year}
