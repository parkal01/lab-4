
from django.shortcuts import render,redirect 
from .models import Contacts

from django.shortcuts import render

def home(request):

    return render(request, 'index.html')



def help_page(request):
    return render(request, 'help.html')


def contacts(request):
    # Fetch all contacts from the database
    contact_list = Contacts.objects.order_by('contact_id')
    

    if request.method == 'POST':
        # Retrieve form data
        contact_id = request.POST.get('contact_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Create a new Contact instance and save it to the database
        new_contact = Contacts(contact_id =contact_id ,first_name=first_name, last_name=last_name, email=email)
        new_contact.save()
        
        # Redirect to the contacts page to display the updated list
    
    # Render contacts.html template with contact_list
    return render(request, 'contacts.html', {'contacts': contact_list})



def delete_contact(request, contact_id):
    if request.method == 'POST':
        # Retrieve contact by ID and delete it
        try:
            contact = Contacts.objects.get(contact_id=contact_id)
            contact.delete()
        except Contacts.DoesNotExist:
            pass  # Handle the case where the contact doesn't exist

    return redirect('contacts')

