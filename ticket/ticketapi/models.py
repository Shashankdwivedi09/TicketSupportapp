from django.db import models
import uuid
from django.contrib.auth.models import User

#status = (
#("PENDING", "Pending"),
#("CLOSED", "Closed"),
#)

priorty = (
    ("HIGH", "high"),
    ("MEDIUM", "medium"),
    ("LOW", "low"),
)


#def generate_ticket_id():
 #   return str(uuid.uuid4()).split("-")[-1]

class Ticket(models.Model):
    department = models.CharField(max_length=200)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    priorty = models.CharField(choices=priorty)
    #ticket_id = models.CharField(max_length=150, blank=True)
    #status = models.CharField(choices=status, max_length=155, default="pending")
    #created = models.DateTimeField(auto_now=True)
    #modified = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return "{} - {}".format(self.title, self.ticket_id)

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = generate_ticket_id()

        super(Ticket, self).save(*args, **kwargs) #initializes the save() function method

    class Meta:
        ordering = ["-created"]

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name