# bulba-home-assistant
A home assistant using the #1 pokemon in PokedeX as a frontman.

#-------------------------
# ntfy configuration guide
#-------------------------
Server setup

1.Pull the docker image. 

	sudo docker pull binwiederhier/ntfy

2.Configure /etc/ntfy/server.yml

	base-url: "https://ntfy.sh"
	listen-http: "127.0.0.1:80"
	attachment-cache-dir: "/var/cache/ntfy/attachments"

3.Run the container with the server.

	sudo docker run -p 80:80 -it binwiederhier/ntfy serve

4.Open 127.0.0.1:80 with your browser and create a topic.

5.Connect with a mobile app to http://192.168.x.x:80 (server/device local address) under the same topic.

6.Python code to post a message to the topic from the server.

	import requests

	requests.post("http://127.0.0.1/your-topic",
    	data="your-message-here".encode(encoding='utf-8'))

OPTIONAL: enable static local IPs for the server and your connected devices.

