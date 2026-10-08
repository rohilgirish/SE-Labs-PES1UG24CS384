import copy
import random

COLS = 7


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [c for c in range(COLS) if board.grid[0][c] == "."]
        if not legal:
            return None

        # 1. Take an immediate win if available.
        for col in legal:
            if self._wins_if_played(board, col, me):
                return col

        # 2. Block the opponent's immediate win.
        for col in legal:
            if self._wins_if_played(board, col, opponent):
                return col

        # 3. Choose safely: avoid moves that hand the opponent a win on top,
        #    and prefer central columns.
        safe = [c for c in legal if not self._gives_win_above(board, c, me, opponent)]
        candidates = safe or legal  # if every move is unsafe, still play
        center = COLS // 2
        best = min(abs(c - center) for c in candidates)
        return random.choice([c for c in candidates if abs(c - center) == best])

    @staticmethod
    def _wins_if_played(board, col, token):
        """True if dropping token in col wins. Works on a copy; real board is untouched."""
        trial = copy.deepcopy(board)
        if trial.drop(col, token) is None:
            return False
        return trial.winner(token)

    @staticmethod
    def _gives_win_above(board, col, me, opponent):
        """True if playing col lets opponent win by playing the same column next."""
        trial = copy.deepcopy(board)
        if trial.drop(col, me) is None:
            return False
        if trial.grid[0][col] != ".":  # column now full, no reply possible there
            return False
        return trial.drop(col, opponent) is not None and trial.winner(opponent)
