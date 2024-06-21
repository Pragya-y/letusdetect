from flask import Flask
from flask import Flask, render_template,request,redirect, flash,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query
from datetime import date
from datetime import datetime
import firebase
import pyrebase
from urllib.request import Request, urlopen
import os
import urllib.request
import webbrowser  
import ast
import webbrowser
import json
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask
from flask_mail import Mail, Message


app=Flask(__name__)
app.secret_key = "super secret key"
firebaseConfig = {
  'apiKey': "AIzaSyD1sDC4lgTk9pi1mO5HZh-TfOgV00veBVA",
  "databaseURL" : "https://distemp-80405-default-rtdb.firebaseio.com/",
  'authDomain': "distemp-80405.firebaseapp.com",
  'projectId': "distemp-80405",
  'storageBucket': "distemp-80405.appspot.com",
  'messagingSenderId': "436787642429",
  'appId': "1:436787642429:web:6bd7220c7097868a2aaa54"
}

##########################
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'closesharedis@gmail.com'
app.config['MAIL_PASSWORD'] = 'dis@12345'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)







firebase = pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
db=firebase.database()
auth=firebase.auth()
# storage=firebase.storage()

global user_mail




@app.route("/",methods=["GET", "POST"])
def login():
    global user_mail

    
    if request.method == "POST":
        print('post')
        # print(request.form["email"])
        email = request.form["email"]
        password = request.form["password"]
      
   

        try:
           
            user=auth.sign_in_with_email_and_password(str(email),str(password))
            print(auth.current_user['email'])
            z=auth.get_account_info(user['idToken'])
            user_mail=z['users'][0]['email']
            
            # user_mail=email


           
            flash('Login sucessfully ', category='sucessful')
            
            return redirect('/aboutus')
        except:
           
            flash('Incorrect mail or password.', category='error')
            return render_template("login.html")
        
       

    return render_template("login.html")


@app.route('/aboutus')
def aboutus():
    print(user_mail)
    return render_template('aboutus.html')


@app.route('/home')
def home():
    print(user_mail)
    return render_template('home.html')


@app.route('/requestform',methods=["GET", "POST"])
def requestform():
    print(user_mail)
    if request.method == "POST":
        # email = request.form["rname"]
        # print(rname+str('22222'))
        name=request.form.get("rname", False)
        rollno=request.form.get("rrollno", False)
        title=request.form.get("rtitle", False)
        description=request.form.get("rdescription", False)
        category=request.form.get("rcategory", False)
        phone=request.form.get("rphone", False)
        contactvia=request.form.get("rcontactvia", False)


        # print(name,rollno,title,description,category,phone,contactvia)
        
        # cu=auth.current_user['email']
        email=name+rollno
        data={'email':email,'name':name,'rollno':rollno,'title':title,'description':description,'category':category,'phone':phone,'comtactvia':contactvia,'Email':user_mail}
        db.child('students').child(email+'_'+title).set(data)
        flash('Request Sent sucessfully', category='sucessful')
        # print(auth.current_user['email'])
        return redirect('/home')
   

    return render_template("requestform.html")
    
    








storage=firebase.storage()


def give_file_locAnd_Name():
    p=db.child('storage').get()
    all_data=[]
    if p !=None:
        for i in p.each():
            # print('i.key',i.key())
            # print('i.val',i.val())
        
            all_data.append((i.key(),i.val()))
            print(all_data)
    return all_data
# give_file_locAnd_Name()


@app.route('/placement',methods=["GET", "POST"])
def placement():
    print(user_mail)
    all_companydata=give_file_locAnd_Name()

    
    if request.method == "POST":

        companyname = request.form["companyname"]
        
        year = request.form["date"]
        file1=request.files['file1']
        time=year
        # time=datetime.now()
        # time=str(time)

        doc_key=companyname+str(time)
        data={'year':year,'companyname':companyname,'loc':companyname+str(time)}
        db.child('storage').child(doc_key).set(data)
        
        
        try:
            
            

            storage.child(doc_key).put(file1)
            flash('File Uploaded sucessfully', category='sucessful')
            print('Uploaded Sucessfully')
            
        except:
            print('Please the enter the file again')
            flash('Please Upload .', category='error')

        
       
        all_companydata=give_file_locAnd_Name()
        render_template('placement.html',all_companydata=all_companydata)



    
    return render_template('placement.html',all_companydata=all_companydata)













@app.route('/requests')
def requests():
    print(user_mail)
    p=db.child('students').get()
    all_data=[]
    for i in p.each():
        email=i.key()
        print('email= ',email)        
        data=i.val()
        print('data= ',data)
        all_data.append((email,data))
    

    return render_template('requests.html',all_data=all_data,user_mail=user_mail)

# rs='C:/Users/AMIT/OneDrive/Desktop'
# rs=Environment.getExternalStorageDirectory()
@app.route('/download/<string:k>', methods=['GET', 'POST'])
def download(k):
    print(user_mail)

    cloudfilename=k
    storage.child(cloudfilename).download('',k)
    url=storage.child(cloudfilename).get_url(None)

    
    # req = Request(url)
    # webpage = urlopen(req).read()
    
    webbrowser.open(url)
    all_companydata=give_file_locAnd_Name()



    return render_template('placement.html',all_companydata=all_companydata)

@app.route('/view/<string:k>', methods=['GET', 'POST'])
def view(k):
    print(user_mail)
    data=ast.literal_eval(k)
    

    return render_template('view.html',data=data)


@app.route('/resolved/<string:k>', methods=['GET', 'POST'])
def resolved(k):
    db.child('students').child(k).remove()

    return redirect('/requests')
    


@app.route('/respond/<string:k>', methods=['GET', 'POST'])
def respond(k):
    k=ast.literal_eval(k)
    request_owner_id=k['Email']
    request_title=k['title']
    request_owner_name=k['name']

    msg = Message('Regarding CloseShare Request '+str(request_title)+'request',sender =user_mail,recipients =[request_owner_id] )
    msg.body = 'Hello ' +str(request_owner_name) +'\n I am ready to help you out ' +str(user_mail)
    mail.send(msg)
    print('Reciver == ',k,'sender ==',user_mail)
    return redirect('/requests')
    









if __name__=="__main__":
   
    app.run(debug=True)