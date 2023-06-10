from django.db import models

class Todo_list(models.Model):
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    todo_content = models.CharField(max_length=500)
    #여기서 부터 다시 시작
    def __str__(self):
        return self.todo_content
    
    class Meta:
        db_table = 'todo_item'
        verbose_name = '투두아이템'
        verbose_name_plural = '투두아이템'