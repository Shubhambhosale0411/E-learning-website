#new csv
import csv

from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import EmailMultiAlternatives
from .models import Client
from .utility import EmailManager

#new
from django.template.loader import render_to_string, get_template
# Create your views here.


def index(request):
    return render(request,'index.html')
def index2(request):
	return render(request,'pages/aboutus.html')
def index3(request):
	return render(request,'pages/contact_us.html')
def index4(request):
	return render(request,'pages/service_accounting.html')
def index5(request):
	return render(request,'pages/service_bpo.html')
def index6(request):
	return render(request,'pages/service_business_setup.html')
def index7(request):
	return render(request,'pages/service_financial_coaching.html')
def index8(request):
	return render(request,'pages/service_investment_opportunities.html')
def index9(request):
	return render(request,'pages/service_property_management.html')
def index10(request):
	return render(request,'pages/service_tax_management.html')

def test(request):
    return JsonResponse({"msg":"Test json response"})

@csrf_exempt
def createMail(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode('utf-8'))

        mail_contents = {
            "subject": data.get("subject", ""),
            "to": data.get("to", ""),
            "message": data.get("message", ""),
            "isBulk": data.get("isBulk", False)
        }
        # send mail
        email = EmailManager(
            mail_contents["subject"], mail_contents["message"])

        if(mail_contents["isBulk"]):
            email.sendMultiple(mail_contents["to"])
        else:
            email.sendOne(mail_contents["to"])

        if(email.status == "success"):
            return JsonResponse({"msg": "success, mail sent", "number of mails sent": email.sent_count})
        else:
            return JsonResponse({"msg": "failure, unable to send mail", "number of mails sent": email.sent_count, })
    else:
        return JsonResponse({"msg":"only post request is allowed"})


