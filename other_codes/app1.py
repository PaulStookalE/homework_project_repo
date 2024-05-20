from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)


with app.app_context():
    db.create_all()




# @app.route('/my_info')
# def my_info():
#     name = 'Paul'
#     age = 13
#     status = 'Developer'

#     return f'Name -- {name}\nAge -- {age}\nStatus -- {status}'


@app.route('/my_info')
def my_info():
    datas = {
        13: 'Paul'
    }
    about_me = 'This is the first homework about templates.'
    header = 'First homework template.'
    
    return render_template('main1.html', header= header, about_me= about_me, datas= datas, title= 'About me web')



@app.route('/main', methods= ['GET', 'POST'])
def main():
    if request.method == 'POST':
        pass
    else:
        header = 'Quick description about website.'
        description = 'This is my first template using HTML- and CSS codes to do a website about me.'
        return render_template('main.html', header= header, description= description, title= 'Main')



@app.route('/about_me')
def about_me():
    header = 'Quick acquintance with me.'
    text_about_me = 'My name is Paul, I am 13 years old and I`m from Kramatorsk, Ukraine.'
    return render_template('about_me.html', header= header, text_about_me= text_about_me, title= 'About me')


@app.route('/hobbies')
def hobby():
    header = 'Quick introduction about my hobbies'
    return render_template('hobbies.html', header= header, title= 'Hobbies')



@app.route('/career_plans')
def career_plans():
    header = 'My plans on my life'
    my_plans = 'To become a Fullstack developer and live in Kiew'
    return render_template('career_plans.html', header= header, my_plans= my_plans, title= 'Career plans')



@app.route('/help')
def help():
    header = 'My contacts in different social networks'
    return render_template('help.html', header= header, title= 'Help')






if __name__ == '__main__':
    app.run(debug=True)