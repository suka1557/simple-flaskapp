from flask import Flask, render_template, request
from utils.utils import calculate_bmi_value

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_bmi():
    if request.method == 'POST':
        try:
            weight = (request.form['weight'])
            height = (request.form['height'])
            bmi = calculate_bmi_value(weight, height)
        except Exception as e:
            bmi = e

        return render_template('result.html', bmi=bmi)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
