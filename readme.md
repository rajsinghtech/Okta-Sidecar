# Okta Sidecar Demo
## In this repo you will find everything you need to run a test application with Okta oauth2.

### Web Application
- `app.py` Flask webapp on port 8080
- `requirements.txt` Python Library`s
- `dockerfile` Image build

### Docker Compose
- `docker-compose.yaml`
- `.env`

### Navigate to [Okta Developer Sign On](https://developer.okta.com/)
1. Login
2. Applications > Create App Integration
3. Select OIDC & Web Application
4. Add a Sign-in redirect URIs `http://localhost:4180/oauth2/callback`
5. Create your `.env` file and set the appropriate values.
6. Run `docker compose up`

### Example `.env`
```
ISSUER=https://dev-xxxxx.okta.com/oauth2/default
CLIENT_ID=CLIENT_ID_HERE
CLIENT_SECRET=CLIENT_SECRET_HERE
OAUTH2_PROXY_COOKIE_SECRET=(Run command: openssl rand -base64 32)
```
