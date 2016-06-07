GU = 1
CHOKI = 2
PA = 3
DRAW = 1
WIN = 2
LOSE = 3
judge = 0
LOOPCONT = 200

def hand_generate():
    import random
    #randomに出力
    player = random.randint(1, 3)
    cpu = random.randint(1, 3)
    return(player, cpu)


#if9パターン
def janken_list1(player, cpu):
    # GUのi
    if(player == GU and cpu == GU):
        judge = DRAW
    elif(player == GU and cpu == CHOKI):
        judge = WIN
    elif(player == GU and cpu == PA):
        judge = LOSE

    #CHOKIのif
    elif(player == CHOKI and cpu == CHOKI):
        judge = DRAW
    elif(player == CHOKI and cpu == PA):
        judge = WIN
    elif(player == CHOKI and cpu == GU):
        judge = LOSE

    #PAのif
    elif(player == PA and cpu == PA):
        judge = DRAW
    elif(player == PA and cpu == GU):
        judge = WIN
    elif(player == PA and cpu == CHOKI):
        judge = LOSE

    if(judge == DRAW):
        return
    elif(judge == WIN):
        return
    elif(judge == LOSE):
        return


#if3パターン
def janken_list2(player, cpu):
    if (player == cpu):
        judge = DRAW
    elif(player == GU and cpu == CHOKI or
        player == CHOKI and cpu == PA or
        player == PA and cpu == GU):
        judge = WIN
    else:
        judge = LOSE


#計算式パターン
def janken_list3(player, cpu):
    DRAW2 = 0
    WIN2 = 1
    LOSE2 = 2
    judge = (player - cpu + 3) % 3

    if(judge == DRAW2):
        return
    elif(judge == WIN2):
        return
    elif(judge == LOSE2):
        return


#配列パターン
def janken_list4(player, cpu):
    jud = [[DRAW, WIN, LOSE],
           [LOSE, DRAW, WIN],
           [WIN, LOSE, DRAW]]

    if(jud[player - 1][cpu - 1] == DRAW):
        return
    elif(jud[player - 1][cpu - 1] == WIN):
        return
    elif(jud[player - 1][cpu - 1] == LOSE):
        return


#経過時間
if __name__ == '__main__':
    import time
    import sys

    '''
    start = time.time()
    for _ in range(LOOPCONT):
        phand, chand = hand_generate()
        janken_(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('')
    print('elapsed_time', (end - start))
    '''

    #if9パターン
    start = time.time()
    for _ in range(LOOPCONT):
        phand, chand = hand_generate()
        janken_list1(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('if9')
    print('elapsed_time', (end - start))

    #if3パターン
    start = time.time()
    for _ in range(LOOPCONT):
        phand, chand = hand_generate()
        janken_list2(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('if3')
    print('elapsed_time', (end - start))

    #配列パターン
    start = time.time()
    for _ in range(LOOPCONT):
        phand, chand = hand_generate()
        janken_list3(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('Calc')
    print('elapsed_time', (end - start))

    start = time.time()
    for _ in range(LOOPCONT):
        phand, chand = hand_generate()
        janken_list4(phand, chand)
        sys.stdout.flush()
    end = time.time()
    print('Array')
    print('elapsed_time', (end - start))