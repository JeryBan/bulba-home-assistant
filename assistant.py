import speech_recog

if __name__ == "__main__":


	while True:
		query = speech_recog.speechRec().lower()

		#---Commands----
		if query == "stop":
			exit()
			
		elif query == ("bulba" or "hello bulba" or "bulta" or "booba" or "hey bulba" or "hey booba" or "hello booba"):
			print("bulbaaa")