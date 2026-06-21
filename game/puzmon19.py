'''
タイトル: Puzzle&Monsters
概要: スッキリわかるPython入門 第2版(著作 国本大悟、須藤秋良/出版 株式会社インプレス)  の誘導に従って、細部は自力で考えながら書いた、ゲームのプログラム。
      仕様はパズドラに類似している。入力されたコマンドに基づき、宝石を移動させ、敵を倒していく。
作成日： 2026/06/01~2026/06/07, 2026/6/19~
作成者: 自分


書籍の指示からオリジナルで変更する点
・チュートリアル機能の追加
・戦闘フィールドを見やすくする（改行、スコアの表示）
・
'''










from random import randint





#敵のモンスターについての情報
slime={
    'name':'スライム',
    'hp':100,
    'max_hp':100,
    'element':'水',
    'ap':10,
    'dp':1
}

goblin={
    'name':'ゴブリン',
    'hp':200,
    'max_hp':200,
    'element':'土',
    'ap':20,
    'dp':5
}

giantbat={
    'name':'オオコウモリ',
    'hp':300,
    'max_hp':300,
    'element':'風',
    'ap':30,
    'dp':10
}

werewolf={
    'name':'ウェアウルフ',
    'hp':400,
    'max_hp':400,
    'element':'風',
    'ap':40,
    'dp':15
}

dragon={
    'name':'ドラゴン',
    'hp':600,
    'max_hp':600,
    'element':'火',
    'ap':50,
    'dp':20
}

monsters=[
    slime,
    goblin,
    giantbat,
    werewolf,
    dragon
    ]








#味方のモンスターについての情報
seiryuu={
    'name':'青龍',
    'hp':150,
    'max_hp':150,
    'element':'風',
    'ap':15,
    'dp':10
    }


suzaku={
    'name':'朱雀',
    'hp':150,
    'max_hp':150,
    'element':'火',
    'ap':25,
    'dp':10
}

byakko={
    'name':'白虎',
    'hp':150,
    'max_hp':150,
    'element':'土',
    'ap':20,
    'dp':5
}

genbu={
    'name':'玄武',
    'hp':150,
    'max_hp':150,
    'element':'水',
    'ap':20,
    'dp':15
}

my_party=[
    seiryuu,
    suzaku,
    byakko,
    genbu
]








#ゲーム全体での記号
ELEMENT_SYMBOLS={
    '火':'$',
    '水':'~',
    '風':'@',
    '土':'#',
    '命':'&',
    '無':' '
}

ELEMENT_COLORS={
    '火':31,
    '水':34,
    '風':32,
    '土':33,
    '命':37,
    '無':30
}


alphabet={
        'A':0,
        'B':1,
        'C':2,
        'D':3,
        'E':4,
        'F':5,
        'G':6,
        'H':7,
        'I':8,
        'J':9,
        'K':10,
        'L':11,
        'M':12,
        'N':13,
}




#一文字目…攻撃するほう　二文字目…されるほう
ELEMENT_BOOST={
    '水火':2.0,
    '火風':2.0,
    '風土':2.0,
    '土水':2.0,

    '火水':0.5,
    '風火':0.5,
    '土風':0.5,
    '水土':0.5,
}






'''
    party_information: 味方の情報
            party_information={
                'player_name':player_name,
                'friends':friends,            #friendsには結局、グローバル関数であるmy_partyを代入している。
                'hp':total_hp,
                'max_hp':600,
                'dp':ave_dp
            }
    the_monster: 敵の情報
            slime={
            'name':'スライム',
            'hp':100,
            'max_hp':100,
            'element':'水',
            'ap':10,
            'dp':1
            }
'''




















#味方・敵のモンスター名に、属性をつけて表示する関数
def print_monster_name(monster_name):
    '''
    monster_name: 味方・敵モンスター（１体）の情報ディクショナリ。
    '''
    symbol=ELEMENT_SYMBOLS[monster_name['element']]
    color=ELEMENT_COLORS[monster_name['element']]
    print(f"\033[{color}m{symbol}{monster_name['name']}{symbol}\033[0m",
        end='')


















