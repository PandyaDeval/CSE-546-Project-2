# CSE 546: Cloud Computing Project-2
Video Processing using AWS Lambda


Group members:
 - Deval Pandya - 1225424200
 - Karthik Ravi Kumar - 1225910467
 - Tirth Hihoriya - 1225413475 
 

<hr>

SQS queue names: `RequestQueue` and `ResponseQueue`

S3 bucket names: `cc-project-input` and `cc-project-output`

<hr>

## Member Tasks
### Deval Pandya - (ASU ID: 1225424200)
 - I worked on setting up the aws environment and all the required resources for the project. I set up the IAM roles required to run lambda function. I set up the ECR repository for the lambda function. I set up the DynamoDB and added the data from student_data.json to the table. I set up the S3 buckets for input and output. Also configured all these resources to work with each other without any delays or authorization problems. 
 - My other task was to create a docker image for the lambda function. I used an EC2 container to pull the required base image. I installed all the necessary libraries on the image, copied the necessary files and made the docker image Lambda compatible. 


### Karthik – (ASU ID: 1225910467).
 - I worked on the implementation and testing of the `handler.py` file. What should happen when the lambda function is called is decided by this script. I worked on preloading data into DynamoDB as key-value pairs, where the primary key is the person's name and the value includes details like the person's graduation year, major, and image name. I also worked on establishing a connection between DynamoDB and the handler function, determining what occurs when the lambda function is called. The face recognition functions are also made to be called by this function. After facial recognition was completed, I retrieved the results from the database to display them as a result.
 - I also tested the code robustly from start to finish which includes extracting the frames, calling the lambda function, encoding using face_recognition, and comparison of the encodings. I made numerous improvements while the code was being tested to make sure the flow was smooth from beginning to end.



### Tirth Hihoriya  -  (ASU ID: 1225413475 )
 - I have designed the App-Tier. The app-tier includes basic image classification program. It receives a task from the RequestQueue and processes it. Once it is done with processing, it sends the output to the Response Queue. It also stores the input in input-bucket and output in output-bucket. If no new task comes to it, it waits for 5 seconds. I have tested the app-tier code rigorously and updated it to have more robust code. In the code there are many points where there is a chance of exceptions. These exceptions may occur due to reasons such as, the code might not get a message from RequestQueue, the input and output might not be stored in S3 buckets successfully, the message form RequestQueue might not be deleted successfully after it gets processed, etc. Thus, to handle it the code is taken care of with the ‘try-except’ block. If any exception occurs then it will wait for 5 seconds and will try to process again.
 
 <hr>
 
### Video for full working project

- https://drive.google.com/file/d/16HHFmE9EIs7-6mGU2nXmNU5jHhu58Cqd

Login with your ASU id to see it.
