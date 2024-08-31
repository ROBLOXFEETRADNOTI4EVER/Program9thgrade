import subprocess

def is_spotify_installed():
    try:
        subprocess.run(['which', 'spotify'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def open_spotify():
    try:
        # Try directly running the spotify command
        subprocess.run(['spotify'], check=True)
    except FileNotFoundError:
        print("Spotify command not found. Trying alternative methods...")
        
        # Try using gio
        try:
            subprocess.run(['gio', 'open', 'spotify://'], check=True)
        except FileNotFoundError:
            print("gio command not found. Trying another alternative...")
            
            # Try opening the Spotify .desktop file
            try:
                subprocess.run(['xdg-open', '/usr/share/applications/spotify.desktop'], check=True)
            except FileNotFoundError:
                print("The Spotify desktop file was not found. Make sure Spotify is installed.")
            except Exception as e:
                print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred with gio: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if is_spotify_installed():
        print("Spotify is installed. Opening Spotify...")
        open_spotify()
    else:
        print("Spotify is not installed. Please install Spotify to use this script.")

if __name__ == "__main__":
    main()
