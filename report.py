class Report:

    def show(

        self,

        summary,

        results

    ):

        print(

            "Games Loaded :",

            len(results),

            "\n"

        )

        print(

            "Detected Openings\n"

        )

        for k, v in summary[

            "openings"

        ].items():

            print(

                f"{k} : {v}"

            )

        print()

        white = sum(

            r["mistakes"]["white"]

            for r in results

        )

        black = sum(

            r["mistakes"]["black"]

            for r in results

        )

        print(

            "Estimated Mistakes\n"

        )

        print(

            "White :",

            white

        )

        print()

        print(

            "Black :",

            black

        )

        print()

        print(

            "Average Moves\n"

        )

        print(

            summary["average"]

        )

        print()

        best = max(

            summary["openings"],

            key=summary["openings"].get

        )

        print(

            "Most Common Opening\n"

        )

        print(best)
