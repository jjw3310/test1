from flask import Flask, request, render_template, redirect, flash
import csv

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # login 
        if username != "aa" or password != "bb":
            return redirect('/')

        return redirect('/data')
    else:
        return render_template('index.html')
    
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/data')
def show_data():
    data = []
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # first header next
        for row in csv_reader:
            name = row[0]
            age = int(row[1])
            data.append({'name': name, 'age': age})
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


