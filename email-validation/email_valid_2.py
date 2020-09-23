# pip install email_validator

from email_validator import validate_email, EmailNotValidError

email = "my+address@mydomain.tld"

try:
  # Validate.
  valid = validate_email(email)

  # Update with the normalized form.
  email = valid.email
except EmailNotValidError as e:
  # email is not valid, exception message is human-readable
  print(str(e))