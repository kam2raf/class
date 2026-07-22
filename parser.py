from models import Game

class PGNParser:

    def parse(self, text):

        lines = text.splitlines()

        event = "Unknown"

        moves = []

        for line in lines:

            if line.startswith("[Event"):

                event = line.split('"')[1]

            if line.startswith("1."):

                clean = line.replace("\n", " ")

                tokens = clean.split()

                for token in tokens:

                    if "." not in token:

                        moves.append(token)

        return Game(

            event,

            moves

        )
