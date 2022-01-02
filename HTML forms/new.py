from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('results.html',result=res)
@app.route('/fail/<int:score>')
def fail(score):
    res = ''
    if score >= 50:
        res = 'PASS'
    else:
        res = 'FAIL'
    return render_template('results.html', result=res)

@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks>50:
        result='success'
    else :
        result='fail'
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['Science'])
        maths=float(request.form['Math'])
        c=float(request.form['C'])
        datascience=float(request.form['Data science'])
        total_score=(science+maths+c+datascience)/4
        res=''
        if total_score>=50:
            res='success'
        else:
            res='fail'
        return redirect(url_for(res,score=total_score))



if __name__==('__main__'):
    app.run(debug=True)