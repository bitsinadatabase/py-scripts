import argparse

# Refer https://pypi.org/project/colorama/ for installing the colorama library
from colorama import init, Fore, Back, Style


init()


symbol_to_piece = {
    "B": "Bishop",
    "K": "King",
    "N": "Knight",
    "P": "Pawn",
    "Q": "Queen",
    "R": "Rook"
}

piece_unicodes = {
    "B": u'\u265D',
    "K": u'\u265A',
    "N": u'\u265E',
    "P": u'\u265F',
    "Q": u'\u265B',
    "R": u'\u265C',
}


def describe_fen(fen, print_board):
    board_state, active_colour, castling_availability, en_passant_target, half_move_clock, full_move_number = fen.split()
    
    describe_board_state(board_state, print_board)
    describe_active_colour(active_colour)
    describe_castling_availability(castling_availability)
    describe_en_passant_target(en_passant_target)
    describe_half_move_clock(half_move_clock)
    describe_full_move_number(full_move_number)

def describe_board_state(board_state, print_board):
    white_pieces, black_pieces = {}, {}

    for piece in symbol_to_piece.values():
        white_pieces[piece] = []
        black_pieces[piece] = []

    if print_board:
        print_board_state(board_state)
        return
    
    rank_name = 8
    for rank in board_state.split("/"):
        file_name = "a"  
        for symbol in rank:
            if symbol.isdigit():
                file_name = chr(ord(file_name) + int(symbol))
            elif symbol.islower():
                piece = symbol_to_piece[symbol.upper()]
                black_pieces[piece].append(f"{file_name}{rank_name}")
                file_name = chr(ord(file_name) + 1)
            else:
                piece = symbol_to_piece[symbol.upper()]
                white_pieces[piece].append(f"{file_name}{rank_name}")
                file_name = chr(ord(file_name) + 1)
                continue
        rank_name -= 1
    
    print(f"LIGHTWHITE_EX Pieces - {white_pieces}")
    print(f"Black Pieces - {black_pieces}")


def print_board_state(board_state):
    rank_number = 8
    for rank in board_state.split("/"):
        file_number = 1
        for symbol in rank:
            if symbol.isdigit():
                for i in range(int(symbol)):
                    is_light_square = ((file_number + rank_number ) % 2) == 1
                    
                    if not is_light_square:
                        print(Back.LIGHTBLACK_EX + "  ", end = "")
                    else:
                        print(Back.YELLOW + "  ", end = "")
                    
                    file_number += 1
            elif symbol.islower():
                is_light_square = ((file_number + rank_number ) % 2) == 1
                file_number += 1
                
                if not is_light_square:
                    print(Back.LIGHTBLACK_EX + Fore.BLACK + f"{piece_unicodes[symbol.upper()]} ", end = "")
                else:
                    is_light_square = ((file_number + rank_number ) % 2) == 1
                    print(Back.YELLOW + Fore.BLACK + f"{piece_unicodes[symbol.upper()]} ", end = "")
                
            else:
                is_light_square = ((file_number + rank_number ) % 2) == 1
                file_number += 1
                
                if not is_light_square:
                    print(Back.LIGHTBLACK_EX +  Fore.WHITE + f"{piece_unicodes[symbol]} ", end = "")
                else:
                    print(Back.YELLOW + Fore.WHITE + f"{piece_unicodes[symbol]} ", end = "")
                
        print(Style.RESET_ALL)
        rank_number -= 1

def describe_active_colour(active_colour):
    active_colour = "White" if active_colour == "w" else "Black"
    print(f"To move : {active_colour}")


def describe_castling_availability(castling_availability):
    white_castling_kingside = "Kingside" if "K" in castling_availability else ""
    white_castling_queenside = "Queenside" if "Q" in castling_availability else ""
    black_castling_kingside = "Kingside" if "k" in castling_availability else ""
    black_castling_queenside = "Queenside" if "q" in castling_availability else ""

    print(f"White can castle : {white_castling_kingside}, {white_castling_queenside}")
    print(f"Black can castle : {black_castling_kingside}, {black_castling_queenside}")


def describe_en_passant_target(en_passant_target):
    print(f"En passant capture square : {en_passant_target}")


def describe_half_move_clock(half_move_clock):
    print(f"Number of half moves since last capture or pawn advance - {half_move_clock}")


def describe_full_move_number(full_move_number):
    print(f"Move number - {full_move_number}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Convert FEN to human readable format.")
    parser.add_argument("fen", metavar = "fen", type = str, help = "FEN to convert")
    parser.add_argument("--print_board", metavar = "print_board", type = bool, default = False, help = "True to print the board as a grid.")

    args = parser.parse_args()
    describe_fen(args.fen, args.print_board)

