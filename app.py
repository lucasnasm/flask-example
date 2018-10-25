from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/index/")
@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        recebe_senha = request.form['senha']
        if recebe_senha == 'lucas' and recebe_senha != None:
            return render_template('index.html', recebe='Bem vindo', info=True)
        else:
            return render_template('index.html', recebe='Senha invalida', info='True')
    else:
        return render_template('index.html', info=False)


app.run(debug=True)
