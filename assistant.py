import speech_recog, ntfyApp, webServer
from take_notes import takeNote
from playsound import playsound
from open_ai import casual_chat



greetingKeys = ["bulba", "booba", "hey", "hello"]
goodbyeKeys = ["bye", "goodbye", "good", "night", "later"]
notesKeys = ["notes", "note", "list", "supermarket"]
chatKeys = ["chat"]
webpageKeys = ["webpage", "homepage"]

while True:
	query = speech_recog.speechRec()
	words = query.split(" ")

	#---Commands----
	for items in words:
		if items in greetingKeys:
			playsound("./sounds/saaar.mp3")
			ntfy.pushMessage('Heeyy!!')
			ntfy.pushFiles('./images/wave.jpg')
			break
						
		elif items in goodbyeKeys:
			playsound("./sounds/bulbasaur-sad.mp3")
			ntfy.pushMessage("Ba byeee")
			exit()

		elif items in notesKeys:
			takeNote()
			print("done")
			ntfy.pushMessage("Your shopping list:")
			ntfy.pushFiles("./notes.txt")

		elif items in webpageKeys:
			webServer.homepage()



		else: continue