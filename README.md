Just some notes from google API quick start guide on how to use python to send emails from my own gmail account

1) Use google API console to generate `client_secret.json`.

2) With `client_secret.json`, run `get_credentials.py` to generate a token for a specific scope. This token is stored as a pickle file.

3) `send_gmail.py` reads this token pickle file to call gmail API to send email.
