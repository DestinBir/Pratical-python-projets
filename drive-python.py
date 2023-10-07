from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
auth_url = gauth.GetAuthUrl() # Create authentication url user needs to visit
code = AskUserToVisitLinkAndGiveCode(auth_url) # Your customized authentication flow
gauth.Auth(code) # Authorize and build service from the code