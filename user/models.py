from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=40, unique=True, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=130, verbose_name='유저 비밀번호')
    user_pw_confirm = models.CharField(max_length=130, verbose_name='비밀번호 확인', null=True)
    user_name = models.CharField(max_length=20, unique=True, verbose_name='유저 이름')
    user_email = models.EmailField(max_length=130, unique=True, verbose_name='유저 이메일')
    user_register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='계정 생성시간')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'sign_up'
        verbose_name = '유저관리'
        verbose_name_plural = '유저관리'