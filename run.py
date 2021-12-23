import os
from spotify_part import SpotifyClient
def run():
    # print("f")
    # print(os.getenv('SPOTIFY_AUTH_TOKEN'))
    spotify_client=SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
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