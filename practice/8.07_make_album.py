#!/usr/bin/env python3

def make_album(name, album, song_count='') : 
    album = {'name' : name, 'album' : album }
    if song_count : 
        album['number_of_songs'] = song_count
    return album

print(make_album('jay chou', 'always fantacy'))
print(make_album('jj lin', '3419757'))
print(make_album('joy tsai', 'dance woman', '23'))


