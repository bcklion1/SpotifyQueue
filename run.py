# import os
from spotify_part import SpotifyClient
def run():
    # print("f")
    spotify_client=SpotifyClient("BQBGiIXvzuqZ67mrBKy2Bo83dQzlTTnpAkxoCkLOJ61VtuRlBaZTHUDtmo-8Xl9TK0sHMn50frvd_GmOqWg7bMlpsNnAnNuCH1SFTXCbPYDsF9cp44aVrJ5EbeSlSB2aCUMVYnX4h3ZvbzMs")
    choice=str(input("Song name: "))
    artist=str(input("Artist's name: "))
    if not artist.isspace() and artist:
        artist=spotify_client.searchArtist(artist)
    # print(artist)
    id, title, artist= spotify_client.searchSong(choice,artist)
    print(f"You want to queue {title} by {artist}?")
    yn=input()
    if yn and yn[0].lower()=="y":
        print(f"Queuing {title} by {artist}")
        spotify_client.addToQueue(id)
    # print(id)
    # print(title)
    # print(artist)
    

if __name__=="__main__":
    run()