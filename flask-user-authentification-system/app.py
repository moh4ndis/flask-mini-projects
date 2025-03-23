from flask import Flask , render_template,request,redirect,session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key='moh4ndis' #secret key for session management
bcrypt = Bcrypt(app)

#Simulated user database , dictionary
users={}

@app.route('/')
def home():
   return render_template('login.html') #redirect to login page by default

@app.route('/register',methods=['GET','POST'])
def register():
  if request.method=='POST':
      username=request.form['username']
      password=request.form['password']
      #check if username already exist
      if username in users:
         return 'Username already exists. Please choose a different one.'
      #hashed password
      hasher_password=bcrypt.generate_password_hash(password).decode('utf-8')
      users[username]=hasher_password #store hashed password
      print(users)
      return redirect('/login')
  return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and bcrypt.check_password_hash(users[username], password):
            session['user'] = username  # save user session
            return redirect('/dashboard')
        else:
            return 'Invalid username or password'
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
   if 'user' in session:
      return render_template('dashboard.html',user=session['user'])
   return redirect('/login')

@app.route('/logout')
def logout():
   session.pop('user',None) #remove user session
   return redirect('/login')

if(__name__ == '__main__'):
  app.run(debug=True)