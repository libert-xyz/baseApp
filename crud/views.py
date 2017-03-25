from crud import app,db
from flask import render_template, request, url_for,redirect,flash,jsonify,abort
#from models import Messages
from crud.models import Messages
import logging
from logging.handlers import RotatingFileHandler
import datetime
from sqlalchemy import desc



@app.route('/',methods=['GET'])
def index():
    return render_template('main.html')


@app.route('/api',methods=['GET','POST'])
def api():
    #query = Messages.query.all()
    query = Messages.query.order_by(desc(Messages.date_message)).all()

    if request.method == 'POST':

        request_data = request.get_json()
        nick = request_data['nick']
        mssg = request_data['text']

        if nick == '':
            nick = "Anonymous"

        m = Messages(nickname=nick)
        m.date_message= datetime.datetime.utcnow()
        m.message= mssg
        db.session.add(m)
        db.session.commit()

        return jsonify({
                    'id': m.id,
                    'nickname': m.nickname,
                    'date': m.date_message,
                    'message': m.message
        })

    return jsonify(Messages=[i.serialize for i in query])
