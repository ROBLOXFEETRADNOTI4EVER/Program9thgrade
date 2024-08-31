import subprocess
import os

# Change to the desired directory
print(os.getcwd())
os.chdir("/mnt/22C2BB19C2BAEFE1")
print(os.getcwd())



import subprocess

# Command to open Spotify desktop app
spotify_command = "spotify"

# Execute the command to open Spotify
subprocess.run([spotify_command])


import webbrowser

spotify_url = "https://open.spotify.com/"

# Specify the correct path to Firefox for your regular user
firefox_path = "/usr/bin/firefox"  # Adjust if necessary

# Register Firefox for the current user, without root privileges
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

# Open the URL in Firefox
webbrowser.get('firefox').open(spotify_url)
