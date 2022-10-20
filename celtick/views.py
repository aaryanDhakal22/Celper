from django.shortcuts import render
from .models import Ticket
from .email_manager import *

# Create your views here.
def ticket_page(request):
    new_email = all_mails().splitlines()
    new_ticket = dict()

    for items in new_email:
        packets = items.split()
        new_ticket.setdefault(packets[0].lower(), " ".join(packets[2:]))
    if len(Ticket.objects.filter(id=new_ticket["id"])) == 0:
        Ticket.objects.create(
            id=new_ticket["id"],
            printer_model=new_ticket["printer-model"],
            toner_color=new_ticket["color"],
            requested_by=new_ticket["requested-by"],
            location=new_ticket["location"],
        )

    tickets = Ticket.objects.all()
    return render(request, "tickets.html", context={"tickets": tickets})
