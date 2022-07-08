import csv

from flask import Flask,render_template,request,url_for,redirect
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

def write_to_file(data):
    with open('databasetext.txt', mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer=csv.writer(database2, delimiter=',', quotechar ='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/<string:page_name>')
def dynamic_page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method=='POST':
        data= request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Error in receiving data.Try again!:("
    #return "form submitted successfully! Will get back you soon:)"