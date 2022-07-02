from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for
        )

import pymongo
import razorpay
blueprint = Blueprint('scitech',__name__, template_folder="templates/", url_prefix='/scitech')

razorpay_secret_key='lmao'

@blueprint.route('/')
def show_scitech():
    return render_template("scitech/scitech_menu.html")
@blueprint.route('/enumeration')
def show_temp_enumeration():
    return render_template(f"scitech/scitech_menu.html")
@blueprint.route('/enumeration/register')
def show_temp2_enumeration():
    return render_template(f"scitech/scitech_menu.html")
@blueprint.route('/<event_name>')
def show_scitechpage(event_name):
    return render_template(f"scitech/{event_name}.html")

@blueprint.route("/chemenigma/register", methods=("GET","POST"))
def register_for_chemenigma2 ():
    event_name = "chemenigma"
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant1'],
                    "participant2_name" : request.form['participant2'],
                    "team_name" : request.form['team'],
                    "participant1_class" : request.form['clsp1'],
                    "participant2_class" : request.form['clsp2'],
                    "participant1_school" : request.form['school1'],
                    "participant2_school" : request.form['school2'],
                    "participant1_email" : request.form['emailp1'],
                    "participant2_email" : request.form['emailp2'],
                    "participant1_phone" : request.form['mobile1'],
                    "participant2_phone" : request.form['mobile2']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb['chemenigma']
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant1_email" : request.form['emailp1'] })

        if existing is None:
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        if existing is not None :
            flash("Email of participant 1 already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()

        return render_template("registration_message.html")

@blueprint.route("/chemenigma/register/post", methods=("GET","POST"))
def register_for_chemenigma ():
    event_name = "chemenigma"
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant1'],
                    "participant2_name" : request.form['participant2'],
                    "team_name" : request.form['team'],
                    "participant1_class" : request.form['clsp1'],
                    "participant2_class" : request.form['clsp2'],
                    "participant1_school" : request.form['school1'],
                    "participant2_school" : request.form['school2'],
                    "participant1_email" : request.form['emailp1'],
                    "participant2_email" : request.form['emailp2'],
                    "participant1_phone" : request.form['mobile1'],
                    "participant2_phone" : request.form['mobile2']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb['chemenigma']
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant1_email" : request.form['emailp1'] })

        if existing is None:
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        if existing is not None :
            flash("Email of participant 1 already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()

        return render_template("registration_message.html")

# @blueprint.route("/enumeration/register", methods=("GET", "POST"))
# def register_for_enumeration ():
#     event_name = "enumeration"
#     amount = 20000
#     g.user = amount
#     if request.method == "GET":
#         return render_template(f"scitech/registration/registration_{event_name}.html")
#
#     if request.method == "POST":
#         details = { "participant1_name" : request.form['participant1'],
#                     "participant2_name" : request.form['participant2'],
#                     "team_name" : request.form['team'],
#                     "participant1_school" : request.form['school1'],
#                     "participant2_school" : request.form['school2'],
#                     "participant1_email" : request.form['emailp1'],
#                     "participant2_email" : request.form['emailp2'],
#                     "participant1_phone" : request.form['mobile1'],
#                     "participant2_phone" : request.form['mobile2'],
#                     "payment_id" : None,
#                     "payment_status" : "Unknown"
#                     }
#         # Authenticating payments
#         razorpay_client = razorpay.Client(auth=("rzp_live_jEr5MWFDFyEN8f",razorpay_secret_key))
#         payment_id = request.form['razorpay_payment_id']
#
#
#         # Inserting things into the database
#         myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#
#         mydb = myclient['registrations']
#         mycol = mydb[event_name]
#
#
#         #Checking for duplicate email numbers
#         existing = mycol.find_one({ "participant1_email" : request.form['emailp1'] })
#
#         paydb = myclient['payments']
#         paycol = paydb[event_name]
#
#
#         if existing is None:
#             razorpay_client.payment.capture(payment_id, amount)
#             details['payment_id'] = payment_id
#             pay_details = razorpay_client.payment.fetch(payment_id)
#             paycol.insert_one(pay_details)
#             details['payment_status'] = pay_details['status']
#             flash(f"Payment ID:{payment_id}")
#             if pay_details['status'] == 'captured':
#                 flash("Payment Successful")
#             else:
#                 flash("Payment not confirmed, Contact us")
#             x = mycol.insert_one(details)
#             flash("Registered successfully!!")
#         else :
#             details['payment_id'] = payment_id
#             pay_details = razorpay_client.payment.fetch(payment_id)
#             paycol.insert_one(pay_details)
#             details['payment_status'] = pay_details['status']
#             flash(f"Payment ID:{payment_id}")
#             flash("Payment not confirmed")
#             flash("Email of participant 1 already registered ask for refund on email if paid twice")
#             myclient.close()
#             return render_template(f"scitech/registration/registration_{event_name}.html")
#
#         myclient.close()
#         return render_template(f"scitech/registration/registration_{event_name}.html")
