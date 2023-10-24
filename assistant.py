import speech_recog
from playsound import playsound

if __name__ == "__main__":

	greetingList = ["bulba", "booba", "hey", "hello"]
	goodbyeList = ["bye", "goodbye", "good", "night", "later"]

	while True:
		query = speech_recog.speechRec()
		words = query.split(" ")

		#---Commands----
		for items in words:
			if items in greetingList:
				playsound("./sounds/saaar.mp3")
				break
							
			elif items in goodbyeList:
				playsound("./sounds/bulbasaur-sad.mp3")
				exit()

			else: continue