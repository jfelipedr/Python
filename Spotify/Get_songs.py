import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify credentials
client_id = "d"
client_secret = "c"
redirect_uri = "http://localhost:3000"
# Set up playlist links
playlist1_url = "https://open.spotify.com/playlist/6G5FJWsrvd570DF8tFs11g?si=c2e17b40be8f4f57" # Todo
playlist2_url = "https://open.spotify.com/playlist/2PcIEmIADTvPXA5qjTOGwS?si=c87b88341e734c4e" # i
playlist3_url = "https://open.spotify.com/playlist/0WchyaRfUwaaO9vxP263IM?si=9c8209e9135b48b8" # Ñ
playlist4_url = "https://open.spotify.com/playlist/0VjNF3hnG6OtcXpzlzfyhk?si=65652996477a4db3" # _
playlist5_url = "https://open.spotify.com/playlist/6MAJfAVipKQDvIMI2EiVdL?si=9350c68b18434ecb" # O

# Create an instance of the spotipy.Spotify class
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Function to get the tracks of a playlist
def get_playlist_tracks(playlist_url):
    results = sp.playlist_tracks(playlist_url)
    tracks = results["items"]
    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])
    return tracks

# Get songs from the 1 playlist
playlist1_tracks = get_playlist_tracks(playlist1_url)
tracks1 = [track["track"]["name"] for track in playlist1_tracks]

"""# Get songs from the 2 playlist
playlist2_tracks = get_playlist_tracks(playlist2_url)
tracks2 = [track["track"]["name"] for track in playlist2_tracks]"""

# Save the tracks of playlist 1 to a text file
if tracks1:
    with open("playlist1_tracks.txt", "a") as file:
        file.write("------------- Songs of Playlist 1: -------------\n")
        for song in tracks1:
            print(song, file)
    print("Playlist 1 tracks saved to 'playlist1_tracks.txt' file.")
else:
    print("No tracks found for Playlist 1.")

"""# Save the tracks of playlist 2 to a text file
if tracks2:
    with open("playlist2_tracks.txt", "w") as file:
        file.write("Songs of Playlist 2:\n")
        for song in tracks2:
            file.write(song + "\n")
    print("Playlist 2 tracks saved to 'playlist2_tracks.txt' file.")
else:
    print("No tracks found for Playlist 2.")"""
