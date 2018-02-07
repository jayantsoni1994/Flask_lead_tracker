from flask import Flask,render_template,flash,redirect,request,url_for,session,logging
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired,Length,Email
from passlib.hash import sha256_crypt
from db import *
from flask import Flask
from flask_mail import Mail, Message#pip install flask_mail
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from functools import wraps





db = Db()
courseList = []
for i in db.execute("SELECT * FROM course_names"):
    courseList.append(i)
db.commit()
db.close()

app=Flask(__name__)
# gmail=Mail(app)
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'gsanjeevreddy91@gmail.com'
# app.config['MAIL_PASSWORD'] = 'digitallync'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# gmail = Mail(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'avaniREDDY52936'
app.config['MYSQL_DB'] = 'flaskappdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql=MySQL(app)

# -----------------------------Login/logout--------------------------------

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/students')

def students():
  cur=mysql.connection.cursor()
  cur.execute("SELECT * FROM joinings WHERE `status`='complect'")
  rv11=cur.fetchall()
  cur.execute("SELECT * FROM joinings WHERE `status`='dead'")
  rv22=cur.fetchall()
  return render_template('students.html',rv=rv11,rv1=rv22)

@app.route('/about')
def index():
  id = request.args.get('id')
  print("complect:",id)
  cur=mysql.connection.cursor()
  cur.execute("UPDATE `joinings` SET `status`='complect' WHERE id=%s",[id])
  cur.execute("SELECT * FROM joinings WHERE `status`='complect'")
  rv=cur.fetchall()
  mysql.connection.commit()
  return render_template('index.html',rv=rv)

@app.route('/delay')
def delay():
  id = request.args.get('id')
  print("delay:",id)
  cur=mysql.connection.cursor()
  cur.execute("UPDATE `joinings` SET `status`='delay' WHERE id=%s",[id])
  cur.execute("SELECT * FROM joinings WHERE `status`='delay'")
  rv=cur.fetchall()
  mysql.connection.commit()
  return render_template('index.html',rv=rv)

@app.route('/dead')
def dead():
  id = request.args.get('id')
  print("dead:",id)
  cur=mysql.connection.cursor()
  cur.execute("UPDATE `joinings` SET `status`='dead' WHERE id=%s",[id])
  cur.execute("SELECT * FROM joinings WHERE `status`='dead'")
  rv=cur.fetchall()
  mysql.connection.commit()
  return render_template('index.html',rv=rv)
#------------currentpage--------------------
@app.route('/currentstatus')
def currentstatus():
  cur=mysql.connection.cursor()
  cur.execute('''SELECT * FROM joinings''')
  rv=cur.fetchall()
  return render_template('currentstatus.html',rv=rv)

#---------------------------------------------------
@app.route('/deleteprofile')

def deleteprofile():
  id = request.args.get('id')
  print("delect:",id)
  cur=mysql.connection.cursor()
  cur.execute("DELETE FROM `registers`  WHERE id=%s",[id])
  mysql.connection.commit()
 
  return redirect(url_for('home'))

@app.route('/willing11')

def willing11():
  id=request.args.get('id')
  print('willing11::',id)
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,name,email FROM users WHERE id=%s",[id])
  rv=cur.fetchall()
  person=rv[0]
  print(person)
  return render_template('update.html',person=person)

@app.route('/updateprofile')

def updateprofile():
  id=request.args.get('id')
  print('updateproile::',id)
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,st_demo_date FROM registers WHERE id=%s",[id])
  rv=cur.fetchall()
  person=rv[0]
  print(person)
  return render_template('update.html',person=person)

@app.route('/updateprofile12')
def updateprofile12(): 
  name=request.args.get('name')
  id1=request.args.get('idel')
  print(name)
  print(id1)
  
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,st_demo_date FROM registers WHERE id='"+id1+"'")
  rv=cur.fetchall()
  a=list(rv)
  print("rvv",list(rv))
  b=a[0]['st_demo_date']
  c=a[0]['id']
  cur=mysql.connection.cursor()
  cur.execute("UPDATE `registers` SET `st_demo_date`=%s WHERE id=%s",[name,c])
  rv1=cur.fetchall()
  print(rv1)
  mysql.connection.commit()

  return redirect(url_for('home'))
# ------------------------------------------------------------------

#-----------------------------------------------------
#----------------------delay---------------------

