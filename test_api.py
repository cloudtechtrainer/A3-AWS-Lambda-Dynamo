def lambda_handler(event, context):
    # Extract the HTTP method from the event object
    http_method = event['httpMethod']
    
    # Process the request based on the HTTP method
    if http_method == 'GET':
        response_body = {'message': 'This is a GET request'}
    elif http_method == 'POST':
        response_body = {'message': 'This is a POST request'}
    else:
        response_body = {'message': 'Unsupported HTTP method'}
    
    # Construct the response
    response = {
        'statusCode': 200,
        'body': response_body
    }
    
    return response
