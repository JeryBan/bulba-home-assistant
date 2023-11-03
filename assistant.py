import speech_recog
from take_notes import takeNote
from playsound import playsound
import ntfy

if __name__ == "__main__":

	greetingKeys = ["bulba", "booba", "hey", "hello"]
	goodbyeKeys = ["bye", "goodbye", "good", "night", "later"]
	notesKeys = ["notes", "note", "list", "supermarket"]

	while True:
		query = speech_recog.speechRec()
		words = query.split(" ")

		#---Commands----
		for items in words:
			if items in greetingKeys:
				playsound("./assets/sounds/saaar.mp3")
				ntfy.pushMessage('Heeyy!!')
				ntfy.pushFiles('./images/wave.jpg')
				break
							
			elif items in goodbyeKeys:
				playsound("./assets/sounds/bulbasaur-sad.mp3")
				ntfy.pushMessage("Ba byeee")
				exit()

			elif items in notesKeys:
				takeNote()
				print("done")
				ntfy.pushMessage("Your shopping list:")
				ntfy.pushFiles("./notes.txt")




			else: continue