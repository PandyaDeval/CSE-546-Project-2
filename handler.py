import sys
import boto3
import os
import glob
import face_recognition
import pickle

db = boto3.client('dynamodb')

def lambda_handler(event,context):

    os.system("ffmpeg -i test_0.mp4 -r 1 /tmp/image-%3d.jpeg")
    response=""

    print(1)
    file = open('encoding','rb')
    encodings = pickle.load(file)
    file.close()
    result = False
    print(2)
    for x in glob.glob('/tmp/*.jpeg'):
        
        image = face_recognition.load_image_file(x)
        print(3)
        unknown = face_recognition.face_encodings(image)[0]
        print(4)
        for y in range(len(encodings['encoding'])):
            result = face_recognition.compare_faces([encodings['encoding'][y]], unknown)[0]
            print(result,y)
            if result:
                name = encodings['name'][y]
                #print(name)
                item = db.get_item(TableName='student_data', Key={'name':{'S': name}})
                major = item['Item']['major']['S']
                year = item['Item']['year']['S']
                print(name, major, year)
                return {"name": name, "major": major, "year": year}
            print(5)

    print()

    return {"name": name, "major": major, "year": year}
