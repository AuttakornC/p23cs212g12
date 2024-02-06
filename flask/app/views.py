import json
from flask import (jsonify, render_template,
                  request, url_for, flash, redirect)

from sqlalchemy.sql import text
from app import app
from app import db
from app.models.contact import Contact
from app.models.blog import BlogEntry

@ app.route('/')
def home():
    return "Flask says 'Hello world!'"

@app.route('/crash')
def crash():
    return 1/0

@app.route('/db')
def db_connection():
    try:
        with db.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return '<h1>db works.</h1>'
    except Exception as e:
        return '<h1>db is broken.</h1>' + str(e)

@app.route('/lab04')
def lab04_bootstrap():
    return app.send_static_file('lab04_bootstrap.html')

@app.route("/lab10/contacts")
def lab10_db_contacts():
    contacts = []
    db_contacts = Contact.query.all()


    contacts = list(map(lambda x: x.to_dict(), db_contacts))
    app.logger.debug("DB Contacts: " + str(contacts))


    return jsonify(contacts)

@app.route('/lab10', methods=('GET', 'POST'))
def lab10_phonebook():
    if request.method == 'POST':
        result = request.form.to_dict()
        app.logger.debug(str(result))
        id_ = result.get('id', '')
        validated = True
        validated_dict = dict()
        valid_keys = ['firstname', 'lastname', 'phone']


        # validate the input
        for key in result:
            app.logger.debug(f"{key}: {result[key]}")
            # screen of unrelated inputs
            if key not in valid_keys:
                continue


            value = result[key].strip()
            if not value or value == 'undefined':
                validated = False
                break
            validated_dict[key] = value


        if validated:
            app.logger.debug('validated dict: ' + str(validated_dict))
            # if there is no id: create a new contact entry
            if not id_:
                entry = Contact(**validated_dict)
                app.logger.debug(str(entry))
                db.session.add(entry)
            # if there is an id already: update the contact entry
            else:
                contact = Contact.query.get(id_)
                contact.update(**validated_dict)

            db.session.commit()


        return lab10_db_contacts()
    return app.send_static_file('lab10_phonebook.html')

@app.route('/lab10/remove_contact', methods=('GET', 'POST'))
def lab10_remove_contacts():
    app.logger.debug("LAB10 - REMOVE")
    if request.method == 'POST':
        result = request.form.to_dict()
        id_ = result.get('id', '')
        try:
            contact = Contact.query.get(id_)
            db.session.delete(contact)
            db.session.commit()
        except Exception as ex:
           app.logger.error(f"Error removing contact with id {id_}: {ex}")
           raise
    return lab10_db_contacts()

@app.route("/hw10")
def lab11():
    return app.send_static_file("hw10_microblog.html")


@app.route("/hw10/blog", methods=('GET', 'POST', 'DELETE'))
def hw10_blog():
    if request.method == 'POST':
        request_data = request.form.to_dict()
        try:
            id_, name, email, message = request_data.get("id", ""), request_data["name"], request_data["email"], request_data["message"]
        except:
            return jsonify({"message": "Your request don't have some arguments."}), 400
        have_err = False
        err_dict = {}
        if len(name) > 50:
            have_err = True
            err_dict["name"] = "Name must less than 51 charactors."
        if len(email) > 50:
            have_err = True
            err_dict["email"] = "Email must less than 51 charactors."
        elif len(list(filter(lambda x: len(x)>0, email.split("@"))))!=2 or \
            len(list(filter(lambda x: len(x)>0, email.split("@")[1].split(".")))) <= 1 :
            have_err = True
            err_dict["email"] = "Email's wrong format."
        
        if len(message) > 280:
            have_err = True
            err_dict["message"] = "Message must less than 281 charactors."
        if have_err:
            return jsonify(err_dict), 400
        
        if id_=="":
            db.session.add(BlogEntry(name, message, email))
        else :
            blog = BlogEntry.query.get(id_)
            blog.update(name, message, email)
        db.session.commit()

        return ""
    elif request.method=='DELETE':
        request_data = request.form.to_dict()
        try:
            id_ = request_data["id"]
            blog = BlogEntry.query.get(id_)
            db.session.delete(blog)
            db.session.commit()
        except Exception as ex:
            app.logger.error(f"Error removing contact with id {id_}: {ex}")
            return ""
        return ""
    else :
        blogs = []
        db_blogs = BlogEntry.query.all()

        blogs = list(map(lambda x: x.to_dict(), db_blogs))
        return jsonify(blogs)