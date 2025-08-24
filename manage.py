from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def start():
          return render_template('pontos.html')
@app.route('/aumentart1',methods=['POST'])
def cont():
        time1=request.form.get('time1')
        time2=request.form.get('time2')
        if time1>time2:
                return render_template('time1.html')
        if time2>time1:
                return render_template('time2.html')
        if time2==time1:
                return render_template('empate.html')
if __name__=='__main__':
        app.run(debug=True)