@app.route('/updateprofiledelay')
def updateprofiledelay():
  id=request.args.get('id')
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,comlection_date FROM joinings WHERE id=%s",[id])
  rv=cur.fetchall()
  person=rv[0]
  print(person)
  return render_template('updatedelay.html',person=person)

@app.route('/updateprofile12delay')
def updateprofile12delay(): 
  name=request.args.get('namedelay')
  id1=request.args.get('ideldelay')
  print(id1)
  
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,comlection_date FROM joinings WHERE id='"+id1+"'")
  rv=cur.fetchall()
  a=list(rv)
  print("rvv",list(rv))
  b=a[0]['comlection_date']
  c=a[0]['id']
  cur=mysql.connection.cursor()
  cur.execute("UPDATE `joinings` SET `comlection_date`=%s WHERE id=%s",[name,c])
  rv1=cur.fetchall()
  print(rv1)
  mysql.connection.commit()

  return redirect(url_for('home'))

#-----------------------------------------------------
#----------------------rejoin---------------------

@app.route('/updateprofilerejoin')
def updateprofilerejoin():
  id=request.args.get('id')
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,data_joining FROM joinings WHERE id=%s",[id])
  rv=cur.fetchall()
  person=rv[0]
  print(person)
  return render_template('updaterejoin.html',person=person)

@app.route('/updateprofile12rejoin')
def updateprofile12rejoin(): 
  name=request.args.get('namerejoin')
  id1=request.args.get('idelrejoin')
  status='inprocess'
  print(id1)
  
  cur=mysql.connection.cursor()
  cur.execute("SELECT id,data_joining FROM joinings WHERE id='"+id1+"'")
  rv=cur.fetchall()
  a=list(rv)
  print("rvv",list(rv))
  b=a[0]['data_joining']
  c=a[0]['id']
  cur=mysql.connection.cursor()
  cur.execute("UPDATE `joinings` SET `data_joining`=%s WHERE id=%s",[name,c])
  rv1=cur.fetchall()
  cur.execute("UPDATE `joinings` SET `status`=%s WHERE id=%s",[status,c])
  rv2=cur.fetchall()
  print(rv1)
  mysql.connection.commit()

  return redirect(url_for('home'))

#-----------------------------------------------------
#-----------------------------------------------------
class RegisterForm11(Form):
  name=StringField('Name',[validators.Length(min=1,max=50)])

@app.route('/page')

def page2():
  cur=mysql.connection.cursor()
  cur.execute('''SELECT * FROM registers''')
  rv=cur.fetchall()

  return render_template('page2.html',rv1=rv)

class RegisterForm(Form):
  name=StringField('Name',[validators.Length(min=1,max=50)])
  mobile = StringField('mobile',[validators.Length(min=10,max =13 )])
  email=StringField('Email',[validators.Length(min=2,max=50)])
  course = SelectField(u'Course', choices=courseList)
  source = SelectField(u'Source', choices=[('None','None'),('Website','Website'),('Facebook','Facebook'),('Suleka','Suleka')])
  leadstatus = SelectField(u'leadstatus',choices=[('None','None'),('Demo','Demo'),('Counselling','Counselling'),('Callback','Callback')])
  dm_coulg_cb = DateField('dm_coulg_cb', format='%Y-%m-%d')

  counsler = StringField('counsler', [validators.Length(min =2 , max = 20)])
  remark = StringField('Remark', [validators.Length(min =2 , max = 20)])

@app.route('/register', methods = ['GET', 'POST'])

def register():
   form = RegisterForm(request.form)
   print("hiii")
   
   if request.method == 'POST' and form.validate():
       print('hello') 
       name = form.name.data
       mobile = form.mobile.data
       email = form.email.data  
       course = form.course.data
       source = form.source.data
       # source = request.form["form.source"]
       leadstatus = form.leadstatus.data
       dm_coulg_cb = form.dm_coulg_cb.data
       counsler = form.counsler.data
       remark = form.remark.data         
       # create cursor
       print(email)
       cur = mysql.connection.cursor()

       cur.execute("INSERT INTO registers(st_name,st_mobile,st_email,st_course,st_source,st_lead_status,st_demo_date,st_counsler,st_remarks) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s)",(name,mobile,email,course,source,leadstatus,dm_coulg_cb,counsler,remark))

       #commit to DB

       mysql.connection.commit()

       #close connection
       cur.close()
       # msg = Message('Hello', sender = 'gsanjeevreddy91@gmail.com', recipients = [(email)])
       # msg.body = "Hello %s welcome to digital lync"%(name)
       # gmail.send(msg)
    

       flash('Thank you for joining')

       return redirect(url_for('home'))

   return render_template('register.html',form = form)

