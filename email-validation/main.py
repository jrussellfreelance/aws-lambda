from validate_email import validate_email

def handler(event, context):
    # assign email from lambda environment variable
    email = os.environ.get("email_address")

    is_valid = validate_email(email)

    return {
        'statusCode': 200,
        'body': json.dumps(is_valid)
    }