#宝石の連続チェックー消去ー攻撃ー生成ーコンボ終了判定　の流れをすべて担う関数
def evaluate_gems(party_information,the_monster,re_gems):
    '''
    re_gems: リストre_gemsの中に、リストgem_symbols（添字０）,gem_colors（添字１）を格納している
            宝石はAからNまで、順に添字0~13で管理する。
            swap_gems()によって並べ替えた後のもの。
    
    banishable: check_banishable()が返すリスト。
            banishable[0]~banishable[1]番目の宝石は消せる。
            消せる宝石がないときは空のリスト。
    
    banish_data=[banished_element,banished_count]。banish_gems() の戻り値。
            banished_element: 消去した宝石の属性。'水'など。
            banished_count: 消去した宝石の数。

        n: 左詰めしたい宝石ブロックの先頭の添字（例　AAA　BBBを左詰めするなら５）
    '''


    banishable=check_banishable(re_gems)
    combo=0
    banish_data=[]
    
    if not banishable:   #何も消せない場合
        pass
    else:  #少なくとも一回消せる場合
        #破壊的変数を呼び出して、re_gemsを14個の宝石が存在し、三連続の宝石が存在しうる状態にする。
        while banishable:
            combo+=1
            
            banish_data=banish_gems(re_gems,banishable)     #宝石の消去
            print_gems(re_gems)         #全消しした状態を一旦表示


            print(f"banishable={banishable}")
            print(f"banish_data={banish_data}" )



            if banish_data[0]!='命':    #命属性以外の宝石を消去した場合
                do_attack(party_information,the_monster,banish_data,combo)  #攻撃
            else:       #命属性の宝石を消去した場合
                do_recover(party_information,banish_data,combo)     #回復

            gem_colors=re_gems[1]
            if gem_colors[13]!=30:     #左詰め操作が必要な場合
                n=banishable[1]+1
                for i in range(banishable[1]-banishable[0]+1):
                    shift_gems(re_gems,n)    #添え字n以降のスロットを一文字だけ左詰め
                    print_gems(re_gems)
                    n-=1
            

            spawn_gems(re_gems,banishable)      #空きスロットに宝石を生成
            banishable=check_banishable(re_gems)
            print_gems(re_gems)
    
    print(f'{combo}COMBO!')








#宝石の並びを調べて消去可能な箇所を検索して返す関数
def check_banishable(re_gems):
    '''
    re_gems: リストre_gemsの中に、リストgem_symbols（添字０）,gem_colors（添字１）を格納している
           宝石はAからNまで、順に添字0~13で管理する。
           swap_gems()によって並べ替えた後のもの。
    '''
    gem_symbols=re_gems[0]
    banishable=[]
    for i in range(12):     #まず消去可能なものがあるか調べる
        if gem_symbols[i]!=' ':
            if gem_symbols[i]==gem_symbols[i+1]==gem_symbols[i+2]:
                banishable.append(i)
                break
            else:
                pass
        
    if len(banishable)==0:
            pass
    else:       #消去可能なものがある場合、何連続で消去できるか調べる
        j=0
        while (i+j+3)<=13:
            if gem_symbols[i]!=' ':
                if gem_symbols[i]==gem_symbols[i+j+3]:
                    j+=1
                else:
                    break
        banishable=[i,i+j+2]    # i ~ (i+j+2)番目の宝石は消せる
        

    return(banishable)

'''
banishable: check_banishable()が返すリスト。
        banishable[0]~banishable[1]番目の宝石は消せる。
        消せる宝石がないときは空のリスト。
'''






