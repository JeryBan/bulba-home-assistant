import os
import speech_recog

def takeNote():
	returnKeys = ["thanks", "done", "finish", "ok"]

	while True:
		query = speech_recog.speechRec()
		words = query.split(" ")

		for items in words:
			if (items not in returnKeys) and (items != "none"):
				if os.path.isfile("./notes.txt"):
					with open("./notes.txt", "a") as file:
						notes = file.write(items + "\n")
				else:
					with open("./notes.txt", "w") as file:
						notes = file.write(items + "\n")
			elif items == "none":
				continue
			else:
				return 0

			
				
