from flask import Blueprint
from flask import render_template
from flask import flash
from flask import request

from classes.User import User
from classes.Song import Song

import os
import jwt
import logging

from utilities.db_util import connect_execute_query


frontend = Blueprint('frontend',
                     __name__,
                     template_folder='templates')


@frontend.route('/',methods=['GET','POST'])
def charts():
    if request.method =='GET':
        select_query=f"SELECT * from songs order by votes desc limit 10"
        Songs=connect_execute_query(select_query)
        if Songs is None:
            logging.info(f"You have selected invalid genre, please try again")
        return render_template('charts.html',Songs=Songs)
    genre=request.form['genre']
    if(genre=='all'):
        select_query=f"SELECT * from songs order by votes desc limit 10"
        Songs=connect_execute_query(select_query)
        if Songs is None:
            logging.info(f"You have selected invalid genre, please try again")
            return render_template('charts.html')
        return render_template('charts.html',Songs=Songs)
    select_query=f"SELECT * from songs where '{genre}'=genre order by votes desc limit 10"
    Songs=connect_execute_query(select_query)
    if Songs is None:
        logging.info(f"You have selected invalid genre, please try again")
        return render_template('charts.html')
    return render_template('charts.html',Songs=Songs) 
    

@frontend.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method =='GET':
        return render_template('sign_up.html')

    username = request.form.get('user')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    user = User(username, password1)

    if password1 != password2:
        flash('Password must match', category='error')
        return render_template("sign_up.html")
        
    success = user.input_user()

    if not success:
        flash("User must have atleast 3 chars, password 4 or the user is already in database.", category='error')
        return render_template("sign_up.html")
        
    token = user.get_encoded_token()
    return render_template('user.html', user=user.name, token=token)


@frontend.route('/songs', methods=['GET','POST'])
def songs():
    if request.method =='GET':
        return render_template('songs.html')

    song_name = request.form.get('song')
    username = request.form.get('user')
    artist = request.form.get('artist')
    genre = request.form.get('genre')
    yt_link = request.form.get('yt_link')
    token = request.form.get('token')
       
    try:
        token = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])['token']
        token_query = f"SELECT * FROM users WHERE token='{token}'"
        result = connect_execute_query(token_query)

        if not result:
            flash("Token is not valid,please try again", category='error')
            return render_template('songs.html')

        logging.info(f"User [{result[0][1]}] is authenticated to use this API Endpoint")
    except Exception as e:
        logging.error(f"Error happened during authentication: [{e}]")
        flash(str(e), category='error')
        return render_template('songs.html')

    song = Song(artist,genre,song_name,yt_link,token)
    success = song.input_song()

    if not success:
        flash("Song already exists!", category='error')
        return render_template("songs.html")

    return render_template('added_song.html',name=song.song_name)

       
@frontend.route('/user')
def main():
    return render_template('user.html')
