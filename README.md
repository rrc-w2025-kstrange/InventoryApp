# Cloud based inventory application

### This inventory app consists of a DynamoDB table, API Gateway and Lambda functions. The user can interact with the inventory app using Postman, there is no web UI for this project.
GitHub is used to manage the lambda function code and sample web application code. Additionally, Github actions are used to implement some basic CI/CD automation.
GitHub actions are implemented on specific events, to automatically deploy function code to AWS Lambda, automatically deploy the sample web application code to AWS S3, and automatically check (lint) the code for syntax and formatting issues.
