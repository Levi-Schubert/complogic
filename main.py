songs = {
	("Say Anything", "Woe"),
	("Coheed and Cambria", "The Dark Sentencer"),
	("Nickelback", "Photograph"),
	("Charly Bliss", "Percolator"),
	("Mom Jeans", "Season 9 ep 2-3"),
	("Shinedown", "Devil"),
	("Nickelback", "Animals"),
	("Sorority Noise", "Fuschia"),
	("You, Me, and Everyone We Know", "Livin' Th' Dream")
}

good_songs = {song for song in songs if song[0] != "Nickelback"}

print(good_songs)