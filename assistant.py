import speech_recog
from take_notes import takeNote
from playsound import playsound

if __name__ == "__main__":

	greetingKeys = ["bulba", "booba", "hey", "hello"]
	goodbyeKeys = ["bye", "goodbye", "good", "night", "later"]
	notesKeys = ["notes","note", "list", "supermarket"]

	while True:
		query = speech_recog.speechRec()
		words = query.split(" ")

		#---Commands----
		for items in words:
			if items in greetingKeys:
				playsound("./sounds/saaar.mp3")
				break
							
			elif items in goodbyeKeys:
				playsound("./sounds/bulbasaur-sad.mp3")
				exit()

			elif items in notesKeys:
				takeNote()
				print("done")




			else: continue