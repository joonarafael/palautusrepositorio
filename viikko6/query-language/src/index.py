from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query1 = QueryBuilder()
    m1 = (
        query1
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    query2 = QueryBuilder()
    m2 = (
        query2
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    query = QueryBuilder()
    matcher = query.oneOf(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
