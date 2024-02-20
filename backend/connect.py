import http.client

conn = http.client.HTTPSConnection("dev-bn071k2eety77tr7.us.auth0.com")

payload = "{\"client_id\":\"MzmtGe9NR5CfLaiDbzBHkYzGtrKKmVoN\",\"client_secret\":\"Hy-QPIS1gHfr1W_MVbXqsgUcQmp5BnPbe8oBB7ZGWQGObxfmv0y7gle2Kcp3RGGl\",\"audience\":\"https://dev-bn071k2eety77tr7.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))