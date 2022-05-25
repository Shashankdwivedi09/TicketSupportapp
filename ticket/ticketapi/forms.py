from django import forms

class NewTicketForm(forms.Form):
    department = forms.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=150, blank=True)
    status = models.CharField(choices=status, max_length=155, default="pending")
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)