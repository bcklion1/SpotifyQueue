import requests
import urllib.parse

class SpotifyClient():
    def __init__(self,apiToken):
        self.apiToken=apiToken
        
    def searchArtist(self,artist):
        search=urllib.parse.quote(f"{artist}")
        # print(search)
        url= f'https://api.spotify.com/v1/search?q={search}&type=artist'
        response=requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.apiToken}"
            }
        )
        response_json = response.json()
        # print(response_json)
        results=response_json["artists"]["items"]
        if results:
            return (results[0]["name"])
    def _searchSong(self,searchurl):
        response=requests.get(
            searchurl,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.apiToken}"
            }
        )
        response_json = response.json()
        return response_json

    def searchSong(self,track,artist):
        search=urllib.parse.quote(f"{track} artist:{artist}")
        # print(search)
        url= f'https://api.spotify.com/v1/search?q={search}&type=track'
        response=self._searchSong(url)

        results=response["tracks"]["items"]
        if results:
            return (results[0]["id"],results[0]["name"],results[0]["artists"][0]["name"])

        else:
            search=urllib.parse.quote(f"{track}")
            # print(search)
            url= f'https://api.spotify.com/v1/search?q={search}&type=track'

            response=self._searchSong(url)

            results=response["tracks"]["items"]
            if results:
                for i in range(20):
                    for j in range(len(results[i]["artists"])):
                        if artist == (results[i]["artists"][j]["name"]):
                            return (results[i]["id"],results[i]["name"],results[i]["artists"][0]["name"])
            else:
                raise Exception("No results found")

    def addToQueue(self, id):
        print(id)
        url= f"https://api.spotify.com/v1/me/player/queue?uri=spotify%3Atrack%3A{id}"

        response=requests.post(
            url,
            # json={
            #     "ids":[id]
            # },
            # data=dat,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.apiToken}"
            }
        )
        print(response)

    def songNameAndArtist(self,id):
        url=f"https://api.spotify.com/v1/tracks/{id}"