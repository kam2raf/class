# PGN Analyzer

PGN Analyzer is a Python console application that reads chess games written in PGN notation and produces simple statistics.

The project identifies opening sequences, estimates inaccuracies using lightweight heuristics and summarizes the analyzed games.

## Features

- PGN parsing
- Opening recognition
- Mistake estimation
- Move statistics
- Console report

## Modules

- Parser
- Opening Detector
- Mistake Analyzer
- Statistics
- Report Generator

## Example

```
Games Loaded : 3

Detected Openings

Italian Game : 1
Sicilian Defense : 1
Queen's Gambit : 1

Estimated Mistakes

White : 2

Black : 4

Average Moves

41

Most Common Opening

Italian Game
```

Run

```bash
python main.py
```

The demo includes built-in sample PGN games.
