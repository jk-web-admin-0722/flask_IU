from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/iepriekseja')
def iepriekseja():
   return render_template('iepriekseja.html')

@app.route('/nakama')
def nakama():
   return render_template('nakama.html')

@app.route('/parametri')
def parametri():
    id = request.args.get('id')
    title = request.args.get('title')
    print("ID:", id)
    print("Title:", title)
    return "Param"

if __name__ == "__main__":
   app.run(debug = True)