import random
action = ["Avengers: Endgame", "Black Panther", "Captain Marvel","Spiderman: Homecoming","Thor: Ragnarok","Guardians of the Galaxy","Wonder Woman","Avatar"]
mystery = ["Us","Zodiac","Sherlock Holmes","10 Cloverfield Lane","Murder on the Orient Express","Wind River","Arrival","Aurora Teagarden Mystery: A Bone to Pick"]
horror = ["Annabelle Comes Home","A Quiet Place","Child's Play","It","Halloween","The Witch","The Nun","The Conjuring"]
comedy = ["Game Night","Blockers","Step Brothers","Wedding Crashers","Super Bad","Tropic Thunder","Zombieland","The Hangaover"]
romcom = ["To All the Boys I Loved Before","The Holiday","The Proposal","Valentine's Day","The Ugly Truth","The Break-up","My Best Friend's Wedding","Clueless"]
animation = ["Toy Story 4","How to Train your Dragon: The Hidden World","Incredibles 2","Moana","Coco","Zootopia","Lego Movie 2","Up"]
scienFiction = ["Children of Men","The Martain","Inception","Edge of Tomorrow","Interstellar","Annihilation","Ex Machina","Gravity"]
documentary = ["13th","Apollo 11","Free Solo","Leaving Neverland","They Shall Not Grow Old","Fyre","Icarus","Blackfish"]
musical = ["The Greatest Showman","Aladdin","La La Land","A Star is Born","Mamma Mia!","Into the Woods","The Sound of Music","High School Musical"]
drama = ["The Aftermath","Spotlight","Boyhood","The Help","Gifted","Room","Call Me by Your Name","Moonlight"]
historicalFiction = ["Selma","Lincoln","12 Years as a Slave","The King's Speech","Kingdom of Heaven","Gladiator","Bridge of Spies","Troy"]
fantasy = ["Harry Potter","Doctor Strange","The Hobbit","Miss Peregrine's Home for Peculiar Children","Maleficent","Fantastic Beasts","Alice in Wonderland","Clash of the Titans"]

while True:
	print("Welcome to MovieLister. We have 12 genres: action, mystery, horror, comedy, romcom, animation, science fiction, documentary, musical, drama, historical fiction, and fantasy.\n")
	genre = raw_input("What type of genre of movies do you like to watch? Press 'q' to quit\n")
	if genre == "action":
		for x in action:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "mystery":
		for x in mystery:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "horror":
		for x in horror:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "comedy":
		for x in comedy:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "romcom":
		for x in romcom:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "animation":
		for x in animation:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "science fiction":
		for x in scienceFiction:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "documentary":
		for x in documentary:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "musical":
		for x in musical:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "drama":
		for x in drama:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "historical fiction":
		for x in histricalFiction:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == "fantasy":
		for x in fantasy:
			print(x)
			ask = raw_input("Would you like to see this movie? y/n\n")
			if ask == 'y':
				break
	elif genre == 'q':
		break
	else:
		print("Not a genre option")