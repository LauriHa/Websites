from flask import Flask, redirect, url_for, request
app = Flask(__name__)

# IP:PORT/
@app.route('/')
def MoveToTest():
    # siirtyy Test funktiolle annettuun '@app.route' eli tässä tapauksessa 'localhost:5000/test'
    return redirect(url_for('Test'))

# Test funktiolle annettu URL ja käytettävissä olevat HTTP kutsut
@app.route('/test', methods=['GET', 'POST'])
def Test():
    # '/test' sivu aiheutti GET kutsun (esim. sivun lataus/päivitys)
    if (request.method == 'GET'):
        return """
        <!DOCTYPE html>
            <html>
                <body>
                    <h1>Tekstiä Headerissa</h1>
                    <form method="POST">
                        <label>Input1: <input type="text" name="input1"></label>
                        <br>
                        <label>Input2:
                        <input type="radio" name="input2" value="Kissa" checked>Kissa
                        <input type="radio" name="input2" value="Koira">Koira
                        </label>
                        <button type="submit">Nappula</button>
                    </form>
                </body>
            </html>
        """
    # '/test' sivu aiheutti POST kutsun (esim. yläpuolella luotu form,jonka method on 'POST' submitataan buttonilla)
    elif (request.method == 'POST'):
        return DoStuff(request)
    else:
        return ""

def DoStuff(request):
    print("Tässä voisi tapahtua juttuja 'serveripuolella'")
    # Palautetaan POST kutsussa tulleet arvot(text-inputissa syötetty teksti ja radio-inputissa valittua vastaava value)
    # html dokumentin formin sisällä olevien inputtien 'name' attribuutin mukaan.
    values = "Input1 oli: " + request.form.get('input1') + " ja Input2 oli: " + request.form.get('input2')
    return values

if __name__ == '__main__':
    # Tähän voi antaa IP:n ja portin missä pyörii. Default 127.0.0.1:5000
    app.run()
    # esim. oma IP
    # app.run(host = '123.123.123.123', port = 5001)
