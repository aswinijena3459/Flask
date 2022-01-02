from flask import Flask #importing required libraries and mentioning them simulataneously in the requirements.txt

app=Flask(__name__) #wsgi app which will interact with the server and the web app we are trying to create

@app.route('/')#specifying url to visit
## whenever i am going to visit this page ...welcome fuction will be triggered automatically
def welcome():
    return 'Hello world'


@app.route('/kingfisher')
def ola():
    return 'say welcome to good times'


if __name__=="__main__":
    app.run(debug=True)