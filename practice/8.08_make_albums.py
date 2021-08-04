#!/usr/bin/env python3

def make_album(name, album, song_count='') : 
    album = {'name' : name, 'album' : album }
    if song_count : 
        album['number_of_songs'] = song_count
    return album

while True : 
    print("\nPlease input the info about the album : ")
    print("input q to terminate any time")
    name = input('Singer : ')
    if name == 'q' : break
    album = input('Album : ')
    if album == 'q' : break
    print(make_album(name, album))