#指定された消去可能な宝石の並び情報に基づき、スロット内の宝石を消滅させて効果を発動させる流れに責任を持つ関数
def banish_gems(re_gems,banishable):
    '''
    re_gems: リストre_gemsの中に、リストgem_symbols（添字０）,gem_colors（添字１）を格納している
            宝石はAからNまで、順に添字0~13で管理する。
            swap_gems()によって並べ替えた後のもの。

    banishable: check_banishable()が返すリスト。
            banishable[0]番目 ~ banishable[1]番目の宝石は消せる。
            消せる宝石がないときは空のリスト。
    '''
    #リストから石を消すと、添え字が変わって面倒なので、ここでは消去できる石を'  'に変える。
    gem_symbols=re_gems[0]
    gem_colors=re_gems[1]

    banished_symbol=gem_symbols[banishable[0]]
    for k,v in ELEMENT_SYMBOLS.items():
        if v==banished_symbol:
            banished_element=k

    if len(banishable)==0:
        pass
    else:
        for i in range(banishable[1]-banishable[0]+1):
            

            gem_symbols[banishable[0]+i]=' '
            gem_colors[banishable[0]+i]=30

    banished_count=banishable[1]-banishable[0]+1

    banish_data=[banished_element,banished_count]

    return banish_data    #破壊的変数なのでgemsは戻り値にしなくてよい。








#空きスロットの右側に並ぶ宝石を "一文字分だけ" 左詰めする関数
def shift_gems(re_gems,n):
    '''
    n: 左詰めしたい宝石ブロックの先頭の添字（例　AAA　BBBを左詰めするなら５）
    '''
    gem_symbols=re_gems[0]
    gem_colors=re_gems[1]

    for i in range(14-n):
        gem_symbols[n+i-1]=gem_symbols[n+i]
        gem_colors[n+i-1]=gem_colors[n+i]

    gem_symbols[13]=' '
    gem_colors[13]=30







#空きスロットにランダムな宝石を生成する関数
def spawn_gems(re_gems,banishable):	
    '''
    re_gems: shift_gems()によって破壊済み。リストgem_symbols（添字０）,gem_colors（添字１）を格納している
            要素数は14。三連以上の宝石は消されている。
    banishable: check_banishable()が返すリスト。
            banishable[0]番目 ~ banishable[1]番目の宝石は消せる。
            消せる宝石がないときは空のリスト。

    この関数を呼び出すと、re_gemsはスロットが埋まった状態になる。
    '''

    ELEMENT_SYMBOL_LIST=['$','~','@','#','&']
    ELEMENT_COLOR_LIST=[31,34,32,33,37]

    gem_symbols=re_gems[0]
    gem_colors=re_gems[1]

    top=13-banishable[1]+banishable[0]    #空きスロットが格納された文字列の先頭の添え字

    for i in range(14-top):
        num=randint(0,4)
        symbol=ELEMENT_SYMBOL_LIST[num]
        color=ELEMENT_COLOR_LIST[num]
        gem_symbols[top+i]=symbol
        gem_colors[top+i]=color

    #re_gemsは14個の宝石が存在し、三連続の宝石が存在しうる状態になる。












#指定位置の宝石を指定した方向の隣の宝石と入れ替えるユーティリティ関数
def swap_gem(gems,re_command1,LR):
    '''
    gems: リストgemsの中に、リストgem_symbols（添字０）,gem_colors（添字１）を格納している
    宝石はAからNまで、順に添字0~13で管理する
    re_command1: 添字が何番の宝石を動かすのか
    LR: 右左どっちへ動かすのか
    re_gems: 並べ替えた後のgems
    '''

    gem_symbols=gems[0]
    gem_colors=gems[1]

    if LR=='L':
        pre_left_symbol=gem_symbols[re_command1-1]
        pre_right_symbol=gem_symbols[re_command1]
        gem_symbols[re_command1]=pre_left_symbol
        gem_symbols[re_command1-1]=pre_right_symbol

        pre_left_color=gem_colors[re_command1-1]
        pre_right_color=gem_colors[re_command1]
        gem_colors[re_command1]=pre_left_color
        gem_colors[re_command1-1]=pre_right_color


    elif LR=='R':
        pre_left_symbol=gem_symbols[re_command1]
        pre_right_symbol=gem_symbols[re_command1+1]
        gem_symbols[re_command1+1]=pre_left_symbol
        gem_symbols[re_command1]=pre_right_symbol

        pre_left_color=gem_colors[re_command1]
        pre_right_color=gem_colors[re_command1+1]
        gem_colors[re_command1+1]=pre_left_color
        gem_colors[re_command1]=pre_right_color

    print_gems(gems)
    re_gems=gems
    return re_gems






