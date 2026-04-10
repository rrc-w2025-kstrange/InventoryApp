# Cloud-Based Inventory Application

## Overview

This inventory app consists of a DynamoDB table, API Gateway, and Lambda functions.
The user can interact with the application using Postman.
There is no web UI for this project.

## Code and Version Control

GitHub is used to manage Lambda function code and sample web application code.

## CI/CD (GitHub Actions)

GitHub Actions are used to implement basic CI/CD automation.
Workflows are triggered on specific events to:

- Automatically deploy function code to AWS Lambda
- Automatically deploy the sample web application code to AWS S3
- Automatically check (lint) the code for syntax and formatting issues
