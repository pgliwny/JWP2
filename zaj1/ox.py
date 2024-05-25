class TicTacToe:
    ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
    X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.

    def __init__(self):
        self.game_board = self.get_blank_board()  # Utwórz słownik planszy KIK.
        self.current_player = self.X  # X wykonuje ruch jako pierwszy.

    def get_blank_board(self):
        """Tworzy nową, pustą planszę gry w kółko i krzyżyk."""
        board = {}  # Plansza jest reprezentowana przez słownik Pythona.
        for space in self.ALL_SPACES:
            board[space] = self.BLANK  # Wszystkie pola na początku są puste.
        return board

    def get_board_str(self):
        """Zwraca tekstową reprezentację planszy."""
        board = self.game_board
        return f'''
                {board['1']}|{board['2']}|{board['3']} 1 2 3 
                -+-+- 
                {board['4']}|{board['5']}|{board['6']} 4 5 6 
                -+-+- 
                {board['7']}|{board['8']}|{board['9']} 7 8 9'''

    def is_valid_space(self, space):
        """Zwraca True, jeśli pole na planszy ma prawidłowy numer i pole jest puste."""
        if space is None:
            return False
        return space in self.ALL_SPACES or self.game_board[space] == self.BLANK

    def is_winner(self, player):
        """Zwraca True, jeśli gracz jest zwycięzcą tej planszy KIK."""
        b, p = self.game_board, player
        # Sprawdzenie, czy trzy takie same znaki występują w wierszach, kolumnach i po przekątnych.
        return ((b['1'] == b['2'] == b['3'] == p) or
                (b['4'] == b['5'] == b['6'] == p) or
                (b['7'] == b['8'] == b['9'] == p) or
                (b['1'] == b['4'] == b['7'] == p) or
                (b['2'] == b['5'] == b['8'] == p) or
                (b['3'] == b['6'] == b['9'] == p) or
                (b['3'] == b['5'] == b['7'] == p) or
                (b['1'] == b['5'] == b['9'] == p))

    def is_board_full(self):
        """Zwraca True, jeśli wszystkie pola na planszy są zajęte."""
        for space in self.ALL_SPACES:
            if self.game_board[space] == self.BLANK:
                return False
        return True

    def update_board(self, space, mark):
        """Ustawia pole na planszy na podany znak."""
        self.game_board[space] = mark

    def main(self):
        """Rozgrywka w kółko i krzyżyk."""
        print('Witaj w grze kółko i krzyżyk!')
        while True:
            print(self.get_board_str())  # Wyświetl planszę na ekranie.

            # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
            move = None
            while not self.is_valid_space(move):
                print(f'Jaki jest ruch gracza {self.current_player}? (1-9)')
                move = input()
            self.update_board(move, self.current_player)  # Wykonanie ruchu.
            # Sprawdzenie, czy gra jest zakończona:
            if self.is_winner(self.current_player):  # Sprawdzenie, kto wygrał.
                print(self.get_board_str())
                print(self.current_player + ' wygrał grę!')
                break
            elif self.is_board_full():  # Sprawdzenie remisu.
                print(self.get_board_str())
                print('Gra zakończyła się remisem!')
                break
            self.current_player = self.O if self.current_player == self.X else self.X  # Zmiana gracza.
        print('Dziękuję za grę!')


if __name__ == '__main__':
    game = TicTacToe()
    game.main()  # Rozpocznij grę.
