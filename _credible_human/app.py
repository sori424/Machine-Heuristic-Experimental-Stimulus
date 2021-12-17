from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
       return render_template('index_final.html')
    
@app.route('/survey.html')
def survey():
       return render_template('survey.html')
    
@app.route('/login.html')
def login():
       return render_template('login.html')

@app.route('/loading.html')
def loading():
    return render_template('loading.html')

@app.route('/loading_human.html')
def loading_human():
    return render_template('loading_human.html')

@app.route('/columns.html')
def columns():
       return render_template('columns.html')
    
@app.route('/code.html')
def code():
    return render_template('code.html')
    
    
    
# video list
@app.route('/templates/videos/eth1.html')
def eth1():
       return render_template('./videos/eth1.html')

@app.route('/templates/videos/eth2.html')
def eth2():
       return render_template('./videos/eth2.html')

@app.route('/templates/videos/eth3.html')
def eth3():
       return render_template('./videos/eth3.html')
    
@app.route('/templates/videos/eth4.html')
def eth4():
       return render_template('./videos/eth4.html')
    
@app.route('/templates/videos/eth5.html')
def eth5():
       return render_template('./videos/eth5.html')
    
@app.route('/templates/videos/eth6.html')
def eth6():
       return render_template('./videos/eth6.html')

@app.route('/templates/videos/eth7.html')
def eth7():
       return render_template('./videos/eth7.html')    

    
@app.route('/templates/videos/non1.html')
def non1():
       return render_template('./videos/non1.html')
    
@app.route('/templates/videos/non2.html')
def non2():
       return render_template('./videos/non2.html')
        
@app.route('/templates/videos/non3.html')
def non3():
       return render_template('./videos/non3.html')
        
@app.route('/templates/videos/non4.html')
def non4():
       return render_template('./videos/non4.html')
        
@app.route('/templates/videos/non5.html')
def non5():
       return render_template('./videos/non5.html')

@app.route('/templates/videos/non6.html')
def non6():
       return render_template('./videos/non6.html')

@app.route('/templates/videos/non7.html')
def non7():
       return render_template('./videos/non7.html')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, port='5000',debug=True)