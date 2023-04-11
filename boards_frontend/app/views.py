from django.shortcuts import render, redirect
import requests
import json

# Create your views here.
def boards_list(request):
    backend_url = 'http://127.0.0.1:8000/'
    headers = {'Content-Type':'Application/json'}
    response = requests.get(backend_url, headers=headers)
    print(response)
    boards = response.json()
    return render(request, 'home.html', {'boards': boards})
    

def board_topics(request, board_id):
    backend_url = "http://127.0.0.1:8000/boards/"+str(board_id)+"/"
    headers = {'Content-Type':'Application/json'}
    response = requests.get(backend_url, headers=headers)
    response_data = response.json()
    
    response_board = requests.get("http://127.0.0.1:8000/board_detail/" + str(board_id) + "/", headers=headers)
    board_details = response_board.json()
    
    
    return render(request, 'topics.html', {'board': board_details,'topics':response_data})

def new_topic(request, board_id):
    
    headers = {'Content-Type':'Application/json'}
    response_board = requests.get("http://127.0.0.1:8000/board_detail/" + str(board_id) + "/", headers=headers)
    board_details = response_board.json()

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        created_by = 1
        data = json.dumps({'subject':subject,'message':message, 'created_by':created_by,'board':board_id})
        response_board = requests.post("http://127.0.0.1:8000/boards/" + str(board_id) + "/", headers=headers, data=data)
        # add_topic_res = response_board.json()
        # print(add_topic_res)
        
        return redirect('board_topics', board_id=board_id)
    
    return render(request, 'new_topic.html', {'board': board_details})