@csrf_exempt
def saveUser(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode('utf-8'))

        client_data = {
            "first_name": data.get("name", ""),
            "last_name": data.get("name", ""),
            "email": data.get("email", ""),
            "phone_no": data.get("mobile", ""),
            "service_visited": data.get("service", ""),
            "page_visited": data.get("page", ""),
            "message": data.get("message", "")
        }

        # create new client
        new_client = Client(**client_data)
        new_client.save()

        # send welcome mail
        if(client_data["service_visited"]=="Financial Coaching & Restructuring"):
            #new
            #message="<html><body>Hello {{client_data['first_name']}},<p>Welcome to the world of programming with money tree team</p></body></html>"
            #message = get_template('mail.html').render(client_data)
            #email = EmailManager('Welcome to A Money Tree',
            #                    message,
            #                    client_data["email"],
            #                    ['team@amoneytreeonline.com'],
            #                    )
            #email.content_subtype = "html"  # Main content is now text/html
            #email.send()
            #print(email)
            #email.sendOne(client_data["email"])

            #new
            subject, from_email, to = 'Welcome to A Money Tree', 'team@amoneytreeonline.com', client_data["email"]
            text_content = 'yo'
            html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/><style>.fa {  padding: 20px;  text-align: center;  margin: 5px 2px;  font-size: 19px;  width: 50px;  }.fa:hover {  opacity: 0.9;  }  </style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br><h3>Social</h3></p><h4><li>   <a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">facebook</a> </li> </h4><h4>  <li>   <a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-facebook">instagram</a> </li> </h4><h4> <li>   <a href="https://www.linkedin.com/company/a-money-tree/" class="fa fa-facebook">linkedin</a> </li> </h4><h4> <li> <a href="https://youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" class="fa fa-facebook">youtube</a> </li></h4> <h3>Resources</h3><h4> <li> <a href="https://drive.google.com/drive/folders/1hCDwj80aGLpZ1ZTFwvp7uK2Tun1dA7E1" class="fa fa-facebook">Financial Coaching &amp; Advisory</a> </li></h4> </body></html>'
            #html_content = '<p>This is an <strong>important</strong> message.</p>'
            
            #html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>.fa {padding: 20px;font-size: 30px;width: 50px;text-align: center;text-decoration: none;}.fa:hover {opacity: 0.7;}.fa-facebook {background: #3B5998;color: white;}.fa-twitter {background: #cd486b;color: white;}</style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br></p><div><a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">FB</a><a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-twitter">insta</a></div></body></html>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return JsonResponse({"msg":"Your query is saved."})
        elif(client_data["service_visited"]=="Accounting Services"):

          #  email = EmailManager('Welcome to A Money Tree',
          #                      f"Welcome {client_data['first_name']}. We are glad to solve your yoo."
          #                      f" We are glad to solve your 2."
          #                      f" We are glad to solve your 2.")
          #  email.sendOne(client_data["email"])
            #new
            subject, from_email, to = 'Welcome to A Money Tree', 'team@amoneytreeonline.com', client_data["email"]
            text_content = 'yo'
            html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/><style>.fa {  padding: 20px;  text-align: center;  margin: 5px 2px;  font-size: 19px;  width: 50px;  }.fa:hover {  opacity: 0.9;  }  </style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br><br>We work with you on <strong>Book-Keeping, Extracting Information</strong> from your Voucher Level Documents, <strong>Generation of MIS, Balance Sheets.</strong> We also synergize your systems for <strong>Audits both Tax and Statutory. Creating the Entire Department for Finance & Accounting can also be taken up, with writing SOPs, Processes, Systems &</strong> more.<br><br>Our Belief is that complete Disclosure & Well written out Systems, and Financial Documents created on these lines, are an Asset for Management, Investors, Clients & for the Growth Story! The lesser made use of Financial Statements is to measure deviations and take corrective action for even the smallest of unfavourable changes. A Sound Team for F & A not only keeps you Compliant, but also becomes a Catalyst in creating faster growth and higher Scalability!<br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br><h3>Social</h3></p><h4><li>   <a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">facebook</a> </li> </h4><h4>  <li>   <a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-facebook">instagram</a> </li> </h4><h4> <li>   <a href="https://www.linkedin.com/company/a-money-tree/" class="fa fa-facebook">linkedin</a> </li> </h4><h4> <li> <a href="https://youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" class="fa fa-facebook">youtube</a> </li></h4> <h3>Resources</h3><h4> <li> <a href="https://drive.google.com/drive/folders/1hCDwj80aGLpZ1ZTFwvp7uK2Tun1dA7E1" class="fa fa-facebook">Financial Coaching &amp; Advisory</a> </li></h4> </body></html>'
            #html_content = '<p>This is an <strong>important</strong> message.</p>'
            #html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>.fa {padding: 20px;font-size: 30px;width: 50px;text-align: center;text-decoration: none;}.fa:hover {opacity: 0.7;}.fa-facebook {background: #3B5998;color: white;}.fa-twitter {background: #cd486b;color: white;}</style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br></p><div><a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">FB</a><a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-twitter">insta</a></div></body></html>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return JsonResponse({"msg":"Your query is saved."})
            
        elif(client_data["service_visited"]=="Complete Tax Management"):
            #new
            subject, from_email, to = 'Welcome to A Money Tree', 'team@amoneytreeonline.com', client_data["email"]
            text_content = 'yo'
            html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/><style>.fa {  padding: 20px;  text-align: center;  margin: 5px 2px;  font-size: 19px;  width: 50px;  }.fa:hover {  opacity: 0.9;  }  </style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We offer <strong>Income Tax & GST Record Maintenance, Extraction of Data & Computations, Filing of Returns, Query Handling, Record Keeping, Advisory, Tax Planning &</strong> more. We also synergize your systems for<strong> Audits both Tax and Statutory.</strong><br><br>Our Belief is that Seamlessly managed Tax Systems, keep you both Compliant and Clean on records. These are also important in current times where fast changing regulations need quick adaptation & agility on your part. Our Team has a cumulative experience of over 50 years in the field of Taxation and we bring to the table an entire Tax Management Suite.<br><br><strong>You would get access to a lot of Free Resources in your inbox and in our Links!</strong><br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br><h3>Social</h3></p><h4><li>   <a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">facebook</a> </li> </h4><h4>  <li>   <a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-facebook">instagram</a> </li> </h4><h4> <li>   <a href="https://www.linkedin.com/company/a-money-tree/" class="fa fa-facebook">linkedin</a> </li> </h4><h4> <li> <a href="https://youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" class="fa fa-facebook">youtube</a> </li></h4> <h3>Resources</h3><h4> <li> <a href="https://drive.google.com/drive/folders/1hCDwj80aGLpZ1ZTFwvp7uK2Tun1dA7E1" class="fa fa-facebook">Financial Coaching &amp; Advisory</a> </li></h4> </body></html>'
            #html_content = '<p>This is an <strong>important</strong> message.</p>'
            #html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>.fa {padding: 20px;font-size: 30px;width: 50px;text-align: center;text-decoration: none;}.fa:hover {opacity: 0.7;}.fa-facebook {background: #3B5998;color: white;}.fa-twitter {background: #cd486b;color: white;}</style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br></p><div><a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">FB</a><a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-twitter">insta</a></div></body></html>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return JsonResponse({"msg":"Your query is saved."})
        elif(client_data["service_visited"]=="Investment Opportunities"):
            #new
            subject, from_email, to = 'Welcome to A Money Tree', 'team@amoneytreeonline.com', client_data["email"]
            text_content = 'yo'
            html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/><style>.fa {  padding: 20px;  text-align: center;  margin: 5px 2px;  font-size: 19px;  width: 50px;  }.fa:hover {  opacity: 0.9;  }  </style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br><h3>Social</h3></p><h4><li>   <a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">facebook</a> </li> </h4><h4>  <li>   <a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-facebook">instagram</a> </li> </h4><h4> <li>   <a href="https://www.linkedin.com/company/a-money-tree/" class="fa fa-facebook">linkedin</a> </li> </h4><h4> <li> <a href="https://youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" class="fa fa-facebook">youtube</a> </li></h4> <h3>Resources</h3><h4> <li> <a href="https://drive.google.com/drive/folders/1hCDwj80aGLpZ1ZTFwvp7uK2Tun1dA7E1" class="fa fa-facebook">Financial Coaching &amp; Advisory</a> </li></h4> </body></html>'
            #html_content = '<p>This is an <strong>important</strong> message.</p>'
            #html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>.fa {padding: 20px;font-size: 30px;width: 50px;text-align: center;text-decoration: none;}.fa:hover {opacity: 0.7;}.fa-facebook {background: #3B5998;color: white;}.fa-twitter {background: #cd486b;color: white;}</style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br></p><div><a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">FB</a><a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-twitter">insta</a></div></body></html>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return JsonResponse({"msg":"Your query is saved."})
        elif(client_data["service_visited"]=="New Business Set-up Services"):
            #new
            subject, from_email, to = 'Welcome to A Money Tree', 'team@amoneytreeonline.com', client_data["email"]
            text_content = 'yo'
            html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/><style>.fa {  padding: 20px;  text-align: center;  margin: 5px 2px;  font-size: 19px;  width: 50px;  }.fa:hover {  opacity: 0.9;  }  </style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br><h3>Social</h3></p><h4><li>   <a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">facebook</a> </li> </h4><h4>  <li>   <a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-facebook">instagram</a> </li> </h4><h4> <li>   <a href="https://www.linkedin.com/company/a-money-tree/" class="fa fa-facebook">linkedin</a> </li> </h4><h4> <li> <a href="https://youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" class="fa fa-facebook">youtube</a> </li></h4> <h3>Resources</h3><h4> <li> <a href="https://drive.google.com/drive/folders/1hCDwj80aGLpZ1ZTFwvp7uK2Tun1dA7E1" class="fa fa-facebook">Financial Coaching &amp; Advisory</a> </li></h4> </body></html>'
            #html_content = '<p>This is an <strong>important</strong> message.</p>'
            #html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>.fa {padding: 20px;font-size: 30px;width: 50px;text-align: center;text-decoration: none;}.fa:hover {opacity: 0.7;}.fa-facebook {background: #3B5998;color: white;}.fa-twitter {background: #cd486b;color: white;}</style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br></p><div><a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">FB</a><a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-twitter">insta</a></div></body></html>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return JsonResponse({"msg":"Your query is saved."})
        
        elif(client_data["service_visited"]=="Properties Management"):
            #new
            subject, from_email, to = 'Welcome to A Money Tree', 'team@amoneytreeonline.com', client_data["email"]
            text_content = 'yo'
            html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/><style>.fa {  padding: 20px;  text-align: center;  margin: 5px 2px;  font-size: 19px;  width: 50px;  }.fa:hover {  opacity: 0.9;  }  </style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br><h3>Social</h3></p><h4><li>   <a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">facebook</a> </li> </h4><h4>  <li>   <a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-facebook">instagram</a> </li> </h4><h4> <li>   <a href="https://www.linkedin.com/company/a-money-tree/" class="fa fa-facebook">linkedin</a> </li> </h4><h4> <li> <a href="https://youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" class="fa fa-facebook">youtube</a> </li></h4> <h3>Resources</h3><h4> <li> <a href="https://drive.google.com/drive/folders/1hCDwj80aGLpZ1ZTFwvp7uK2Tun1dA7E1" class="fa fa-facebook">Financial Coaching &amp; Advisory</a> </li></h4> </body></html>'
            #html_content = '<p>This is an <strong>important</strong> message.</p>'
            #html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>.fa {padding: 20px;font-size: 30px;width: 50px;text-align: center;text-decoration: none;}.fa:hover {opacity: 0.7;}.fa-facebook {background: #3B5998;color: white;}.fa-twitter {background: #cd486b;color: white;}</style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br></p><div><a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">FB</a><a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-twitter">insta</a></div></body></html>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return JsonResponse({"msg":"Your query is saved."})
        
        elif(client_data["service_visited"]=="BPO"):
            #new
            subject, from_email, to = 'Welcome to A Money Tree', 'team@amoneytreeonline.com', client_data["email"]
            text_content = 'yo'
           # html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/><style>.fa {  padding: 20px;  text-align: center;  margin: 5px 2px;  font-size: 19px;  width: 50px;  }.fa:hover {  opacity: 0.9;  }  </style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br><h3>Social</h3></p><h4><li>   <a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">facebook</a> </li> </h4><h4>  <li>   <a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-facebook">instagram</a> </li> </h4><h4> <li>   <a href="https://www.linkedin.com/company/a-money-tree/" class="fa fa-facebook">linkedin</a> </li> </h4><h4> <li> <a href="https://youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" class="fa fa-facebook">youtube</a> </li></h4> <h3>Resources</h3><h4> <li> <a href="https://drive.google.com/drive/folders/1hCDwj80aGLpZ1ZTFwvp7uK2Tun1dA7E1" class="fa fa-facebook">Financial Coaching &amp; Advisory</a> </li></h4> </body></html>'
            #html_content = '<p>This is an <strong>important</strong> message.</p>'
            html_content='''
            <!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
        <!-- NAME: 1 COLUMN -->
        <!--[if gte mso 15]>
        <xml>
            <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
        </xml>
        <![endif]-->
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>*|MC:SUBJECT|*</title>
        
    <style type="text/css">
		p{
			margin:10px 0;
			padding:0;
		}
		table{
			border-collapse:collapse;
		}
		h1,h2,h3,h4,h5,h6{
			display:block;
			margin:0;
			padding:0;
		}
		img,a img{
			border:0;
			height:auto;
			outline:none;
			text-decoration:none;
		}
		body,#bodyTable,#bodyCell{
			height:100%;
			margin:0;
			padding:0;
			width:100%;
		}
		.mcnPreviewText{
			display:none !important;
		}
		#outlook a{
			padding:0;
		}
		img{
			-ms-interpolation-mode:bicubic;
		}
		table{
			mso-table-lspace:0pt;
			mso-table-rspace:0pt;
		}
		.ReadMsgBody{
			width:100%;
		}
		.ExternalClass{
			width:100%;
		}
		p,a,li,td,blockquote{
			mso-line-height-rule:exactly;
		}
		a[href^=tel],a[href^=sms]{
			color:inherit;
			cursor:default;
			text-decoration:none;
		}
		p,a,li,td,body,table,blockquote{
			-ms-text-size-adjust:100%;
			-webkit-text-size-adjust:100%;
		}
		.ExternalClass,.ExternalClass p,.ExternalClass td,.ExternalClass div,.ExternalClass span,.ExternalClass font{
			line-height:100%;
		}
		a[x-apple-data-detectors]{
			color:inherit !important;
			text-decoration:none !important;
			font-size:inherit !important;
			font-family:inherit !important;
			font-weight:inherit !important;
			line-height:inherit !important;
		}
		#bodyCell{
			padding:10px;
			border-top:1px inset ;
		}
		.templateContainer{
			max-width:600px !important;
			border:0;
		}
		a.mcnButton{
			display:block;
		}
		.mcnImage,.mcnRetinaImage{
			vertical-align:bottom;
		}
		.mcnTextContent{
			word-break:break-word;
		}
		.mcnTextContent img{
			height:auto !important;
		}
		.mcnDividerBlock{
			table-layout:fixed !important;
		}
	/*
	@tab Page
	@section Background Style
	@tip Set the background color and top border for your email. You may want to choose colors that match your company's branding.
	*/
		body,#bodyTable{
			/*@editable*/background-color:#ffffff;
		}
	/*
	@tab Page
	@section Background Style
	@tip Set the background color and top border for your email. You may want to choose colors that match your company's branding.
	*/
		#bodyCell{
			/*@editable*/border-top:1px inset ;
		}
	/*
	@tab Page
	@section Email Border
	@tip Set the border for your email.
	*/
		.templateContainer{
			/*@editable*/border:0;
		}
	/*
	@tab Page
	@section Heading 1
	@tip Set the styling for all first-level headings in your emails. These should be the largest of your headings.
	@style heading 1
	*/
		h1{
			/*@editable*/color:#202020;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:26px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:normal;
			/*@editable*/text-align:left;
		}
	/*
	@tab Page
	@section Heading 2
	@tip Set the styling for all second-level headings in your emails.
	@style heading 2
	*/
		h2{
			/*@editable*/color:#202020;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:22px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:normal;
			/*@editable*/text-align:left;
		}
	/*
	@tab Page
	@section Heading 3
	@tip Set the styling for all third-level headings in your emails.
	@style heading 3
	*/
		h3{
			/*@editable*/color:#202020;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:20px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:normal;
			/*@editable*/text-align:left;
		}
	/*
	@tab Page
	@section Heading 4
	@tip Set the styling for all fourth-level headings in your emails. These should be the smallest of your headings.
	@style heading 4
	*/
		h4{
			/*@editable*/color:#202020;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:18px;
			/*@editable*/font-style:normal;
			/*@editable*/font-weight:bold;
			/*@editable*/line-height:125%;
			/*@editable*/letter-spacing:normal;
			/*@editable*/text-align:left;
		}
	/*
	@tab Preheader
	@section Preheader Style
	@tip Set the background color and borders for your email's preheader area.
	*/
		#templatePreheader{
			/*@editable*/background-color:#fafafa;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:9px;
			/*@editable*/padding-bottom:9px;
		}
	/*
	@tab Preheader
	@section Preheader Text
	@tip Set the styling for your email's preheader text. Choose a size and color that is easy to read.
	*/
		#templatePreheader .mcnTextContent,#templatePreheader .mcnTextContent p{
			/*@editable*/color:#656565;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:12px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Preheader
	@section Preheader Link
	@tip Set the styling for your email's preheader links. Choose a color that helps them stand out from your text.
	*/
		#templatePreheader .mcnTextContent a,#templatePreheader .mcnTextContent p a{
			/*@editable*/color:#656565;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Header
	@section Header Style
	@tip Set the background color and borders for your email's header area.
	*/
		#templateHeader{
			/*@editable*/background-color:#FFFFFF;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:9px;
			/*@editable*/padding-bottom:0;
		}
	/*
	@tab Header
	@section Header Text
	@tip Set the styling for your email's header text. Choose a size and color that is easy to read.
	*/
		#templateHeader .mcnTextContent,#templateHeader .mcnTextContent p{
			/*@editable*/color:#202020;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:16px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Header
	@section Header Link
	@tip Set the styling for your email's header links. Choose a color that helps them stand out from your text.
	*/
		#templateHeader .mcnTextContent a,#templateHeader .mcnTextContent p a{
			/*@editable*/color:#007C89;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Body
	@section Body Style
	@tip Set the background color and borders for your email's body area.
	*/
		#templateBody{
			/*@editable*/background-color:#ffffff;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:2px solid #EAEAEA;
			/*@editable*/padding-top:0;
			/*@editable*/padding-bottom:9px;
		}
	/*
	@tab Body
	@section Body Text
	@tip Set the styling for your email's body text. Choose a size and color that is easy to read.
	*/
		#templateBody .mcnTextContent,#templateBody .mcnTextContent p{
			/*@editable*/color:#202020;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:16px;
			/*@editable*/line-height:100%;
			/*@editable*/text-align:left;
		}
	/*
	@tab Body
	@section Body Link
	@tip Set the styling for your email's body links. Choose a color that helps them stand out from your text.
	*/
		#templateBody .mcnTextContent a,#templateBody .mcnTextContent p a{
			/*@editable*/color:#007C89;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	/*
	@tab Footer
	@section Footer Style
	@tip Set the background color and borders for your email's footer area.
	*/
		#templateFooter{
			/*@editable*/background-color:#fafafa;
			/*@editable*/background-image:none;
			/*@editable*/background-repeat:no-repeat;
			/*@editable*/background-position:center;
			/*@editable*/background-size:cover;
			/*@editable*/border-top:0;
			/*@editable*/border-bottom:0;
			/*@editable*/padding-top:9px;
			/*@editable*/padding-bottom:9px;
		}
	/*
	@tab Footer
	@section Footer Text
	@tip Set the styling for your email's footer text. Choose a size and color that is easy to read.
	*/
		#templateFooter .mcnTextContent,#templateFooter .mcnTextContent p{
			/*@editable*/color:#656565;
			/*@editable*/font-family:Helvetica;
			/*@editable*/font-size:12px;
			/*@editable*/line-height:150%;
			/*@editable*/text-align:center;
		}
	/*
	@tab Footer
	@section Footer Link
	@tip Set the styling for your email's footer links. Choose a color that helps them stand out from your text.
	*/
		#templateFooter .mcnTextContent a,#templateFooter .mcnTextContent p a{
			/*@editable*/color:#656565;
			/*@editable*/font-weight:normal;
			/*@editable*/text-decoration:underline;
		}
	@media only screen and (min-width:768px){
		.templateContainer{
			width:600px !important;
		}

}	@media only screen and (max-width: 480px){
		body,table,td,p,a,li,blockquote{
			-webkit-text-size-adjust:none !important;
		}

}	@media only screen and (max-width: 480px){
		body{
			width:100% !important;
			min-width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnRetinaImage{
			max-width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImage{
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnCartContainer,.mcnCaptionTopContent,.mcnRecContentContainer,.mcnCaptionBottomContent,.mcnTextContentContainer,.mcnBoxedTextContentContainer,.mcnImageGroupContentContainer,.mcnCaptionLeftTextContentContainer,.mcnCaptionRightTextContentContainer,.mcnCaptionLeftImageContentContainer,.mcnCaptionRightImageContentContainer,.mcnImageCardLeftTextContentContainer,.mcnImageCardRightTextContentContainer,.mcnImageCardLeftImageContentContainer,.mcnImageCardRightImageContentContainer{
			max-width:100% !important;
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnBoxedTextContentContainer{
			min-width:100% !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageGroupContent{
			padding:9px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnCaptionLeftContentOuter .mcnTextContent,.mcnCaptionRightContentOuter .mcnTextContent{
			padding-top:9px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageCardTopImageContent,.mcnCaptionBottomContent:last-child .mcnCaptionBottomImageContent,.mcnCaptionBlockInner .mcnCaptionTopContent:last-child .mcnTextContent{
			padding-top:18px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageCardBottomImageContent{
			padding-bottom:9px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageGroupBlockInner{
			padding-top:0 !important;
			padding-bottom:0 !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageGroupBlockOuter{
			padding-top:9px !important;
			padding-bottom:9px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnTextContent,.mcnBoxedTextContentColumn{
			padding-right:18px !important;
			padding-left:18px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcnImageCardLeftImageContent,.mcnImageCardRightImageContent{
			padding-right:18px !important;
			padding-bottom:0 !important;
			padding-left:18px !important;
		}

}	@media only screen and (max-width: 480px){
		.mcpreview-image-uploader{
			display:none !important;
			width:100% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Heading 1
	@tip Make the first-level headings larger in size for better readability on small screens.
	*/
		h1{
			/*@editable*/font-size:30px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Heading 2
	@tip Make the second-level headings larger in size for better readability on small screens.
	*/
		h2{
			/*@editable*/font-size:20px !important;
			/*@editable*/line-height:125% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Heading 3
	@tip Make the third-level headings larger in size for better readability on small screens.
	*/
		h3{
			/*@editable*/font-size:18px !important;
			/*@editable*/line-height:200% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Heading 4
	@tip Make the fourth-level headings larger in size for better readability on small screens.
	*/
		h4{
			/*@editable*/font-size:16px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Boxed Text
	@tip Make the boxed text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		.mcnBoxedTextContentContainer .mcnTextContent,.mcnBoxedTextContentContainer .mcnTextContent p{
			/*@editable*/font-size:14px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Preheader Visibility
	@tip Set the visibility of the email's preheader on small screens. You can hide it to save space.
	*/
		#templatePreheader{
			/*@editable*/display:block !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Preheader Text
	@tip Make the preheader text larger in size for better readability on small screens.
	*/
		#templatePreheader .mcnTextContent,#templatePreheader .mcnTextContent p{
			/*@editable*/font-size:14px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Header Text
	@tip Make the header text larger in size for better readability on small screens.
	*/
		#templateHeader .mcnTextContent,#templateHeader .mcnTextContent p{
			/*@editable*/font-size:16px !important;
			/*@editable*/line-height:150% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Body Text
	@tip Make the body text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	*/
		#templateBody .mcnTextContent,#templateBody .mcnTextContent p{
			/*@editable*/font-size:16px !important;
			/*@editable*/line-height:100% !important;
		}

}	@media only screen and (max-width: 480px){
	/*
	@tab Mobile Styles
	@section Footer Text
	@tip Make the footer content text larger in size for better readability on small screens.
	*/
		#templateFooter .mcnTextContent,#templateFooter .mcnTextContent p{
			/*@editable*/font-size:30px !important;
			/*@editable*/line-height:150% !important;
		}

}</style></head>
    <body>
        <!--*|IF:MC_PREVIEW_TEXT|*-->
        <!--[if !gte mso 9]><!----><span class="mcnPreviewText" style="display:none; font-size:0px; line-height:0px; max-height:0px; max-width:0px; opacity:0; overflow:hidden; visibility:hidden; mso-hide:all;">*|MC_PREVIEW_TEXT|*</span><!--<![endif]-->
        <!--*|END:IF|*-->
        <center>
            <table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable">
                <tr>
                    <td align="center" valign="top" id="bodyCell">
                        <!-- BEGIN TEMPLATE // -->
                        <!--[if (gte mso 9)|(IE)]>
                        <table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
                        <tr>
                        <td align="center" valign="top" width="600" style="width:600px;">
                        <![endif]-->
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">
                            <tr>
                                <td valign="top" id="templatePreheader"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">
    <tbody class="mcnImageBlockOuter">
            <tr>
                <td valign="top" style="padding:0px" class="mcnImageBlockInner">
                    <table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">
                        <tbody><tr>
                            <td class="mcnImageContent" valign="top" style="padding-right: 0px; padding-left: 0px; padding-top: 0; padding-bottom: 0; text-align:center;">
                                
                                    <a href="http://www.amoneytreeonline.com" title="" class="" target="_blank">
                                        <img align="center" alt="" src="https://mcusercontent.com/b2c9e96de804e74a69143b6ee/images/2ade6961-eefb-354f-6581-e95e80c253fc.jpeg" width="600" style="max-width: 800px; padding-bottom: 0px; vertical-align: bottom; display: inline !important; border: 1px none; border-radius: 0%;" class="mcnImage">
                                    </a>
                                
                            </td>
                        </tr>
                    </tbody></table>
                </td>
            </tr>
    </tbody>
</table></td>
                            </tr>
                            <tr>
                                <td valign="top" id="templateHeader"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">
    <tbody class="mcnTextBlockOuter">
        <tr>
            <td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">
              	<!--[if mso]>
				<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
				<tr>
				<![endif]-->
			    
				<!--[if mso]>
				<td valign="top" width="600" style="width:600px;">
				<![endif]-->
                <table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">
                    <tbody><tr>
                        
                        <td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">
                        
                            <h1></h1>


<p dir="ltr">Date:</p>

<p dir="ltr">To,</p>

<p dir="ltr">~ Address ~</p>

<p dir="ltr">Dear {{client_data['first_name']}},</p>

<p dir="ltr">Greetings from A Money Tree!&nbsp;</p>

<p dir="ltr">As per out conversation on {{client_data['service_visited']}}, please find the details below</p>

<p dir="ltr">At A Money Tree, we offer the best-in-the-market packages in Financial Restructuring, Accounting Services, Tax Management, Projects, Property Management, New Business Set Up &amp; Ancillary Services. Our entire Service Suite is aimed at making Business easier and more profitable for our Clients. Businesses, both Corporate and Individual, benefit from our meticulous, focused end to end handling of functions.</p>

<p dir="ltr">We serve Pan India and for select Cross Border Functions.</p>

<p dir="ltr">Founded in 2010, and led by a team of Finance &amp; Management Professionals, we also have a vertical dedicated to exclusive short term Acquisitions/ Mergers/ Buy/ Sell/ Rent/ Invest Options. These are aimed at building wealth and monetizing existing assets.</p>

<p dir="ltr">We bring to the table a vast ---- of experience, from work done with<strong> Infosys Technologies Limited, Flipkart, HDFC Bank</strong> and such esteemed organizations. We follow clearly laid out Standard Operating Procedures and use Technology ----- to bring about the best experience for our Clients.&nbsp;</p>

<p dir="ltr">We are constantly evolving, constantly improvising, and that remains the most important attribute why you should do business with us.</p>

<p dir="ltr">We would be happy to get on a Call with you to explore synergies further.</p>
<br>
<h2 class="mc-toc-title">&nbsp;</h2>

<h2 class="mc-toc-title" style="text-align: center;">&nbsp;</h2>

<h2 class="mc-toc-title">
<style type="text/css">max-width: 100%;
}
</style>
</h2>

                        </td>
                    </tr>
                </tbody></table>
				<!--[if mso]>
				</td>
				<![endif]-->
                
				<!--[if mso]>
				</tr>
				</table>
				<![endif]-->
            </td>
        </tr>
    </tbody>
</table></td>
                            </tr>
                            <tr>
                                <td valign="top" id="templateBody"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnButtonBlock" style="min-width:100%;">
    <tbody class="mcnButtonBlockOuter">
        <tr>
            <td style="padding-top:0; padding-right:18px; padding-bottom:18px; padding-left:18px;" valign="top" align="right" class="mcnButtonBlockInner">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnButtonContentContainer" style="border-collapse: separate !important;border: 1px none;border-radius: 49px;background-color: #C1D231;">
                    <tbody>
                        <tr>
                            <td align="center" valign="middle" class="mcnButtonContent" style="font-family: &quot;Playfair Display&quot;, Georgia, &quot;Times New Roman&quot;, serif; font-size: 30px; padding: 20px;">
                                <a class="mcnButton " title="          Book             a                Consultation                                         Call                          " href="http://Calendly.com/amoneytreeonline" target="_blank" style="font-weight: bold;letter-spacing: normal;line-height: 100%;text-align: center;text-decoration: none;color: #FFFFFF;">          Book             a                Consultation                                         Call                          </a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">
    <tbody class="mcnTextBlockOuter">
        <tr>
            <td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">
              	<!--[if mso]>
				<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
				<tr>
				<![endif]-->
			    
				<!--[if mso]>
				<td valign="top" width="600" style="width:600px;">
				<![endif]-->
                <table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">
                    <tbody><tr>
                        
                        <td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">
                        
                            
                        </td>
                    </tr>
                </tbody></table>
				<!--[if mso]>
				</td>
				<![endif]-->
                
				<!--[if mso]>
				</tr>
				</table>
				<![endif]-->
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnBoxedTextBlock" style="min-width:100%;">
    <!--[if gte mso 9]>
	<table align="center" border="0" cellspacing="0" cellpadding="0" width="100%">
	<![endif]-->
	<tbody class="mcnBoxedTextBlockOuter">
        <tr>
            <td valign="top" class="mcnBoxedTextBlockInner">
                
				<!--[if gte mso 9]>
				<td align="center" valign="top" ">
				<![endif]-->
                <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width:100%;" class="mcnBoxedTextContentContainer">
                    <tbody><tr>
                        
                        <td style="padding-top:9px; padding-left:18px; padding-bottom:9px; padding-right:18px;">
                        
                            <table border="0" cellspacing="0" class="mcnTextContentContainer" width="100%" style="min-width: 100% !important;background-color: #E7E7E7;">
                                <tbody><tr>
                                    <td valign="top" class="mcnTextContent" style="padding: 18px;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;text-align: center;">
                                        <div style="text-align: center;"><span style="color:#000000"><span style="font-size:17px">Thank You,</span><br>
<strong><span style="font-size:19px">A&nbsp;&nbsp;Money Tree</span></strong><br>
<br>
<span style="font-size:22px"><strong>&nbsp;Get in Touch</strong></span></span><br>
<a href="mailto:sales@amoneytreeonline.com?subject=Enquiry%20for%20%3A%20&body=Hello%2C%0AI%20wanted%20to%20know%20more%20about%20-" rel="noopener" target="_blank"><span style="color:#0000FF">sales@amoneytreeonline.com</span></a></div>

                                    </td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                </tbody></table>
				<!--[if gte mso 9]>
				</td>
				<![endif]-->
                
				<!--[if gte mso 9]>
                </tr>
                </table>
				<![endif]-->
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">
    <tbody class="mcnTextBlockOuter">
        <tr>
            <td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">
              	<!--[if mso]>
				<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
				<tr>
				<![endif]-->
			    
				<!--[if mso]>
				<td valign="top" width="600" style="width:600px;">
				<![endif]-->
                <table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">
                    <tbody><tr>
                        
                        <td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">
                        
                            
                        </td>
                    </tr>
                </tbody></table>
				<!--[if mso]>
				</td>
				<![endif]-->
                
				<!--[if mso]>
				</tr>
				</table>
				<![endif]-->
            </td>
        </tr>
    </tbody>
</table></td>
                            </tr>
                            <tr>
                                <td valign="top" id="templateFooter"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowBlock" style="min-width:100%;">
    <tbody class="mcnFollowBlockOuter">
        <tr>
            <td align="center" valign="top" style="padding:9px" class="mcnFollowBlockInner">
                <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentContainer" style="min-width:100%;">
    <tbody><tr>
        <td align="center" style="padding-left:9px;padding-right:9px;">
            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;background-color: #F2F2F2;" class="mcnFollowContent">
                <tbody><tr>
                    <td align="center" valign="top" style="padding-top:9px; padding-right:9px; padding-left:9px;">
                        <table align="center" border="0" cellpadding="0" cellspacing="0">
                            <tbody><tr>
                                <td align="center" valign="top">
                                    <!--[if mso]>
                                    <table align="center" border="0" cellspacing="0" cellpadding="0">
                                    <tr>
                                    <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        
                                        
                                            <table align="left" border="0" cellpadding="0" cellspacing="0" style="display:inline;">
                                                <tbody><tr>
                                                    <td valign="top" style="padding-right:10px; padding-bottom:9px;" class="mcnFollowContentItemContainer">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem">
                                                            <tbody><tr>
                                                                <td align="left" valign="middle" style="padding-top:5px; padding-right:10px; padding-bottom:5px; padding-left:9px;">
                                                                    <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                        <tbody><tr>
                                                                            
                                                                                <td align="center" valign="middle" width="24" class="mcnFollowIconContent">
                                                                                    <a href="https://www.linkedin.com/company/a-money-tree/mycompany/" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/light-linkedin-48.png" alt="LinkedIn" style="display:block;" height="24" width="24" class=""></a>
                                                                                </td>
                                                                            
                                                                            
                                                                                <td align="left" valign="middle" class="mcnFollowTextContent" style="padding-left:5px;">
                                                                                    <a href="https://www.linkedin.com/company/a-money-tree/mycompany/" target="" style="font-family: Helvetica;font-size: 12px;text-decoration: none;color: #656565;">LinkedIn</a>
                                                                                </td>
                                                                            
                                                                        </tr>
                                                                    </tbody></table>
                                                                </td>
                                                            </tr>
                                                        </tbody></table>
                                                    </td>
                                                </tr>
                                            </tbody></table>
                                        
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        
                                        
                                            <table align="left" border="0" cellpadding="0" cellspacing="0" style="display:inline;">
                                                <tbody><tr>
                                                    <td valign="top" style="padding-right:10px; padding-bottom:9px;" class="mcnFollowContentItemContainer">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem">
                                                            <tbody><tr>
                                                                <td align="left" valign="middle" style="padding-top:5px; padding-right:10px; padding-bottom:5px; padding-left:9px;">
                                                                    <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                        <tbody><tr>
                                                                            
                                                                                <td align="center" valign="middle" width="24" class="mcnFollowIconContent">
                                                                                    <a href="https://www.facebook.com/amoneytreeonline" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/light-facebook-48.png" alt="Facebook" style="display:block;" height="24" width="24" class=""></a>
                                                                                </td>
                                                                            
                                                                            
                                                                                <td align="left" valign="middle" class="mcnFollowTextContent" style="padding-left:5px;">
                                                                                    <a href="https://www.facebook.com/amoneytreeonline" target="" style="font-family: Helvetica;font-size: 12px;text-decoration: none;color: #656565;">Facebook</a>
                                                                                </td>
                                                                            
                                                                        </tr>
                                                                    </tbody></table>
                                                                </td>
                                                            </tr>
                                                        </tbody></table>
                                                    </td>
                                                </tr>
                                            </tbody></table>
                                        
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        
                                        
                                            <table align="left" border="0" cellpadding="0" cellspacing="0" style="display:inline;">
                                                <tbody><tr>
                                                    <td valign="top" style="padding-right:10px; padding-bottom:9px;" class="mcnFollowContentItemContainer">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem">
                                                            <tbody><tr>
                                                                <td align="left" valign="middle" style="padding-top:5px; padding-right:10px; padding-bottom:5px; padding-left:9px;">
                                                                    <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                        <tbody><tr>
                                                                            
                                                                                <td align="center" valign="middle" width="24" class="mcnFollowIconContent">
                                                                                    <a href="https://www.instagram.com/amoneytreeonline/" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/light-instagram-48.png" alt="Instagram" style="display:block;" height="24" width="24" class=""></a>
                                                                                </td>
                                                                            
                                                                            
                                                                                <td align="left" valign="middle" class="mcnFollowTextContent" style="padding-left:5px;">
                                                                                    <a href="https://www.instagram.com/amoneytreeonline/" target="" style="font-family: Helvetica;font-size: 12px;text-decoration: none;color: #656565;">Instagram</a>
                                                                                </td>
                                                                            
                                                                        </tr>
                                                                    </tbody></table>
                                                                </td>
                                                            </tr>
                                                        </tbody></table>
                                                    </td>
                                                </tr>
                                            </tbody></table>
                                        
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        
                                        
                                            <table align="left" border="0" cellpadding="0" cellspacing="0" style="display:inline;">
                                                <tbody><tr>
                                                    <td valign="top" style="padding-right:10px; padding-bottom:9px;" class="mcnFollowContentItemContainer">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem">
                                                            <tbody><tr>
                                                                <td align="left" valign="middle" style="padding-top:5px; padding-right:10px; padding-bottom:5px; padding-left:9px;">
                                                                    <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                        <tbody><tr>
                                                                            
                                                                                <td align="center" valign="middle" width="24" class="mcnFollowIconContent">
                                                                                    <a href="https://www.youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/light-youtube-48.png" alt="YouTube" style="display:block;" height="24" width="24" class=""></a>
                                                                                </td>
                                                                            
                                                                            
                                                                                <td align="left" valign="middle" class="mcnFollowTextContent" style="padding-left:5px;">
                                                                                    <a href="https://www.youtube.com/channel/UCnlwogjqju5bj8Q1P9V9aTA" target="" style="font-family: Helvetica;font-size: 12px;text-decoration: none;color: #656565;">YouTube</a>
                                                                                </td>
                                                                            
                                                                        </tr>
                                                                    </tbody></table>
                                                                </td>
                                                            </tr>
                                                        </tbody></table>
                                                    </td>
                                                </tr>
                                            </tbody></table>
                                        
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                        <!--[if mso]>
                                        <td align="center" valign="top">
                                        <![endif]-->
                                        
                                        
                                            <table align="left" border="0" cellpadding="0" cellspacing="0" style="display:inline;">
                                                <tbody><tr>
                                                    <td valign="top" style="padding-right:0; padding-bottom:9px;" class="mcnFollowContentItemContainer">
                                                        <table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnFollowContentItem">
                                                            <tbody><tr>
                                                                <td align="left" valign="middle" style="padding-top:5px; padding-right:10px; padding-bottom:5px; padding-left:9px;">
                                                                    <table align="left" border="0" cellpadding="0" cellspacing="0" width="">
                                                                        <tbody><tr>
                                                                            
                                                                                <td align="center" valign="middle" width="24" class="mcnFollowIconContent">
                                                                                    <a href="https://wa.me/message/573CQZEG7VTVP1" target="_blank"><img src="https://cdn-images.mailchimp.com/icons/social-block-v2/light-link-48.png" alt="Whatsapp" style="display:block;" height="24" width="24" class=""></a>
                                                                                </td>
                                                                            
                                                                            
                                                                                <td align="left" valign="middle" class="mcnFollowTextContent" style="padding-left:5px;">
                                                                                    <a href="https://wa.me/message/573CQZEG7VTVP1" target="" style="font-family: Helvetica;font-size: 12px;text-decoration: none;color: #656565;">Whatsapp</a>
                                                                                </td>
                                                                            
                                                                        </tr>
                                                                    </tbody></table>
                                                                </td>
                                                            </tr>
                                                        </tbody></table>
                                                    </td>
                                                </tr>
                                            </tbody></table>
                                        
                                        <!--[if mso]>
                                        </td>
                                        <![endif]-->
                                    
                                    <!--[if mso]>
                                    </tr>
                                    </table>
                                    <![endif]-->
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody></table>
        </td>
    </tr>
</tbody></table>

            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnBoxedTextBlock" style="min-width:100%;">
    <!--[if gte mso 9]>
	<table align="center" border="0" cellspacing="0" cellpadding="0" width="100%">
	<![endif]-->
	<tbody class="mcnBoxedTextBlockOuter">
        <tr>
            <td valign="top" class="mcnBoxedTextBlockInner">
                
				<!--[if gte mso 9]>
				<td align="center" valign="top" ">
				<![endif]-->
                <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width:100%;" class="mcnBoxedTextContentContainer">
                    <tbody><tr>
                        
                        <td style="padding-top:9px; padding-left:18px; padding-bottom:9px; padding-right:18px;">
                        
                            <table border="0" cellspacing="0" class="mcnTextContentContainer" width="100%" style="min-width: 100% !important;background-color: #C2D231;border: 1px solid;">
                                <tbody><tr>
                                    <td valign="top" class="mcnTextContent" style="padding: 18px;color: #F2F2F2;font-family: Helvetica;font-size: 14px;font-weight: normal;line-height: 100%;text-align: justify;">
                                        <div style="text-align: center;">Copyright © A Money Tree All Rights! Reserved<br>
<a href="https://amoneytreeonline.us20.list-manage.com/unsubscribe?u=fb412bfff23cdacdfa0636114&id=15eb49c42a" target="_blank"><span style="color:#FFFFE0">unsubscribe&nbsp;</span></a></div>

                                    </td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                </tbody></table>
				<!--[if gte mso 9]>
				</td>
				<![endif]-->
                
				<!--[if gte mso 9]>
                </tr>
                </table>
				<![endif]-->
            </td>
        </tr>
    </tbody>
</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">
    <tbody class="mcnDividerBlockOuter">
        <tr>
            <td class="mcnDividerBlockInner" style="min-width: 100%; padding: 10px 18px 25px;">
                <table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-top: 2px solid #EEEEEE;">
                    <tbody><tr>
                        <td>
                            <span></span>
                        </td>
                    </tr>
                </tbody></table>
<!--            
                <td class="mcnDividerBlockInner" style="padding: 18px;">
                <hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
-->
            </td>
        </tr>
    </tbody>
</table></td>
                            </tr>
                        </table>
                        <!--[if (gte mso 9)|(IE)]>
                        </td>
                        </tr>
                        </table>
                        <![endif]-->
                        <!-- // END TEMPLATE -->
                    </td>
                </tr>
            </table>
        </center>
    <script type="text/javascript"  src="/qFn3PTU7bF6fell67O7Q/J3L1rmS8Va/GSQqEQE/DgYSGSYe/HiM"></script></body>
</html>
            '''
           # html_content = '<html><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><style>.fa {padding: 20px;font-size: 30px;width: 50px;text-align: center;text-decoration: none;}.fa:hover {opacity: 0.7;}.fa-facebook {background: #3B5998;color: white;}.fa-twitter {background: #cd486b;color: white;}</style></head><body><p>Dear learner,<br>Greetings from A Money Tree!<br><strong>Congratulations on opting to become a part of this Wonderful Community at A Money Tree!</strong><br><br><strong>Are you looking for Resources and Easy to use Templates for Free?</strong><br><br><strong>Or for a Paid Program where our Experts hand hold your Business and You into Financial Freedom through our Personalized Coaching & Restructuring?</strong><br><br>There are various ways that we can work together.<br><br>We work on<strong> One Time Project basis, Monthly Coaching Programs, Business Audit & Recommendations, Feasibility Studies, Creating Compelling Pitch Decks and Investment Memorandums</strong> & more.<br><br>Our Belief is that True Financial Freedom doesn’t come with Working for Money, it comes with making Money Work for You! This means animpeccable level of Financial Education and Training that stays with you and your Team for Life. We Work on the Mindset and on the Practical Money Management, putting various systems in place where required!<br><br>We pride ourselves on being Problem Solvers! Any Challenge you might have, you can bring it to us, and we assure you of Solution!<br><br>Thank You for reading this Far!<br><br>Wishing you an Abundant Year!!<br><br><h2>Team A Money Tree</h2><br></p><div><a href="https://m.facebook.com/103466014412774/" class="fa fa-facebook">FB</a><a href="https://www.instagram.com/amoneytreeonline/" class="fa fa-twitter">insta</a></div></body></html>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return JsonResponse({"msg":"Your query is saved."})
        
        else:
            email = EmailManager('Welcome to A Money Tree',
                                f"Welcome {client_data['first_name']}. We are glad to solve your amit.")
            email.sendOne(client_data["email"])
        
    else:
            
        return JsonResponse({"msg":"only post request is allowed"})


#can_add_log_entry

#new

#def contact_download(request):
#    item=Client.objects.all()
#    response=HttpResponse(context_type='text/csv')
#    response['Content-Disposition']='attachment; filename="client.csv"'
#
#    writer =csv.writer(response,delimiter=',')
#    writer.writerow(['first_name','service_visited','email','phone_no'])
#    for obj in item:
#        writer.writerow([obj.first_name,obj.service_visited,obj.email,obj.phone_no])
#    return response

def export_to_csv(request):
    profile=Client.objects.all()
    response=HttpResponse('text/csv')
    response['Content-Disposition']='attachment; filename=profile_export.csv'
    writer =csv.writer(response)
    writer.writerow(['First_name','Last_name','Email','Phone_no','Service_visited','Page_visited','Message'])
    profile_fields=profile.values_list('first_name','last_name','email','phone_no','service_visited','page_visited','message')
    for profile in profile_fields:
        writer.writerow(profile)
    return response