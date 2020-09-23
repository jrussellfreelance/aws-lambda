# pip install validate_email
# pip install pyDNS
from validate_email import validate_email

# basic
is_valid = validate_email('example@example.com')

# check for smtp server
is_valid2 = validate_email('example@example.com',check_mx=True)

# verify email exists
is_valid3 = validate_email('example@example.com',verify=True)