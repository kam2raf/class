class OpeningDetector:

    def detect(

        self,

        moves

    ):

        first = " ".join(

            moves[:4]

        )

        if first.startswith(

            "e4 e5 Nf3 Nc6"

        ):

            return "Italian Game"

        if first.startswith(

            "e4 c5"

        ):

            return "Sicilian Defense"

        if first.startswith(

            "d4 d5 c4"

        ):

            return "Queen's Gambit"

        return "Unknown Opening"
