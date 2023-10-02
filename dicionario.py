playlist = {
    'title': 'capeta collection',
    'author': 'cruzp',
    'songs': [
        {'title': 'Naked City', 'artist':['Bonehead'], 'duration':2.42},
        {'title': 'Pirá, Pirá, Piro', 'artist':['Coração Melão','Hermes', 'Renato'], 'duration':2.06},
        {'title': 'I Talk to the Wind', 'artist':['King Crimson'], 'duration':6.06}
        ] 
}

total = 0
for song in playlist['songs']:
    total += song['duration']
print(total)
