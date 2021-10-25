import requests

class Client:
	def __init__(self, url):
		self.session = requests.Session()
		self.url = url
	def __del__(self):
		self.session.close()
	def set_header(self, header):
		self.session.headers.update(header)
	def get(self, path, query):
		full_path = self.url
		full_path += path
		request = self.session.get(full_path, params=query)
		if request.status_code != requests.codes.ok:
			return None
		return request

	def post(self, path, query):
		full_path = self.url
		full_path += path
		request = self.session.post(full_path, params=query)
		if request.status_code != requests.codes.ok:
			return None
		return request

client = Client("https://httpbin.org")
client.set_header({"user-agent": "test_client"})
response_1 = client.get(path="/get",query={"key_1":"value_1"})
print(response_1)
response_1 = client.post(path="/status/400",query={"key_2":"value_2"})
print(response_1)