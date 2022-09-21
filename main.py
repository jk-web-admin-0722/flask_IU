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

@app.route('/saskaitit')
def saskaitit():
    sk1 = request.args.get('sk1')
    sk2 = request.args.get('sk2')
    # print("sk1", type(sk1))
    # print("sk2", type(sk2))
    if sk1 is not None and sk2 is not None:
        if sk1.isdigit() and sk2.isdigit():
            sum = int(sk1) + int(sk2)
            return f"Summa ir {sum}"
        else:
            return "Kāds no parametriem nav skaitlis!"
    else:
        return "Neatradu parametrus"

@app.route('/meklet')
def meklet():
    parametrs = request.args.get('vaicajums')
    rezultats = []
    if parametrs is not None:
        with open("titanic.csv", "r", encoding="utf-8") as f:
            for rindina in f.readlines():
                if parametrs in rindina:
                    rezultats.append(rindina)

    return rezultats

    #RECEPTES

@app.route('/receptes')
def receptes():
    return render_template('receptes.html')

@app.route('/vafeles')
def vafeles():
    return render_template('vafeles.html')

@app.route('/vrapi')
def vrapi():
    return render_template('vrapi.html')

if __name__ == "__main__":
   app.run(debug = True)