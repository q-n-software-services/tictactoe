from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import time
import random

# Create your views here.
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


player1 = 'X'
player2 = 'o'
choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

game_still_going = True
winner = None
current_player = player1
stuff_for_frontend = {'results': [], 'btn1': '-', 'btn2': '-', 'btn3': '-', 'btn4': '-', 'btn5': '-', 'btn6': '-', 'btn7': '-',
                      'btn8': '-', 'btn9': '-'}

@csrf_exempt
def gameprogress(request):
    global stuff_for_frontend
    results = models.results.objects.all().order_by("-added_date")
    stuff_for_frontend['results'] = results
    return render(request, 'base.html', stuff_for_frontend)


def show_totals():
    global winner

    if winner == player1 or winner == player2:
        date = timezone.now()
        text = "\t \t" + winner + "    won"

        models.results.objects.create(added_date=date, text=text)
    elif winner is None:
        date = timezone.now()
        text = "    \t \t Tie     "
        models.results.objects.create(added_date=date, text=text)


@csrf_exempt
def play(request):
    new_game()
    global stuff_for_frontend
    results = models.results.objects.all().order_by("-added_date")
    stuff_for_frontend['results'] = results
    return render(request, 'base.html', stuff_for_frontend)


@csrf_exempt
def delete_results(request):
    models.results.objects.all().delete()
    global stuff_for_frontend
    results = models.results.objects.all().order_by("-added_date")
    stuff_for_frontend['results'] = results
    return render(request, 'base.html', stuff_for_frontend)


'''def gaming_bot(request):
    global choices
    global board
    global stuff_for_frontend
    global player2
    time.sleep(1)
    x = len(choices)
    c = random.randint(0, x-1)
    n = choices.pop(c)
    board[n] = player2
    k = 'btn' + str(n)
    stuff_for_frontend[k] = player2
    results = models.results.objects.all().order_by("-added_date")
    stuff_for_frontend['results'] = results
    return render(request, 'base.html', stuff_for_frontend)'''


def new_game():
    global board
    global winner
    global game_still_going
    global current_player
    global player1
    global player2
    global stuff_for_frontend
    global choices

    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    stuff_for_frontend['btn1'] = "-"
    stuff_for_frontend['btn2'] = "-"
    stuff_for_frontend['btn3'] = "-"
    stuff_for_frontend['btn4'] = "-"
    stuff_for_frontend['btn5'] = "-"
    stuff_for_frontend['btn6'] = "-"
    stuff_for_frontend['btn7'] = "-"
    stuff_for_frontend['btn8'] = "-"
    stuff_for_frontend['btn9'] = "-"
    winner = None
    game_still_going = True
    current_player = player1
    choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]






@csrf_exempt
def handle_turn(request, address):
    global current_player
    global player1
    global player2
    global stuff_for_frontend
    global game_still_going


    position = address
    position = int(position) - 1
    if board[position] != "-":
        results = models.results.objects.all().order_by("-added_date")
        stuff_for_frontend['results'] = results
        return render(request, 'base.html', stuff_for_frontend)

    board[position] = current_player
    if address == 1:
        stuff_for_frontend['btn1'] = current_player
    elif address == 2:
        stuff_for_frontend['btn2'] = current_player
    elif address == 3:
        stuff_for_frontend['btn3'] = current_player
    elif address == 4:
        stuff_for_frontend['btn4'] = current_player
    elif address == 5:
        stuff_for_frontend['btn5'] = current_player
    elif address == 6:
        stuff_for_frontend['btn6'] = current_player
    elif address == 7:
        stuff_for_frontend['btn7'] = current_player
    elif address == 8:
        stuff_for_frontend['btn8'] = current_player
    elif address == 9:
        stuff_for_frontend['btn9'] = current_player

    if current_player == player1:
        current_player = player2
    elif current_player == player2:
        current_player = player1

    check_if_game_over()
    if game_still_going is False:
        show_totals()

    results = models.results.objects.all().order_by("-added_date")
    stuff_for_frontend['results'] = results
    return render(request, 'base.html', stuff_for_frontend)





def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going

    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2 :
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
