from flask import Flask, render_template, request, redirect
import random
import datetime

app = Flask(__name__)
li = ["rock", "paper", "scissors"]
c_in_post = []

def rps(u_in):
    c_in = random.choice(li)
    c_in_post.clear()
    c_in_post.append(c_in)
    go = ''
    if u_in == c_in:
        go = 'tie'
    elif u_in == "rock" and c_in == "paper":
        go = 'lose'
    elif u_in == "paper" and c_in == "scissors":
        go = 'lose'
    elif u_in == "scissors" and c_in == "rock":
        go = 'lose'
    elif u_in == "rock" and c_in == "scissors":
        go = 'win'
    elif u_in == "paper" and c_in == "rock":
        go = 'win'
    elif u_in == "scissors" and c_in == "paper":
        go = 'win'
    return go
fun = []


@app.route('/rock', methods=['get', 'post'])
def get_rock():
    fun.clear()
    fun.append('rock')
    return redirect('/result')


@app.route('/paper', methods=['get', 'post'])
def get_paper():
    fun.clear()
    fun.append('paper')
    return redirect('/result')


@app.route('/scissors', methods=['get', 'post'])
def get_scissors():
    fun.clear()
    fun.append('scissors')
    return redirect('/result')


@app.route('/', methods=['get', 'post'])
def hello_world():
    if request.method == 'POST':
        fun.clear()
        return redirect('/result')
    else:
         return render_template('index.html')



@app.route('/result', methods=['get', 'post'])
def result():
    hello = rps(fun[0])
    go = 'tie'
    if hello == 'tie':
        go = 'tie'
    elif hello == 'win':
        go = 'win'
    elif hello == 'lose':
        go = 'lose'
    if request.method == 'POST':
        bleh = request.form['retry']
        if bleh == 'retry':
            return redirect('/')
    return render_template('result.html', go=go, post=c_in_post[0])





if __name__ == '__main__':
    app.run(debug=True)
