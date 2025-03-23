from flask import Flask , request,render_template,redirect

app=Flask(__name__)

tasks=[]

@app.route('/')
def index():
  return render_template("index.html",tasks=tasks)

@app.route('/add',methods=['POST'])
def add_task():
   task=request.form['task']
   tasks.append(task)
   return redirect("/")

@app.route('/delete/<int:index>')
def delete_task(index):
   tasks.pop(index)
   return redirect("/")

@app.route('/edit/<int:index>',methods=['GET','POST'])
def edit_task(index):
  if request.method=='POST':
    tasks[index]=request.form['task']
    return redirect("/")
  return render_template('edit.html',index=index , task=tasks[index])

if __name__ == '__main__':
    app.run(debug=True)
