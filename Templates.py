from flask import Flask, render_template
app =Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user): # http://127.0.0.1:5000/hello/max
    return render_template('hello.html',name= user)
@app.route('/score')  #http://127.0.0.1:5000/score
def result():
    dict = {'phy':50,'che':60,'maths':70}

    return render_template('score.html', result = dict)

if __name__ == '__main__':
    app.run(debug = True)