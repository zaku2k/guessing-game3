from flask import request
from flask import Flask, render_template

app = Flask(__name__)

def guess(min, max):
    return round((max - min) / 2 + min)

@app.route('/zgadywanka', methods=['GET', 'POST'])
def zgadywanka():
    if request.method == 'GET':
        min = 0
        max = 1000
        return render_template("zgadywanka.html", guess=f'Czy jest to {guess(min, max)}?', min=min, max=max)
    else: #POST
        result = request.form['result']
        min = int(request.form['min'])
        max = int(request.form['max'])
        gss = guess(min, max)

        if result == 'Za dużo':
            max = gss
        elif result == 'Za mało':
            min = gss
        else:
            return render_template("zgadywanka.html", guess='Hurra!')
        return render_template("zgadywanka.html", guess=f'Czy jest to {guess(min, max)}?', min=min, max=max)

if __name__== "__main__":
    app.run(debug=True, port=5005)

