def alphabeta(current_game):
    """
    :param current_game: the first GameClass object of the game
    :return: result of recursive alphabeta
    """
    # Initialize alpha as negative infinity and beta as positive infinity
    return recursive_alphabeta(current_game, float('-inf'), float('inf'))


def recursive_alphabeta(current_game, alpha, beta):
    """
    Alpha-beta pruning algorithm to find the optimal move.
    :param current_game: Game Class Object
    :param alpha: Best score for MAX along the path to root
    :param beta: Best score for MIN along the path to root
    :return: v - value, best_prev_move - list of previous game class objects that leads to v
    """
    if current_game.game_over():
        return current_game.get_score(), []

    best_move = None
    best_prev_move = []

    if current_game.get_cur_player() == 1:  # -- MIN player --
        v = float('inf')  # Initialize to positive infinity for MIN
        moves = current_game.get_moves()
        for move in moves:
            mx, prev_moves = recursive_alphabeta(move, alpha, beta)
            if v > mx:
                v = mx
                best_move = move
                best_prev_move = prev_moves
            beta = min(beta, v)  # Update beta
            if v <= alpha:  # Prune if v <= alpha
                break

    if current_game.get_cur_player() == 2:  # -- MAX player --
        v = float('-inf')  # Initialize to negative infinity for MAX
        moves = current_game.get_moves()
        for move in moves:
            mx, prev_moves = recursive_alphabeta(move, alpha, beta)
            if v < mx:
                v = mx
                best_move = move
                best_prev_move = prev_moves
            alpha = max(alpha, v)  # Update alpha
            if v >= beta:  # Prune if v >= beta
                break

    best_prev_move.append(best_move)
    return v, best_prev_move