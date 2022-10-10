# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

@app.route('/')
# ‘/’ URL is bound with welcome() function.
#http://127.0.0.1:5000 prints welcome message
def welcome():
    return 'Hello Flask! This is the home page'


#http://127.0.0.1:5000/hello prints hello message
@app.route('/hello')
def hello():
   return 'Hello to you as well!'


#http://127.0.0.1:5000/hello/naus prints hello message
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
 

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

#redirects examples
#chooses which msg to redirect based on <name> used in url
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


#http://127.0.0.1:5000/hellopage renders an html page instead of msg
@app.route("/hellopage")
def hellopage():
   return render_template("hellopage.html")


#http://127.0.0.1:5000/login shows a login page and accepts form submission and redirects to success msg
#redirects to success msg after login form is submitted
@app.route('/login',methods = ['POST', 'GET'])
def login():
   #redirect after POST submission
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))

   else: #GET 
      return render_template('login.html')


#http://127.0.0.1:5000/userinfo is a form to take user input and display after submit to next page
@app.route('/userinfo',methods = ['POST', 'GET'])
def user_info():
   #check userinfo.html form method which tells which route to redirect. /showinfo in this case
   return render_template('userinfo.html') 


@app.route('/showinfo',methods = ['POST', 'GET'])
def show_info():
   if request.method == 'POST':
      result = request.form
      # user_items variable can be found in jinja template of showinfo.html
      return render_template("showinfo.html",user_items = result) 

#file uploads example: http://127.0.0.1:5000/upload is a form page to upload a file
@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      # f = request.files['file']
      # f.save(secure_filename(f.filename))
      # return f"{request.url_root}{filepath}"
      # return 'file uploaded successfully'

      # receive the file from the client
      file = request.files['file']
      filepath = f'static/temp/{file.filename}'
      file.save(filepath) # save to directory
      
      # return server url to client
      return f"file uploaded successfully at: {request.url_root}{filepath}"
   
def create_app():
   return app

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)

   #  from waitress import serve
   #  print("serving...")
   #  serve(app, host="0.0.0.0", port=8080)