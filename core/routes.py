from core import app
from core.forms import ResultForm

from flask import render_template, request, redirect, url_for, flash


@app.route('/', methods=['GET','POST'])
def task_1():
    form = ResultForm()
    if form.validate_on_submit():
        a = form.a.data
        b = form.b.data
        c = form.c.data
        x_1 = 0
        x_2 = 0
        if b**2+4*a*c == 0:
            x_1 = -b/2*a
            result = x_1
            flash(f'Квадратное уравнение решено успешно! Ответ: {result}', 'success')
            return render_template('success.html')
        elif b**2+4*a*c > 0:
            num = b**2-4*a*c
            num_2 = -b + num**(0.5)
            x_1 = num_2/2*a
            num_3 = -b - num**(0.5)
            x_2 = num_3/2*a
            flash(f'Квадратное уравнение решено успешно! Ответ: 1-x = {x_1}, 2-x = {x_2}', 'success')
            return render_template('success.html')

        elif b**2+4*a*c < 0:
            flash(f'Квадратное уравнение не имеет корней!', 'success') 
            return render_template('success.html')

    return render_template('task_1.html', form=form)

@app.route('/task_2', methods=['GET','POST'])
def task_2():

    return render_template('task_2.html')

@app.route('/result')
def result():

    return render_template('result.html')