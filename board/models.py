from django.db import models

class Board(models.Model):
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(max_length=64, verbose_name='글 제목')
    contents = models.TextField(verbose_name='글 내용')
    write_dttm = models.DateTimeField(auto_now_add=True, verbose_name='글 작성일')

    board_name = models.CharField(max_length=32, default='1번', verbose_name='게시판 종류')
    update_dttm = models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')

    is_temporary = models.BooleanField(default=False, verbose_name='임시저장 여부')
    temporary_saved_at = models.DateTimeField(null=True, blank=True, verbose_name='임시저장 시간')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'