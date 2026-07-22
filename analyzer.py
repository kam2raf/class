from openings import OpeningDetector
from mistakes import MistakeAnalyzer

class Analyzer:

    def analyze(

        self,

        game

    ):

        opening = OpeningDetector().detect(

            game.moves

        )

        mistakes = MistakeAnalyzer().estimate(

            game.moves

        )

        return {

            "opening": opening,

            "moves": len(game.moves),

            "mistakes": mistakes

        }
