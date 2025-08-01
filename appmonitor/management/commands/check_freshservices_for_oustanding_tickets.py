from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import Group
import datetime
from appmonitor import models
from appmonitor import utils
from appmonitor import email_templates
from django.conf import settings
from datetime import datetime
import requests

class Command(BaseCommand):
    help = 'Send Notification for Outstanding Tickets'

    def handle(self, *args, **options):
            print ("Running Ticket Check")
           
            ticket_filters = models.TicketFilter.objects.filter(active=True)
            FRESHSERVICES_API_KEY = settings.FRESHSERVICES_API_KEY
            auth_request = requests.auth.HTTPBasicAuth(FRESHSERVICES_API_KEY, "X")
            ticket_systems = models.TicketSystem.objects.filter(active=True)
            ticket_status = models.TicketStatus.objects.filter(active=True)

            for tf in ticket_filters:         
                tickets_total = 0 
                tickets = []  
                tickets_array = []

                try:
                    tickets = requests.get(tf.url,auth=auth_request)
                    tickets_pending = tickets.json()
                    
                    if "tickets" in tickets_pending:
                        tickets_total = len(tickets_pending['tickets'])
                        for t in tickets_pending['tickets']:
                            ticket_row = {}
                            ticket_row['id']  = t['id']
                            ticket_row['subject'] = t['subject']
                            ticket_row['system_id'] = t['custom_fields']['system_id']
                            ticket_row['lf_system_id'] = t['custom_fields']['lf_system_id']
                            ticket_row['status'] = t['status']

                            print (t['subject'])   
                            nowtime = datetime.now()
                            # print (t)             
                            
                            # created_at = t['created_at'].replace("T"," ")
                            # created_at = created_at.replace("Z","")
                            ticket_created_datetime = datetime.strptime(t['created_at'], '%Y-%m-%dT%H:%M:%SZ')  
                            ticket_row['ticket_created_datetime']  = ticket_created_datetime
                            timediff = nowtime - ticket_created_datetime
                            ticket_row['age'] = timediff.days

                            ticket_updated_datetime = datetime.strptime(t['updated_at'], '%Y-%m-%dT%H:%M:%SZ')                                       
                            ticket_row['ticket_updated_datetime'] = ticket_updated_datetime
                            timediff = nowtime - ticket_updated_datetime
                            ticket_row['age_updated'] = timediff.days

                            ticket_row['updated_at'] = t['updated_at']
                            ticket_row['created_at'] = t['created_at']
                    
                            tickets_array.append(ticket_row)
                except Exception as e:
                    print (e)

                t = email_templates.TicketList()
                t.subject = "Tickets Outstanding for "+str(tf.name) + " (Total: "+str(tickets_total)+")"
                to_addresses=[]
                for notification in models.TicketFilterNotification.objects.filter(active=True,ticket_filter=tf):
                    print ("Preparing to "+notification.email)
                    to_addresses.append(notification.email)
                t.send(to_addresses=to_addresses, context={"tickets": tickets_pending, "tickets_total": tickets_total, "settings": settings, "tickets_array": tickets_array, "ticket_systems" : ticket_systems, "ticket_status": ticket_status, "test": {19: "test1", 17: "test2", 18: "test3"}})        
        

