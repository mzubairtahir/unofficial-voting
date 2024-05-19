from django.db import models

# Create your models here.

class Party(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    picture = models.CharField(max_length=500, unique = True)

    code = models.CharField(max_length = 30, unique = True)


    def __str__(self) -> str:
        return str(self.name)







class Vote(models.Model):

    voter_name = models.CharField(max_length = 100)
    voter_email = models.EmailField(unique = True)
    voter_ip = models.CharField(max_length = 15, unique= True)
    voted_party = models.ForeignKey(Party, on_delete = models.CASCADE)
    



    def __str__(self) -> str:
        return str(self.voter_name)
