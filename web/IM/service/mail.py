
import smtplib
import traceback

sender = 'inventory_management@emc.com'

message = """From: From ###Person """+sender+"""
To: To Person <to@todomain.com>
Subject: SMTP e-mail notice

This is a notice e-mail message from Inventory Management.
"""
class Mail(object):
    @staticmethod
    def send_mail(inv_id, msg):
        try:
            smtpObj = smtplib.SMTP('127.0.0.1', 1025)
            smtpObj.sendmail(sender, Mail.get_receivers(inv_id), Mail.get_msg(inv_id, msg))  
            print message       
            print "Successfully sent email"
        except Exception:
            print "Error: unable to send email"
            print traceback.print_exc()
    @staticmethod        
    def get_receivers(inv_id):
        receivers=[]
        return receivers
    
    @staticmethod
    def get_msg(inv_id, msg):
        msg=""" sss """+msg
        return message+msg
        
        
    
        
