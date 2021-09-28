from django.db import models

# Create your models here.

class Member(models.Model):
    memberid=models.CharField(max_length=64, verbose_name='아이디', primary_key=True)
    membername = models.CharField(max_length=64, verbose_name='사용자명', null=False)
    memberpw = models.CharField(max_length=64, verbose_name='비밀번호', null=False)
    registered = models.DateTimeField(auto_now_add=True, verbose_name='등록 일자')
    GENDERS = (('M','남성(Man'),('W','여성(Woman'))
    gender = models.CharField(max_length=1, verbose_name='성별', choices=GENDERS, default='M')
    memberemail = models.EmailField(max_length=128, verbose_name='사용자 이메일', null=False)
    memberprofile =models.TextField(max_length=100, null=True, verbose_name='자기소개', default='자기소개를 작성해보세요^_^')
    def __str__(self):
        return self.membername

# 강의
class Lecture(models.Model):
    lectureid=models.AutoField(primary_key=True)
    # 강의 이름(이미지)
    lectureName=models.CharField(max_length=64, verbose_name='강의이름', null=False, unique=True)
    lectureregistered = models.DateTimeField(auto_now_add=True, verbose_name='등록 일자')
    # 보여줄 강의 이름
    lectureho = models.CharField(max_length=100, verbose_name="별명", null=True)
    # 강의 등록한 사람
    lecture_registrant = models.CharField(max_length=64, verbose_name="등록자",null=True)
    lecture_memo = models.TextField(max_length=1000,null=True, verbose_name='강의 소개', default='강의 소개')
    def __str__(self):
        return self.lectureho
# 회원_강의
class Member_Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    member_id=models.ForeignKey("Member",related_name="member",on_delete=models.CASCADE,db_column="memberid")
    lecture_id=models.ForeignKey("Lecture",related_name="lecture",on_delete=models.CASCADE,db_column="lectureid")