#指定位置の宝石を別の位置へ移動させるユーティリティ関数。移動の過程も画面表示する。
#swap_gem() = 「隣接交換」という最小単位の処理
#move_gem() = 「目的地まで移動」という高レベル処理。swap_gem() を呼び出す。
def move_gem(command,gems):	
    '''
    command: 2文字のアルファベットA~N
    gems: リストgemsの中に、リストgem_symbols（添字０）,gem_colors（添字１）を格納している
           宝石はAからNまで、順に添字0~13で管理する
    '''

    command1=command[0]     #アルファベット一文字
    command2=command[1] 


    re_command1=alphabet[command1]
    re_command2=alphabet[command2]
    modified_command=[re_command1,re_command2]       #modified_commandには[3,1]などが格納
    
    is_move=False
    while is_move==False:
        if re_command1==re_command2:
            is_move=True

        elif re_command1 < re_command2:      #右へ動かす
            swap_gem(gems,re_command1,'R')
            if (re_command1+1)==(re_command2):
                is_move=True
            else:
                re_command1+=1

        else:       #左へ動かす
            swap_gem(gems,re_command1,'L')
            if (re_command1-1)==(re_command2):
                is_move=True
            else:
                re_command1-=1










#宝石スロットにランダムに宝石を発生させるユーティリティ関数
def fill_gems():
    gem_symbols=[]          
    gem_colors=[]

    ELEMENT_SYMBOL_LIST=['$','~','@','#','&']
    ELEMENT_COLOR_LIST=[31,34,32,33,37]
    for i in range(14):
        num=randint(0,4)
        symbol=ELEMENT_SYMBOL_LIST[num]
        color=ELEMENT_COLOR_LIST[num]
        gem_symbols.append(symbol)
        gem_colors.append(color)

    gems=[gem_symbols,gem_colors]
    return gems
'''
リストgemsの中に、リストgem_symbols（添字０）,gem_colors（添字１）を格納している
宝石はAからNまで、順に添字0~13で管理する
'''





#宝石スロット(14個分)を画面に表示する関数
def print_gems(gems):
    '''
    gems: fill_gems() で定義したリスト
    '''
    gem_symbols=gems[0]
    gem_colors=gems[1]
    print('ーーーーーーーーーーーーーーーーーーーーーー')
    print('A B C D E F G H I J K L M N')    #アルファベット、空白いずれも半角
    for i in range(14):
        print(f"\033[{gem_colors[i]}m{gem_symbols[i]} \033[0m"
              ,end="")
    print()
    print('ーーーーーーーーーーーーーーーーーーーーーー')
    print()













