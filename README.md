# Valorant Key Farmer
A 'kick-your-feet-up' way of getting yourself a closed beta Valorant key.

## Usage
This python project, when run, opens a chrome window with the [Twitch](https://twitch.tv)
directory of all of the current live streams that have the tag 'Drops Enabled'. The script automatically
redirects the webpage to the first live stream. Every x seconds, the script checks if the stream is still
live. If it is not, then the webpage is redirected back to the directory and another live stream is loaded.

## Why?
At the time I made this project, the only way to get yourself a closed beta key for the video game 'Valorant',
was to watch endless hours of Twitch live streams, and hope that you were lucky enough to get a 'drop' (key).
To save myself for checking the live stream's status every 10 minutes, I decided to make this little project,
which I could just run in the background.

## Setup

### Prerequisties
In order to run this project on your computer, you will need the following python packages installed:
```
Python 3.7
Selenium 3.141.0
```
### Installing
Run the following commands in your command prompt to install the prerequsitites listed above:
```
pip install selenium
```
## License
MIT - so feel free to do as you wish with this project.
