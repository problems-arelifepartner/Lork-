# Lork-
Public web 


# 1. Install Python (if not installed)
sudo apt update && sudo apt install python3 python3-pip -y  # Linux/WSL
brew install python  # macOS (using Homebrew)

# 2. Install Flask
pip3 install flask

# 3 clone into git 
 git clone https://github.com/problems-arelifepartner/Lork-

# 4. Run the Flask app
python3 app.py


# 5 Open a browser and navigate to:
 http://127.0.0.1:5000

 # 6 For network access (other devices):
  flask run --host=0.0.0.0 --port=5000


 # 7 Then use:
 http://[YOUR-COMPUTER-LOCAL-IP]:5000

 Find your IP via hostname -I on Linux/WSL or ipconfig on macOS).

 # Important
 Educational purposes only!

 Termux requires manual directory setup (templates/, static/).
 For public access, always use --host=0.0.0.0.
 To stop the server, press Ctrl+C in the terminal.
