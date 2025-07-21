# showmap.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser, sys, pyperclip

address = input("Insert an address: ")

if len(sys.argv) > 1:
    # Get address from command line
    address = " ".join(sys.argv[1:])
else:
    # Get Address from clipboard
    address = pyperclip.paste()

# Open the webbrowser
webbrowser.open(f"https://www.openstreetmap.org/search?query={address}")

