**AWS Lambda Function for Basic Web Page Routing and Data Insertion**

This repository contains a simple AWS Lambda function implemented in Python that serves as a basic web page router and data inserter. The Lambda function handles both GET and POST HTTP methods to provide a contact us page and insert submitted form data into a DynamoDB table.

**Repository Contents:**

1. **Lambda Function Code (`lambda_function.py`):** This Python script defines the Lambda function. It includes the logic to route HTTP requests and perform data insertion.

2. **HTML Files (`contactus.html` and `confirm.html`):** These HTML files are used to generate the content of the web pages displayed to users. `contactus.html` displays the contact us page, while `confirm.html` confirms successful form submissions.

**Usage:**

1. **Create an AWS Lambda Function:**
   - Log in to your AWS Management Console.
   - Open the Lambda service.
   - Create a new function and choose "Python 3.x" as the runtime.
   - Upload the `lambda_function.py` file as the function code.

2. **Configure API Gateway:**
   - In the Lambda function settings, add a new trigger using "API Gateway" as the trigger type.
   - Configure the API Gateway settings, including creating a new API or using an existing one.

3. **Upload HTML Files to GitHub:**
   - Include the `contactus.html` and `confirm.html` files in your GitHub repository.

4. **Testing the Lambda Function:**
   - Obtain the API Gateway URL for your Lambda function.
   - Use tools like cURL, Postman, or a web browser to test:
     - Open the URL in a browser to test the GET method.
     - Send a POST request with form data to the URL to test the POST method.

**Note:**
- Replace placeholders in the code (e.g., DynamoDB table name) with actual resource names and configurations.
- Ensure proper IAM permissions for Lambda and DynamoDB.
- Make sure you have basic knowledge of AWS Lambda, API Gateway, and HTTP methods.
