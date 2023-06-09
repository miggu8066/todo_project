from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import BoardWriteForm
from .models import Board, TemporaryBoard
from user.models import User
from user.decorators import login_required
from datetime import date, datetime, timedelta
from django.core.paginator import Paginator

@login_required
def board_modify(request, pk):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    board = get_object_or_404(Board, id=pk)
    context['board'] = board

    if board.writer.user_id != login_session:
        return redirect(f'/board/detail/{pk}/')
    
    if request.method == 'GET':
        write_form = BoardWriteForm(instance=board)
        context['forms'] = write_form
        return render(request, 'board/board_modify.html', context)
    
    elif request.method == 'POST':
        if 'save_edit' in request.POST:
            write_form = BoardWriteForm(request.POST)

            if write_form.is_valid():
                
                board.title = write_form.title
                board.contents = write_form.contents
                board.board_name = write_form.board_name

                board.save()
                return redirect('/board')
            else:
                context['forms'] = write_form
                if write_form.errors:
                    for value in write_form.errors.values():
                        context['error'] = value
                return render(request, 'board/board_modify.html', context)
            
        elif 'save_temp' in request.POST:
            write_form = BoardWriteForm(request.POST)

            if write_form.is_valid():
                board.title = write_form.title
                board.contents = write_form.contents
                board.board_name = write_form.board_name

                board.save()
                return redirect(f'/board/detail/{pk}/modify/')
            else:
                context['forms'] = write_form
                if write_form.errors:
                    for value in write_form.errors.values():
                        context['error'] = value
                return render(request, 'board/board_modify.html', context)


def board_delete(request, pk):
    login_session = request.session.get('login_session', '')
    board = get_object_or_404(Board, id=pk)
    if board.writer.user_id == login_session:
        board.delete()
        return redirect('/board')
    else:
        return redirect(f'/board/detail/{pk}/')

def board_detail(request, pk):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    board = get_object_or_404(Board, id=pk)
    context['board'] = board

    if board.writer.user_id == login_session:
        context['writer'] = True
    else:
        context['writer'] = False

    response = render(request, 'board/board_detail.html', context)

    # 조회수 기능 (쿠키 사용)
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get('hitboard','_')

    if f'_{pk}_' not in cookie_value:
        cookie_value += f'{pk}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=max_age, httponly=True)
        board.hits += 1
        board.save()
    return response

def board_list(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    page = request.GET.get('page','1') # 페이지
    all_boards = Board.objects.order_by('-id')

    paginator = Paginator(all_boards, 3) # 페이지당 10개 씩 보여주기
    page_obj = paginator.get_page(page)
    
    context['board_list'] = page_obj
    
    return render(request, 'board/board_list.html', context)

@login_required
def board_write(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    if request.method == 'GET':
        temp_boards = TemporaryBoard.objects.filter(writer__user_id=login_session).order_by('-temporary_saved_at')
        context['temp_boards'] = temp_boards

        temp_board_id = request.GET.get('temp_board_id')
        if temp_board_id:
            temp_board = TemporaryBoard.objects.get(id=temp_board_id)
            initial_data = {
                'title': temp_board.title,
                'contents': temp_board.contents,
                'write_dttm': temp_board.temporary_saved_at,
            }
            write_form = BoardWriteForm(initial=initial_data)
        else:
            write_form = BoardWriteForm()

        context['forms'] = write_form

        return render(request, 'board/board_write.html', context)
    
    elif request.method == 'POST':
        if 'save_write' in request.POST:
            write_form = BoardWriteForm(request.POST)

            if write_form.is_valid():
                writer = User.objects.get(user_id=login_session)
                board = Board(
                    title=write_form.title,
                    contents=write_form.contents,
                    writer=writer,
                    board_name=write_form.board_name
                )
                board.save()

                return redirect('/board')
            
            else:
                context['forms'] = write_form
                if write_form.errors:
                    for value in write_form.errors.values():
                        context['error'] = value
                temp_boards = TemporaryBoard.objects.filter(writer__user_id=login_session).order_by('-temporary_saved_at')
                context['temp_boards'] = temp_boards
                return render(request, 'board/board_write.html', context)
            
        elif 'save_temp' in request.POST:
            write_form = BoardWriteForm(request.POST)

            if write_form.is_valid():
                writer = User.objects.get(user_id=login_session)
                temp_board = TemporaryBoard(
                    title=write_form.title,
                    contents=write_form.contents,
                    writer=writer,
                    temporary_saved_at=datetime.now()
                )
                temp_board.save()
                return redirect(reverse('board:board_write') + '?temp_board_id=' + str(temp_board.id))
            else:
                context['forms'] = write_form
                if write_form.errors:
                    for value in write_form.errors.values():
                        context['error'] = value
                temp_boards = TemporaryBoard.objects.filter(writer__user_id=login_session).order_by('-temporary_saved_at')
                context['temp_boards'] = temp_boards
                return render(request, 'board/board_write.html', context)
        
        elif 'delete_temp' in request.POST:
            delete_temp_id = request.POST.get('delete_temp')
            delete_temp_board = TemporaryBoard.objects.get(id=delete_temp_id)
            delete_temp_board.delete()
            return redirect(reverse('board:board_write'))