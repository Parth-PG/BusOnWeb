from flask import Flask,request,url_for,redirect
from flask import render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLAlCHEMY_DATABASE_URI']='mysql://username:dbpass@host add / databaseName'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://DarkWebArtists:root1234@DarkWebArtists.mysql.pythonanywhere-services.com/DarkWebArtists$default'
db=SQLAlchemy(app)

class Admin(db.Model):
    ID=db.Column(db.String(30),primary_key=True)
    Password=db.Column(db.String(30),nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

#ADMIN_LOGIN

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/login',methods=['POST'])
def login():
    n1=request.form.get('u1')
    n2=request.form.get('u2')
    data1=Admin.query.filter_by(ID=n1).first()
    data2=Admin.query.filter_by(Password=n2).first()
    error='Invalid username or password'
    if data1:
        if data2:
            return redirect(url_for('admin',user=n1,_method='POST'))
        else:
            return render_template('adminlogin.html',error=error)
    else:
        return render_template('adminlogin.html',error=error)

@app.route('/admin/<user>',methods=['POST','GET'])
def admin(user):
    if user is None and request.method=='GET':
        return redirect(url_for('adminlogin'))
    else:
        return render_template('login.html')


# guard database

class Guard(db.Model):
    ID=db.Column(db.String(30),primary_key=True)
    Password=db.Column(db.String(30),nullable=False)

@app.route('/guardlogin')
def guardlogin():
    return render_template('guardlogin.html')

@app.route('/gulogin',methods=['POST'])
def gulogin():
    n1=request.form.get('u1')
    n2=request.form.get('u2')
    data1=Guard.query.filter_by(ID=n1).first()
    data2=Guard.query.filter_by(Password=n2).first()
    error='Invalid username or password'
    if data1:
        if data2:
            return redirect(url_for('guard',user=n1,_method='POST'))
        else:
            return render_template('guardlogin.html',error=error)
    else:
        return render_template('guardlogin.html',error=error)

@app.route('/guard/<user>',methods=['POST','GET'])
def guard(user):
    if user is None and request.method=='GET':
        return redirect(url_for('guardlogin'))
    else:
        return render_template('fill_info.html')

class Daily_info(db.Model):
    Date=db.Column(db.String(20),primary_key=True)
    Bus_no=db.Column(db.Integer,nullable=False)
    Time=db.Column(db.String(10),nullable=False)
    Student=db.Column(db.Integer,nullable=False)

@app.route('/info',methods=['GET','POST'])
def info():
    if request.method=="POST":
        n1=request.form.get('u1')
        n2=request.form.get('u2')
        n3=request.form.get('u3')
        n4=request.form.get('u4')
        entry=Daily_info(Date=n1, Bus_no=n2, Time=n3, Student=n4)
        db.session.add(entry)
        db.session.commit()
    return render_template('fill_info.html')

#FACULTY_LOGIN

class Faculty(db.Model):
    ID=db.Column(db.String(30),primary_key=True)
    Password=db.Column(db.String(30),nullable=False)

@app.route('/facultylogin')
def facultylogin():
    return render_template('facultylogin.html')

@app.route('/falogin',methods=['POST'])
def falogin():
    n1=request.form.get('u1')
    n2=request.form.get('u2')
    data1=Faculty.query.filter_by(ID=n1).first()
    data2=Faculty.query.filter_by(Password=n2).first()
    error='Invalid username or password'
    if data1:
        if data2:
            return redirect(url_for('faculty',user=n1,_method='POST'))
        else:
            return render_template('facultylogin.html',error=error)
    else:
        return render_template('facultylogin.html',error=error)

@app.route('/faculty/<user>',methods=['POST','GET'])
def faculty(user):
    if user is None and request.method=='GET':
        return redirect(url_for('facultylogin'))
    else:
        return render_template('faculty.html')

#STUDENT_LOGIN

class Student(db.Model):
    ID=db.Column(db.String(30),primary_key=True)
    Password=db.Column(db.String(30),nullable=False)

@app.route('/studentlogin')
def studentlogin():
    return render_template('studentlogin.html')

@app.route('/stlogin',methods=['POST','GET'])
def stlogin():
    if request.method=='POST':
        n1=request.form.get('u1')
        n2=request.form.get('u2')
        data1=Student.query.filter_by(ID=n1).first()
        data2=Student.query.filter_by(Password=n2).first()
        error='Invalid username or password'
        if data1:
            if data2:
                return redirect(url_for('student',user=n1,_method='POST'))
            else:
                return render_template('studentlogin.html',error=error)
        else:
            return render_template('studentlogin.html',error=error)
    else:
        return render_template('studentlogin.html')

@app.route('/student/<user>',methods=['POST','GET'])
def student(user):
    if user is None and request.method=='GET':
        return redirect(url_for('studentlogin'))
    else:
        return render_template('student.html')

#MAP_CODE
class Route(db.Model):
    Stop_no=db.Column(db.Integer,primary_key=True)
    Link=db.Column(db.String(500),nullable=False)
    Route_no=db.Column(db.String(10),nullable=False)
    Stop_name=db.Column(db.String(30),nullable=False)

@app.route('/seemap',methods=['POST'])
def seemap():
    v1=request.form.get('list1')
    drive=Location.query.filter_by(Bus_no=v1).first()
    loc=drive.current_loc
    links=Route.query.filter_by(Stop_no=loc).first()
    link1=links.Link
    #link='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d11024.92805944445!2d75.86722740708456!3d22.760616040416327!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x396302914b2a05eb%3A0xe427a8ddaa5bc6af!2sMr%2010%20Chandra%20Gupt%20Morya%20Square!5e0!3m2!1sen!2sin!4v1600610874212!5m2!1sen!2sin'

    return render_template("student.html",ilink=link1)


#DRIVER_REGISTRATION

@app.route('/driverregis')
def driverregis():
    return render_template("driverregis.html")

#DRIVER_LOGIN
class Driver(db.Model):
    ID=db.Column(db.String(30),primary_key=True)
    Name=db.Column(db.String(30),nullable=False)
    Age=db.Column(db.String(30),nullable=False)
    Address=db.Column(db.String(30),nullable=False)
    contact_no=db.Column(db.String(30),nullable=False)
    Bus_no=db.Column(db.Integer,nullable=False)
    Licence=db.Column(db.String(30),nullable=False)
    Photo=db.Column(db.String(30),nullable=False)
    Password=db.Column(db.String(30),nullable=False)

@app.route('/drregis',methods=['POST','GET'])
def drregis():
    if request.method=='POST':
        n1=request.form.get('u1')
        n2=request.form.get('u2')
        n3=request.form.get('u3')
        n4=request.form.get('u4')
        n5=request.form.get('u5')
        n6=request.form.get('u6')
        n7=request.form.get('u7')
        n8=request.form.get('u8')
        n9=request.form.get('u9')
        entry=Driver(ID=n5, Name=n1, Age=n2, Address=n4, contact_no=n3, Bus_no=n8, Licence=n6, Photo=n7, Password=n9)
        db.session.add(entry)
        db.session.commit()
    return render_template('driverregis.html')

@app.route('/driverlogin')
def driverlogin():
    return render_template("driverlogin.html")



@app.route('/dlogin',methods=['POST'])
def dlogin():
    n1=request.form.get('u1')
    n2=request.form.get('u2')
    data1=Driver.query.filter_by(ID=n1).first()
    data2=Driver.query.filter_by(Password=n2).first()
    error='Invalid username or password'
    if data1:
        if data2:
            return redirect(url_for('driver',user=n1,_method='POST'))
        else:
            return render_template('driverlogin.html',error=error)
    else:
        return render_template('driverlogin.html',error=error)

@app.route('/driver/<user>',methods=['POST','GET'])
def driver(user):
    if user is None and request.method=='GET':
        return redirect(url_for('driverlogin'))
    else:
        #businfo=Driver.query.filter_by(ID='DR001').first()
        #busno=businfo.Bus_no
        return render_template('driver.html')
            #if data3 is None:
         #   return render_template('driver.html')#,busno=busn)


#LOCATION_TABLE
class Location(db.Model):
    Bus_no=db.Column(db.Integer,primary_key=True)
    current_loc=db.Column(db.String(30),nullable=False)

@app.route('/current',methods=['POST'])
def current():
    cu=request.form.get('list1')
    bn=request.form.get('list2')
    drive=Location.query.filter_by(Bus_no=bn).first()
    drive.current_loc=cu
    db.session.commit()
    return render_template('driver.html')

#showall

#class Daily_info(db.Model):
 #   Date=db.Column(db.Date,primary_key=True)
  #  Bus_no=db.Column(db.String(30),nullable=False)
   # Time=db.Column(db.Time,nullable=False)
    #Student=db.Column(db.Integer,nullable=False)

@app.route('/showall')
def showall():
    return render_template('showall.html')

@app.route('/details',methods=['POST'])
def details():
    showd=Daily_info.query.all()
    return render_template('showall.html',detailss=showd)
 #   dataget=Daily_info.query.filter_by(Date=n1).first()
  #  busno=Daily_info.query.filter_by(Bus_no=n2)
