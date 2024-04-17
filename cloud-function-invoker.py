import urllib
import google.auth.transport.requests
import google.oauth2.credentials
import google.oauth2.id_token

# Ensure env var GOOGLE_APPLICATION_CREDENTIALS with the service account file path
# replace <project> and <function> with your gcp project and function names
ENDPOINT = "https://<project>.cloudfunctions.net/<function>"
AUDIENCE = "https://<project>.cloudfunctions.net/<function>"

# Auth
auth_req = google.auth.transport.requests.Request()
id_token = google.oauth2.id_token.fetch_id_token(auth_req, AUDIENCE)

# Request
req = urllib.request.Request(ENDPOINT)
req.add_header("Authorization", f"Bearer {id_token}")
req.add_header("Content-Type", "application/json")
response = urllib.request.urlopen(req)
result = response.read().decode("utf-8")

print(result)
