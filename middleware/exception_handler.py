from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.
    custom_response = {'error': True, 'message': None, 'data': None, 'status_code': None}

    if response is not None:
        for key, value in response.data.items():
            if key != 'non_field_errors':
                message = key + ": " + value[0] if isinstance(value, str) is False else value
            else:
                message = value[0] if isinstance(value, str) is False else value

            custom_response['message'] = message
        custom_response['status_code'] = response.status_code

        response.data = custom_response
        # response.status_code = 200
    return response
