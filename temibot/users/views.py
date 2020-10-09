from flask import Flask, request, Blueprint
from temibot import db
from temibot.models import User
from twilio.twiml.messaging_response import  MessagingResponse

users = Blueprint('users',__name__)


@users.route("/")
def welcome():
    return "Welcome to our bot Page for Hackacademy"


@users.route("/sms", methods = ["GET","POST"])
def sms_reply():
    msg = request.values.get('Body').lower()
    phone_no = request.values.get('From')#this gives us the phone number of the user
    phone_no = phone_no.replace("whatsapp:", "")
    response = MessagingResponse()
    user = User.query.filter_by(phone_num = phone_no).first()
    user_email = User.query.filter_by(email = "missing").first() 




    wel_msg = ['hey', 'hello', 'hi']
    # welcome message section
    if msg in wel_msg:
        if (user!=None):
            name = User.query.filter_by(phone_num=phone_no).first()
            reply = (f"Welcome back {name.full_name.upper()}, How can I help you today? These are the things I can do for you.\n\n"
            f"A.  Web Design\n"
            f"B.  Digital Marketing and Branding\n"
            f"C.  Web development\n"
            f"D.  Chatbot development\n"
            f"E. Providing Business Solutions with Artificial Intelligence and Machine Learning\n"
            f"F. Big data analysis\n\n"
            f"Please reply with *A* to choose option A or send *quit* to end the conversation")
            
        else:
            if (user== None):
                reply = (f"Hello there, Welcome to Temigotechnobs! How can I help you today? These are the things we do at Temigotechnobs.\n\n"
                f"A. Web Design\n"
                f"B. Digital Marketing and Branding\n"
                f"C. Web development\n"
                f"D. Chatbot development\n"
                f"E. Providing Business Solutions with Artificial Intelligence and Machine Learning\n"
                f"F. Big data analysis\n\n"
                f"Please *A* to choose option A or send quit to end the chat.")
        response.message(reply)
        responded = True

    if msg == "quit":
        if user== None:
            reply = (f"Ok, thanks. Please, What is your name?\n\n"
                f"Please respond like this:\n"
                f"*My name is <your name>*")
        else:
            reply = f"Ok, {user.full_name.upper(), goodbye}"
        response.message(reply)
        responded = True

    if "name" in msg: #we are expecting the name to come in at this section
        if user == None:
            try:
                name = msg.replace("my name is", "")
                user = User(phone_num = phone_no, email = "missing", full_name = name)
                #local_government = "missing", political_party = "missing", occupation = "missing", status = "registered",
                #otp_num =0000)
                db.session.add(user)
                db.session.commit()
                reply= (f"Ok, good. Your name has been registered!\n\n"
                f"What is your email address?")
            except:
                reply = (f"Please enter your details correctly.\n\n"
                f"If your full name is John Musa, send  *My name is John Musa*")

        response.message(reply)
        responded = True

    if   "@" in msg and "." in msg or "yahoo" in msg or "gmmail" in msg:
        if user != None:
            try:
                emai = msg
                #updating email and status
                user_email.email = emai
                #otp_get.otp_num = otp
                db.session.commit()
                #send_mail(emai, otp)
                reply =( f"Ok, good. We will get back to you soon!\n")
            except:
                if user_email == None:
                    reply = f"You have registered your email. {user.email} is the email you sent to us."


        response.message(reply)
        responded = True
    if msg == "ok":
        reply = f"Yeah, Thanks."
        response.message(reply)
        responded = True
        

    fallback_reply = f'Sorry, I didnt get that. Can you please give a valid input?'
    #f"I can only help you with the following; \n\n")
    
    
    if not responded:
        reply = fallback_reply
        response.message(reply)
        
    

    
    
    return str(response)