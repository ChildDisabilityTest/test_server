from django.db import models

# Create your models here.
class IncheonRegion(models.Model):
    si = models.CharField(max_length=10, null=True, blank=True, help_text="시")
    gu = models.CharField(max_length=10, null=True, blank=True, help_text="구/군")
    emd = models.CharField(max_length=10, null=True, blank=True, help_text="읍면동")

    def __str__(self):
        return self.si + " " + self.gu + " " + self.emd

class Tester(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True, help_text="이름")
    birthDate = models.DateField(null=True, blank=True, help_text="생년월일")
    email = models.EmailField(null=True, blank=True, help_text="이메일")
    privacy_agree = models.BooleanField(default=False, help_text="개인정보수집동의")

    def __str__(self):
        return "[" + str(self.id) + "] " + self.name + "(" + str(self.birthDate) + "," + self.email + ")"

class Child(models.Model):

    GENDER_CHOICES = (
        ('M', '남자'),
        ('F', '여자')
    )

    name = models.CharField(max_length=10, null=True, blank=True, help_text="이름")
    birthDate = models.DateField(null=True, blank=True, help_text="생년월일")
    residence = models.ForeignKey(IncheonRegion, on_delete=models.CASCADE, related_name="residence", null=True, blank=True, help_text="거주지역")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, help_text="성별")
    kindergarden = models.CharField(max_length=20, null=True, blank=True, help_text="유치원 이름")
    testDate = models.DateField(null=True, blank=True, help_text="검사일")
    tester = models.ForeignKey(Tester, on_delete=models.CASCADE, related_name="tester", null=True, blank=True, help_text="검사자")
