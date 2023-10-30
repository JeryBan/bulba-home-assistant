import requests
import mimetypes

# resp = requests.get("http://127.0.0.1:80/json", stream=True)

def pushMessage (message):
    requests.post("http://192.168.2.9/bulba-home-assistant",
        data=message.encode(encoding='utf-8'))

def pushFiles (path_to_file):
    content_type = mimetypes.guess_type(path_to_file)
    if content_type is None:
        content_type = "application/octet-stream"

    filename = path_to_file.split("/")    

    headers = {"Content-Type" : content_type[0],
               "Filename" : filename[-1]}

    response = requests.put("http://192.168.2.9/bulba-home-assistant",
        data=open(path_to_file, 'rb'),
        headers=headers)



