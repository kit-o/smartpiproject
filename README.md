# smartpiproject
## How to download:
### A. Go to releases, then download the newest version.
### B. Use this code in the terminal with git.
```
git pull https://github.com/kit-o/smartpiproject.git
cd smartpiproject
python3 speak.py
```
## Push:
```
cd smartpiproject
git add .
git commit
git push -u orgin main
# May not work on devices other than kit-o Raspberry Pi (DEMO DEVICE)
```
## Install (RasPi):
Download the Raspberry Pi Imager from the official website.
Give it root permissions.
Select your model.
Install Raspberry Pi OS (Debian).
Once it is installed, boot your Raspberry Pi.
Ctrl + Alt + T
```
git pull https://github.com/kit-o/smartproject.git
cd smartpiproject
sudo apt install portaudio19-dev python3-dev libasound-dev espeak espeak
python3 -m venv ./.venv/
pip install -r requirements.txt
source ./.venv/bin/activate
```
NOTE: YOU MAY NEED TO INSTALL SPECIFIC THINGS TO YOUR RASPIOS. I WILL MAKE A LIST SOON.
