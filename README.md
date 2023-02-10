- 👋 Hi, I’m @Kelvin Hung, I am new to Github and wanna to share my software development experiences, please feel free to discuss.
- [¬º-°]¬ I’m interested in software development, data ETL and machine learning.
- ☁ ☁ I’m learning programming languages including NodeJS, Python, (non) SQL as well as some foundamental machine learning techniques. 

## Sample of python API server ##
After pulling the project, please run the following in sequences in terminal
** Remimber to install Dev Containers before testing **
- brew install pipenv (if you haven't install it yet)
- pipenv install
- pipenv shell
- pipenv run python app.py

## Server calling procedure ##
Step 1: To import the "Sample_api_call.postman_collection.json" under "postman_endpoint" into Postman
Step 2: In "body", add two keys which are "file" and "test_file", choose the cooresponding files from folder "dataset"
Step 3: In "headers", add key "token" of value "password"
Step 4: Click "Send" to call the sample API and get the responses 
Step 5 (optional): 
     5.1 Trigger endpoint "get_predicted_file" to get the training and testing reports OR 
     5.2 Open your browser to type "http://localhost:1001/api/v1/get_predicted_file" to get the reports