from django.db import models

# Create your models here.

class Books(models.Model):  
    title = models.CharField(max_length = 100) 
    author = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 10)
    ISBN = models.CharField(max_length = 10)
    availability_status = models.BooleanField()
    
    def __str__(self):
        return self.title

class Patron(models.Model):
    name = models.CharField(max_length = 30)
    contact_info = models.IntegerField(max_length = 10)
    membership_id = models.Index(max_length = 7)
    
    def __str__(self):
        return self.membership_id
    
class Borrowing(models.Model):
    title = models.ForeignKey(Books, on_delete=models.CASCADE)
    name = models.ForeignKey(Patron, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(Patron, on_delete=models.CASCADE)
    membership_id = models.ForeignKey(Patron, on_delete=models.CASCADE)
    borrowing_date = models.DateTimeField(auto_now_add = True)
    return_date = models.DateTimeField(auto_now_add = False)
    
    def __str__(self):
        return self.return_date