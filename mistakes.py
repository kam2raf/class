class MistakeAnalyzer:

    def estimate(

        self,

        moves

    ):

        white = 0

        black = 0

        for move in moves:

            if len(move) > 5:

                white += 1

            if "?" in move:

                black += 1

        return {

            "white": white,

            "black": black

        }