class JoiningForm(Form):
  name=StringField('Name',[validators.Length(min=1,max=50)])
  course = SelectField(u'Course', choices=courseList)
  completion_date = DateField('completion_date', format='%Y-%m-%d')
  data_joining = DateField('data_joining', format='%Y-%m-%d')
  course_fee = StringField('course_fee',[validators.Length(min =2 ,max =10)])
  instructor = StringField('instructor', [validators.Length(min =2 , max = 20)])
  aadhar_number=StringField('aadhar_number',[validators.Length(min=2,max=50)])
  mobile = StringField('mobile',[validators.Length(min=10)])
  email=StringField('Email',[validators.Length(min=2,max=50)])
  remark = StringField('Remark', [validators.Length(min =2 , max = 20)])

@app.route('/joining', methods = ['GET', 'POST'])

def joining():
   form = JoiningForm(request.form)
   if request.method == 'POST' and form.validate():
       name = form.name.data 
       course = form.course.data
       completion_date = form.completion_date.data
       data_joining = form.data_joining.data
       course_fee = form.course_fee.data
       instructor = form.instructor.data
       aadhar_number = form.aadhar_number.data
       mobile = form.mobile.data
       email = form.email.data
       remark = form.remark.data
                
       # create cursor
       cur = mysql.connection.cursor()

       cur.execute("INSERT INTO joinings(name,course,comlection_date,data_joining,course_fee,instructor,aadhar_number,mobile,email,remarks) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s,%s)",(name,course,completion_date,data_joining,course_fee,instructor,aadhar_number,mobile,email,remark))

       #commit to DB

       mysql.connection.commit()

       flash('You are now registered and can log in','success')
       # msg = Message('Hello', sender = 'gsanjeevreddy91@gmail.com', recipients = [(email)])
       # msg.body = "Hi %s welcome to Digital lync Academy You have successfully joined in Digital Lync "%(name)
       # gmail.send(msg)

       #close connection
       cur.close()


       # return redirect(url_for('home'))

   return render_template('joinings.html',form = form)
#------------------------------------pase-2------------------------------------------------
class Councling(Form):
  Today_date=DateField('Today_date', format='%Y-%m-%d')
  course = SelectField(u'Course', choices=courseList) 
@app.route('/councling', methods = ['GET', 'POST'])

def councling():
   form = Councling(request.form)
   print("hiii")
   if request.method == 'POST' and form.validate():
       print('hello') 
       Today_date = form.Today_date.data
       course = form.course.data
       cur=mysql.connection.cursor()
       cur.execute('''SELECT * FROM registers WHERE st_course =%s AND st_demo_date=%s''',(course,Today_date))
       rv=cur.fetchall()
       return render_template('council1.html',rv=rv)
   return render_template('council.html',form = form)
#-------------------------page-3------------------------------------------------------------
class Calling(Form):
  demo_call=SelectField(u'demo_call',choices=[('None','None'),('Demo','Demo'),('Counselling','Counselling'),('Callback','Callback')])
  Today_date = DateField('Today_date', format='%Y-%m-%d')

@app.route('/calling', methods = ['GET', 'POST'])
def calling():
   form = Calling(request.form)
   print("hiii")
   if request.method == 'POST' and form.validate():
       print('hello') 
       demo_call = form.demo_call.data
       Today_date = form.Today_date.data
       cur=mysql.connection.cursor()
       cur.execute('''SELECT * FROM registers WHERE st_lead_status =%s AND st_demo_date=%s''',(demo_call,Today_date))
       rv=cur.fetchall()
       return render_template('calling1.html',rv=rv)
   return render_template('calling.html',form = form)

@app.route('/walkins')
def walkins():
  cur=mysql.connection.cursor()
  cur.execute('''SELECT * FROM registers''')
  rv=cur.fetchall()
  # print(rv)
  # cur.execute("SELECT status FROM joinings WHERE name='"++"'")
  # rv=cur.fetchall()
  return render_template('walkins.html',rv1=rv)

if __name__=='__main__':
  app.secret_key = os.urandom(12)
  app.run(host='localhost', port=8181, debug=True)