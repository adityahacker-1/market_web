from market import app,db
from flask import render_template,redirect,url_for,flash
from market.models import Item,User
from market.forms import RegisterForm
    
@app.route('/')
@app.route('/home')
def index_page():
    return render_template('index.html')


@app.route('/market')
def market_page():
    items=Item.query.all()
    return render_template('market.html',items=items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form=RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(username=form.username.data,email_address=form.email_address.data,password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors!={}: # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error: {err_msg}','error')
    return render_template('register.html',form=form)