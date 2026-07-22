from parser import PGNParser
from analyzer import Analyzer
from statistics import Statistics
from report import Report
from sample_games import SAMPLE_GAMES

parser = PGNParser()

analyzer = Analyzer()

results = []

for text in SAMPLE_GAMES:

    game = parser.parse(

        text

    )

    results.append(

        analyzer.analyze(

            game

        )

    )

summary = Statistics().summarize(

    results

)

Report().show(

    summary,

    results

)
