# bulba-home-assistant
A home assistant using the #1 pokemon in PokedeX as a frontman.


### ntfy configuration guide / server setup
------------------------------------------

1.Pull the docker image. 

	sudo docker pull binwiederhier/ntfy

2.Configure /etc/ntfy/server.yml

	base-url: "http://http://192.168.x.x"
	listen-http: ":80"
	attachment-cache-dir: "/var/cache/ntfy/attachments"

3.Create the docker container of the ntfy server.

	sudo docker run -d --name container_name -v /var/cache/ntfy:/var/cache/ntfy -v /etc/ntfy:/etc/ntfy -p 80:80 -it binwiederhier/ntfy serve --cache-file /var/cache/ntfy/cache.db

4.Open 192.168.x.x with your browser and create a topic.

5.Connect with a mobile app to http://192.168.x.x:80 (server/device local address) under the same topic.

6.Python code to post a message to the topic from the server.

	import requests

	requests.post("http://192.168.x.x/your-topic",
    	data="your-message-here".encode(encoding='utf-8'))

OPTIONAL: enable static local IPs for the server and your connected devices.

