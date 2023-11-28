import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up Spotify credentials
client_id = "d"
client_secret = "c"
redirect_uri = "http://localhost:3000"
# Set up playlist links
playlist1_url = "https://open.spotify.com/playlist/6G5FJWsrvd570DF8tFs11g?si=defee89f96044895"
playlist2_url = "https://open.spotify.com/playlist/0WchyaRfUwaaO9vxP263IM?si=9af2e07926e04cdf"

# Create an instance of the spotipy.Spotify class
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Function to get the tracks of a playlist
def get_playlist_tracks(playlist_url):
    results = sp.playlist_tracks(playlist_url)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

# Get songs from the 1 playlist
playlist1_tracks = get_playlist_tracks(playlist1_url)
tracks1 = [track['track']['name'] for track in playlist1_tracks]

# Get songs from the 2 playlist
playlist2_tracks = get_playlist_tracks(playlist2_url)
tracks2 = [track['track']['name'] for track in playlist2_tracks]

# Find duplicate songs
duplicate_songs = set(tracks1) & set(tracks2)

""" # Print the duplicate songs
if duplicate_songs:
    print("Duplicate songs found:")
    for song in duplicate_songs:
        print(song)
else:
    print("No duplicate songs found.") """

# Save the duplicate songs to a text file
if duplicate_songs:
    with open("duplicate_songs.txt", "a") as file:
        file.write("Duplicate songs found:\n")
        for song in duplicate_songs:
            print(song, file)
    print("Duplicate songs saved to 'duplicate_songs.txt' file.")
else:
    print("No duplicate songs found.")
