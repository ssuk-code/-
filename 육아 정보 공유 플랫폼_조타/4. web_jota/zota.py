from flask import Flask
app = Flask(__name__)

@app.route('/')
def main_page():
   return render_template('mainpage.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, debug = True)