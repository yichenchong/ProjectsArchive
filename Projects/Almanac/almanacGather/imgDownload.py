# import the necessary packages
import requests

def url_to_image(url,name):
	with open('img/{}.jpg'.format(name), 'wb') as handle:
		response = requests.get(url, stream=True)
		if not response.ok:
			print(response)
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)