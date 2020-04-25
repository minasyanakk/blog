import requests
import os

class Message:
	def send_without_image(self,title,content,slug):
		requests.get('https://api.telegram.org/bot818972814:AAGYr2FqsEAzVqD5wk2GSaO_E8Ep4moX6Io/sendMessage?chat_id=@erikovich&text={}\n{}'.format(title,content))
	
	def send_with_image(self,title,content,cover,slug):
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		images_dir = os.path.join(BASE_DIR, 'media/')
		url = "https://api.telegram.org/bot818972814:AAGYr2FqsEAzVqD5wk2GSaO_E8Ep4moX6Io/sendPhoto";
		files = {'photo': open(images_dir+cover, 'rb')}
		data = {'chat_id' : "@erikovich",
				'caption':'{}\n\n{}\n\n '.format(title,content)}
		requests.post(url, files=files, data=data)