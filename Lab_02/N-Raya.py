import random
import math
import os

#X is max = 1
#O in min = -1

class TicTacToe:
    def __init__(self):
        self.primero = input("elige quien empieza, jugador(O) o maquina(X): ")
        self.size = int(input("poner 3"))
        self.humanPlayer = "O"
        self.botPlayer = "X"
        self.board = ['-' for _ in range(self.size*self.size)] #creamos tablero

    def show_board(self):
        
        print("")
        for i in range(self.size):
            print("  ",self.board[0+(i*3)]," | ",self.board[1+(i*3)]," | ",self.board[2+(i*3)])
            print("")
        """
        print("")
        for i in range(self.size):
            print("  ", self.board[i*self.size], end =" " )
            for j in range (i+1,i+self.size):
                print(" | ",self.board[j],end = "")
            print("\n")
        """
            
    def is_board_filled(self,state):
        return not "-" in state

    def is_player_win(self,state,player):
        test=0
        for i in range(0,self.size*(self.size-1)+1,self.size):
            for j in range(i,i+self.size-1):
                if state[j]==state[j+1] and state[j]==player:
                    test=test+1
            if test==self.size-1:
                return True
            test=0
        for i in range(0,self.size):
            for j in range(i,self.size*(self.size-1),self.size):
                if state[j]==state[j+self.size] and state[j]==player:
                    test=test+1
            if test==self.size-1:
                return True
            test=0
        test=0
        for i in range(0,self.size*self.size-1,self.size+1):
            if state[i]==state[i+self.size+1] and state[i]==player:
                test=test+1
        if test==self.size-1:
            return True
        test=0
        for i in range(self.size-1,self.size*(self.size-1),self.size-1):
            if state[i]==state[i+self.size-1] and state[i]==player:
                test=test+1
        if test==self.size-1:
            return True

        return False
        
        
        


    def checkWinner(self):
        if self.is_player_win(self.board,self.humanPlayer):
            os.system("cls")
            print(f"   Player {self.humanPlayer} wins the game!")
            return True
            
        if self.is_player_win(self.board,self.botPlayer):
            os.system("cls")
            print(f"   Player {self.botPlayer} wins the game!")
            return True

        
        if self.is_board_filled(self.board):
            os.system("cls")
            print("   Match Draw!")
            return True
        return False

    def start(self):
        bot = ComputerPlayer(self.botPlayer,self.primero,self.size)
        human = humanPlayer(self.humanPlayer)
        
        if self.primero == "X":
            self.board[random.randint(0, 9)]= "X"

            
                    
            square = human.human_move(self.board)
            self.board[square] = self.humanPlayer

            square = bot.machine_move(self.board)
            self.board[square] = self.botPlayer
        
        while True:
            os.system("cls")
            print(f"   Player {self.humanPlayer} turn")
            self.show_board()
            
            #Human
            square = human.human_move(self.board)
            self.board[square] = self.humanPlayer
            if self.checkWinner():
                break
            
            #Bot
            square = bot.machine_move(self.board)
            self.board[square] = self.botPlayer
            if self.checkWinner():
                break

        
        print()
        self.show_board()

class humanPlayer:
    def __init__(self,letter):
        self.letter = letter
    
    def human_move(self,state):
        
        while True:
            square =  int(input("Enter the square to fix spot(1-9): "))
            print()
            if state[square-1] == "-":
                break
        return square-1

class ComputerPlayer(TicTacToe):
    def __init__(self,letter,primero,size):
        self.botPlayer = letter
        self.humanPlayer = "X" if letter == "O" else "O"
        self.primero=primero
        self.size=size

    def players(self,state):
        n = len(state)
        x = 0
        o = 0
        for i in range(9):
            if(state[i] == "X"):
                x = x+1
            if(state[i] == "O"):
                o = o+1
        
        if self.primero == "X":
            if x>o:
                return"O"
            else:
                return "X"
        else:
            if x<o:
                return"X"
            else:
                return "O"
    
    def actions(self,state):
        return [i for i, x in enumerate(state) if x == "-"]
    
    def result(self,state,action):
        newState = state.copy()
        player = self.players(state)
        newState[action] = player
        return newState
    
    def terminal(self,state):
        if(self.is_player_win(state,"X")):
            return True
        if(self.is_player_win(state,"O")):
            return True
        return False

    def minimax(self, state, player):
        max_player = self.humanPlayer  # yourself
        other_player = 'O' if player == 'X' else 'X'

    
        if self.terminal(state):
            return {'position': None, 'score': 1 * (len(self.actions(state)) + 1) if other_player == max_player else -1 * (
                        len(self.actions(state)) + 1)}
        elif self.is_board_filled(state):
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  
        else:
            best = {'position': None, 'score': math.inf}  
        for possible_move in self.actions(state):
            newState = self.result(state,possible_move)
            sim_score = self.minimax(newState, other_player)  

            sim_score['position'] = possible_move  

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

    def machine_move(self,state):
        square = self.minimax(state,self.botPlayer)['position']
        return square


tic_tac_toe = TicTacToe()
tic_tac_toe.start()
