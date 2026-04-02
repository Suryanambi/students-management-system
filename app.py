from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('index.html', students=students)

# ADD student
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    if name:
        students.append(name)
    return redirect('/')

# DELETE student
@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(students):
        students.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
