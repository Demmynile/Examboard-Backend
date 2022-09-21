from django.db import models


# creating a payment model


class Payment(models.Model):
    EventsType = (
        ('1', 'M.C'),
        ('2', 'P.S')
    )
    pinNo = models.TextField()
    name = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    amount = models.CharField(null=True, max_length=255)
    transactionRef = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    bulknumber = models.BigIntegerField(null=True)
    ExamType = models.CharField(
        max_length=100, choices=EventsType, null=True, default=0, blank=True)

    def __str__(self):
        return self.pinNo
    #    return  f"{self.pinNo}"

    def save(self, *args, **kwargs):
        self.update()
        super().save(*args, **kwargs)

    def update(self):
        # self.TotalPrice= self.StudentNumber * 4
        if(self.ExamType == '1'):
            self.amount = self.bulknumber * 4
        elif(self.ExamType == '2'):
            self.amount = self.bulknumber * 3
        # elif(self.ExamType == '2'):
        #     self.TotalPrice = self.StudentNumber * 5