#消した宝石が攻撃系のとき、攻撃計算
def do_attack(party_information,the_monster,banish_data,combo):
    '''
    party_information: 味方の情報
    the_monster: 敵の情報
 
    banish_data=[banished_element,banished_count]。banish_gems() の戻り値。
        banished_element: 消去した宝石の属性。'水'など。
        banished_count: 消去した宝石の数。

    combo: コンボ数
    '''
    friends=party_information['friends']     #攻撃する味方を選択
    for friend in friends:
        if friend['element']==banish_data[0]:
            my_attacker=friend

    print(f'{my_attacker['name']}の攻撃')

    if not banish_data:     #宝石を消去しなかったときはダメージが1になるようにプログラム
        damage=1
        
    else:   #宝石を少なくとも一回消去できたとき
        element_command=banish_data[0] + the_monster['element']     #属性補正の計算
        if element_command in ELEMENT_BOOST:    #属性補正あり
            element_adjustment=ELEMENT_BOOST[element_command]
        else:     #属性補正なし
            element_adjustment=1.0

        combo_adjustment=1.5**(banish_data[1]-3+combo)       #コンボ補正の計算

        num=randint(90,110)
        a=my_attacker['ap']-the_monster['dp']
        b=a*element_adjustment*combo_adjustment*num*0.01
        temp_damage=round(b)

        if temp_damage>=0:
            damage=temp_damage
        else:
            damage=1

    print(f'{damage}のダメージを与えた')
    the_monster['hp']-=damage      #これは破壊的関数





#消した宝石が回復系のとき、回復計算
def do_recover(party_information,banish_data,combo):
    print()
    '''
    party_information: 味方の情報
 
    banish_data=[banished_element,banished_count]。banish_gems() の戻り値。
        banished_element: 消去した宝石の属性。'水'など。
        banished_count: 消去した宝石の数。

    combo: コンボ数
    '''

    combo_adjustment=1.5**(banish_data[1]-3+combo)       #コンボ補正の計算

    num=randint(90,110)
    temp_recover=20*combo_adjustment*num
    recover=round(temp_recover)  
    
    hp=party_information['hp']
    max_hp=party_information['max_hp']

    if hp+recover<max_hp:
        party_information['hp']=hp+recover
    else:
        recover=max_hp-hp
        party_information['hp']=max_hp
        
    print(f'{recover}だけ味方のHPを回復した')
















#戦闘時のバトルフィールド画面を表示する関数
def show_battle_field(party_information,the_monster):

    print('<バトルフィールド>')
    print_monster_name(the_monster)  #敵の名前を表示
    print(f'  hp ={the_monster['hp']} / {the_monster['max_hp']}')

    friends=party_information['friends']    #friendsは、実質リストmy_partyが代入される
    print()
    for the_friend in friends:        #味方一覧
        print_monster_name(the_friend)
        print(' ',end="")
    print()
    print(f"hp = {party_information['hp']} / {party_information['max_hp']}")










#戦闘（敵のターン）
def on_enemy_turn(party_information,the_monster):     
    '''
    引数party_information: organize_party() で定めたディクショナリ。
    引数the_monster: 対戦するモンスター（１体）の情報ディクショナリ。
    '''
    print(f"【{the_monster['name']}のターン】（hp={the_monster['hp']}）")

    num=randint(90,110)
    a=the_monster['ap']-party_information['dp']
    temp_damage=a*0.01*num

    if temp_damage<=0:
        damage=1
    else:
        damage=round(temp_damage)

    print(f'{damage}のダメージを受けた')
    party_information['hp']-=damage
    print()












#戦闘（プレイヤーのターン）
def on_player_turn(party_information,the_monster,gems_in_this_battle): 
    '''
    party_information: organize_party() で定めたディクショナリ。
    the_monster: は対戦するモンスター（１体）の情報ディクショナリ。
    '''
    print(
        f"【{party_information['player_name']}のターン】(hp={party_information['hp']}）"
          )
    
    show_battle_field(party_information,the_monster)
    print_gems(gems_in_this_battle)

    is_command=False
    while is_command==False:
        command=input('コマンドを入力してください>>')
        is_command=check_valid_command(command) 
        if is_command==False:
            print('無効なコマンドです。')
    
    move_gem(command,gems_in_this_battle)    #コマンドによる宝石の移動
    evaluate_gems(party_information,the_monster,gems_in_this_battle)     #移動した宝石の　連続チェックー消去ー攻撃ー生成ーコンボ終了判定

    print()










