import http.client

#connection establish
conn = http.client.HTTPConnection("dummyjson.com")

# HTTP/HTTPS request
conn.request("GET", "/todos")

# Response
response = conn.getresponse()

# Response status code
print(response.status)

# Response header
print(response.headers)

# Response body
print(response.read())