import math
from flask import Flask, render_template, request
app=Flask(__name__)
# number1 = 0
# number2 = 0
# o=0
def calc():
  if o==1:
    global a
    a=(number1+number2)
  if o==2:
    a=(number1-number2)
  if o==3:
    a=(number1*number2)
  if o==4:
    a=(number1/number2)
  
@app.route('/', methods=['GET','POST'])
def main_route():
  if request.method=='POST':
    global number1
    number1 = int(request.form.get("num1"))
    global number2
    number2 = int(request.form.get("num2"))
    global o
    o=int(request.form.get('operation'))
    calc()
 
  return '''
  <html>
  <meta name= "keywords" content = "HTML, CSS"/>
  <style>
  body{background-color: grey}
  h1{color: white; font-family:Verdana;text-align:center;border-style:groove}
  h2{color: black; font-family:Verdana;text-align:center; border-style:groove}
  p{color: lime; font-family:Verdana;text-align:center; outline-style:groove}
  div1{color: lightgreen; font-family:Verdana;text-align:center}
  </style>
  <body>
  <h1>Welcome to my calculator website</h1>
  <h2>please enter 2 numbers and a operator</h2>
  <p>Operations: 1. addition 2. subtraction 3. multiplication 4. division</p>
  <br>
  <center><form method="POST">
  <div1>
  <label for="num1">First number:</label>
  <input type="text" id="num1" name="num1" class="num"><br>
  <label for="num2">Second number:</label>
  <input type="text" id="num2" name="num2" class="num"><br>
  <label for="o">Operation:</label>
  <input type="text" id="operation" name="operation" class="num"><br>
  <input type="submit" value="Submit">
  </div1>
  </form>
  <br>
  
  
  <center><img src='https://advisorsavvy.com/wp-content/uploads/2020/03/calculator.png' width="150" height="200">'''
@app.route('/sqr', methods=['GET',"POST"])
def sqr():
  if request.method=='POST':
    global a
    a = math.sqrt(int(request.form.get("sqr")))
  return '''
  <style>
   body{background-color:grey}
   div2{color:lightgreen; font-family:Verdana;text-align:center}
  </style>
  <center><form method="POST">
  <div2>
  <label for="sqr">Square Root:</label>
  <input type="text" id="sqr" name="sqr" class="sqr"><br>
  <input type="submit" value="Submit">
  </div2>
  </form>
  <center><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Nuvola_apps_edu_mathematics_blue-p.svg/1200px-Nuvola_apps_edu_mathematics_blue-p.svg.png' width="200" height="200">'''
@app.route('/result')
def result():
  return '''
  <style>
  body{background-color:white}
  h{color: grey;font-family:Verdana;text-align:center}
  </style>
  <h>'''+str(a)+'''</h1>
  '''


app.run(host="0.0.0.0")