#与えられたコマンドが適切かどうかをチェックする関数。正しければTrueを返す。
def check_valid_command(command):
    is_command=True
    if len(command)==2:
        each_char=[]
        for char in command:
            each_char.append(char)
        for i in range(2):

            if each_char[i]in'ABCDEFGHIJKLMN':
                pass
            else:
                is_command=False
    else:
        is_command=False

    return is_command







#バトル全体を進行する関数        
def do_battle(party_information,the_monster):                
    ''' 
    party_information: organize_party() で定めたディクショナリ。
    the_monster: 対戦するモンスター（１体）の情報ディクショナリ。
    '''
    print_monster_name(the_monster)
    print(
        f"（hp＝{the_monster['hp']}）が現れた！"
        )

    gems_in_this_battle=fill_gems()

    is_battle=False
    while is_battle==False:
        #味方ターン
        on_player_turn(party_information,the_monster,gems_in_this_battle)
        if party_information['hp']<=0:
            print(f'パーティーのhpは0になった\n{party_information['player_name']}はダンジョンから逃げ出した')
            return 0
            is_battle=True

        #敵ターン
        on_enemy_turn(party_information,the_monster)
        if the_monster['hp']<=0:
            print_monster_name(the_monster)
            print('を倒した！')
            return 1
            is_battle=True











#パーティーを表示する関数
def show_party(party_information):
    ''' 
    party_information: organize_party() で定めたディクショナリ。
    '''
    friends=party_information['friends']
    for i in range(len(friends)):
        the_monster=friends[i]
        print_monster_name(the_monster)
        print(f'  hp={the_monster['hp']}  攻撃＝{the_monster['ap']}  防御＝{the_monster['dp']}')











#ダンジョン撤退・続行の判定関数
def go_dungeon(party_information,monsters):
    '''
    party_information: organize_party() で定めたディクショナリ。
    monsters: 敵モンスター一覧のリスト
    '''

    print(f'{party_information['player_name']}のパーティー（hp＝{party_information['hp']}）はダンジョンに到達した')

    print('＜パーティー編成＞ーーーーーーーーーーーーー')
    show_party(party_information)
    print('ーーーーーーーーーーーーーーーーーーーーーー')

    is_win=0
    for i in range(len(monsters)):          #エラー修正メモ　do_battle()に与える値はiではいけない
        is_win+=do_battle(party_information,monsters[i])    #do_battle関数の呼び出し
        
        if party_information['hp']<=0:
            print(f'{party_information['player_name']}はダンジョンから逃げ出した')
            break
        else:
            print(f'{party_information['player_name']}はさらに奥へと進んだ')
            print('＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝')

    if is_win==5:
        print(f'{party_information['player_name']}はダンジョンを制覇した')
    else:
        pass

    return is_win











#パーティー編成を一括管理する関数
def organize_party(player_name,friends):
    '''
    player_name: プレイヤーの名前
    friends: 味方のモンスター一覧のリスト（例　my_party）
    '''

    total_hp=0
    total_dp=0
    for i in range(len(friends)):
        the_monster=friends[i]
        total_hp+=the_monster['hp']
        total_dp+=the_monster['dp']
    ave_dp=total_dp/len(friends)

    party_information={
        'player_name':player_name,
        'friends':friends,            #friendsには結局、グローバル関数であるmy_partyを代入している。
        'hp':total_hp,
        'max_hp':600,
        'dp':ave_dp
    }

    return party_information











#総括のmain関数
def main():

    is_name=False
    while is_name==False:
        name=input('プレイヤー名を入力してください>>')

        if not name:      #空白判定
            print('名前を入力してください。')
        else:
            is_name=True


    print('\n***Puzzle&Monsters***\n')

    party_information=organize_party(name,my_party)

    defeated_monsters=go_dungeon(party_information,monsters)
    if defeated_monsters==5:
        print(f'***GAME CLEARD!!***\n倒したモンスターの数＝{defeated_monsters}')
    else:
        print('***GAME OVER!!***')

    return name








#main関数の呼び出し
main()

