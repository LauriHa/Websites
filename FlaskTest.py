from flask import Flask, redirect, url_for, request
app = Flask(__name__)

#localhost:5000/
@app.route('/')
def MoveToTest():
    return redirect(url_for('Test')) #siirtyy Test funktiolle annettuun '@app.route' eli tässä tapauksessa 'localhost:5000/test'

#Test funktiolle annettu URL
@app.route('/test', methods=['GET', 'POST'])
def Test():
    #'/test' sivu aiheutti GET kutsun (esim. sivun lataus/päivitys)
    if (request.method == 'GET'):
        return """
        <!DOCTYPE html>
            <html>
                <body>
                    <h1>Tekstiä Headerissa</h1>
                    <form>
                        <label>Test field: <input type="text"></label>
                        <br><br>
                        <button type="submit">Nappula</button>
                    </form>
                </body>
            </html>
        """
    #'/test' sivu aiheutti POST kutsun (esim. nappulan painallus sivulla)
    elif (request.method == 'POST'):
        DoStuff()
    else:
        return ""

def DoStuff():
    print("Tässä voisi tapahtua juttuja 'serveripuolella'")

if __name__ == '__main__':
    app.run()
