# Notes

## Register

```
curl -X POST http://127.0.0.1:5000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
        "username": "skaricharla",
        "password": "skaricharla",
        "email": "ganeshkaricherla@gmail.com",
        "first_name": "Swamy",
        "last_name": "Karicharla"
  }'
```

## Login

```
curl -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "skaricharla",
    "password": "skaricharla"
  }'


  #
  {
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NDA1OTg2NSwianRpIjoiYzA5MzZkYWMtMDJkZS00NjFhLWJmZTktYTE4NDMyOTRlMmVjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY3ZjQzNjNkYmVmMzc4MDVmNGE3YjJhNyIsIm5iZiI6MTc0NDA1OTg2NSwiY3NyZiI6ImY5NTdiNDdiLWU5NGMtNDY2NS05MzZiLTY5ZTE1MjE0YTY1NSIsImV4cCI6MTc0NDA2MDc2NX0.ABOVhoAH1oYaJwbN_u4eGv9HZBjp0ciI_PFMbeJN9CA",
  "message": "Login successful",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NDA1OTg2NSwianRpIjoiMDM0NTJjMzctOTVkMC00YzhmLWIxZjMtMTU4NzI5MTVhYTg2IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiI2N2Y0MzYzZGJlZjM3ODA1ZjRhN2IyYTciLCJuYmYiOjE3NDQwNTk4NjUsImNzcmYiOiJhNDljYTdmZS00YzRlLTQ2OTktYmU1Zi0yMmRmMjUzOWVmNmIiLCJleHAiOjE3NDQ2NjQ2NjV9.6Khe2mdWz0QKc6IjxRcBo-8FEKT3ZsZcv6chyKXx8oU"
}
```

```
curl -X POST http://127.0.0.1:5000/api/projects/create \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0NDA1OTg2NSwianRpIjoiYzA5MzZkYWMtMDJkZS00NjFhLWJmZTktYTE4NDMyOTRlMmVjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjY3ZjQzNjNkYmVmMzc4MDVmNGE3YjJhNyIsIm5iZiI6MTc0NDA1OTg2NSwiY3NyZiI6ImY5NTdiNDdiLWU5NGMtNDY2NS05MzZiLTY5ZTE1MjE0YTY1NSIsImV4cCI6MTc0NDA2MDc2NX0.ABOVhoAH1oYaJwbN_u4eGv9HZBjp0ciI_PFMbeJN9CA' \
  -d '{
    "project_name": "Common Criteria",
    "visibility": "private"
  }'
```
