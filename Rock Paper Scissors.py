game_dic = {"rock" : 1, "paper" : 2, "scissors" : 3}
while(True) :
    player_1st = game_dic.get(input("1st player choice : "))
    player_2nd = game_dic.get(input("2nd player choice : "))

    input_ver = (player_1st - player_2nd)
    if input_ver == -2 :
        print("1st player win !!")
    elif input_ver == -1 :
        print("2nd player win !!")
    elif input_ver == 1 :
        print("1st player win !!")
    elif input_ver == 2 :
        print("2nd player win !!")
    elif input_ver == 0 :
        print("Match is Draw !!")
    else :
        print("worng input")