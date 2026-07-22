from collections import Counter

class Statistics:

    def summarize(

        self,

        results

    ):

        openings = Counter(

            r["opening"]

            for r in results

        )

        avg = sum(

            r["moves"]

            for r in results

        ) // len(results)

        return {

            "openings": openings,

            "average": avg

        }
