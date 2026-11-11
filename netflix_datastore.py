import sqlite3, csv, ast


class Datastore:
    def __init__(self, database_file: str, data_file: str):

        self.database_file = database_file
        self.data_file = data_file
        self.conn = sqlite3.connect(self.database_file)
        self.cursor = self.conn.cursor()

        # self.delete()
        self.conn.commit()
        self.populate_database()
        self.conn.commit()

    def delete(self):
        tables = ["Actor", "Cast", "Country", "Director", "Genre", "Media", "MediaCountries", "MediaDirectors", "Rating", "Type"]
        for table in tables:
            self.cursor.execute("""
            DELETE FROM :table
            """, {table: table})


    def populate_database(self):
        """
        populates the database with data from the csv file
        """
        with open(self.data_file, mode="r", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)

            # process the CSV data
            for record in csv_reader:
                # process the CSV data
                for record in csv_reader:
                    
                    type = record["type"]
                    title = record["title"]
                    date_added = record["date_added"]
                    release_year = int(record["release_year"])
                    duration = record["duration"]
                    description = record["description"]
                    rating = self.add_or_get_rating(record["rating"])

                    self.add_or_get_rating("PG-13")
                    self.add_media(
                        type,
                        title,
                        date_added,
                        release_year,
                        duration,
                        rating,
                        description
                    )

    def add_media(
            self, 
            type,
            title,
            date_added,
            release_year,
            rating,
            duration,
            description
    ):
        self.cursor.execute(
            """
            INSERT INTO Media (type, title, date_added, release_year, rating, duration, description)
            VALUES (:type, :title, :date_added, :release_year, :rating, :duration, :description)
            """,
            {
                "type":type,
                "title":title,
                "date_added":date_added,
                "release_year":release_year,
                "rating":rating,
                "duration":duration,
                "description":description
            }
        )
        return self.cursor.lastrowid

    def add_or_get_rating(
            self,
            rating: str
    ):
        id = self.cursor.execute(
            """
            SELECT rating_id
            FROM Rating
            WHERE name = :name
            """, {
                "name":rating
            }
        ).fetchone()
        if id is None:
            self.cursor.execute(
                """
                INSERT INTO Rating (name)
                VALUES (:name)
                """,
                {
                    "name":rating
                }
            )
            id = self.cursor.lastrowid
            return id
        return id[0]

    def add_driver(
        self,
        name: str,
        nationality: str,
        race_entries: int,
        race_starts: int,
        pole_positions: int,
        race_wins: int,
        podiums: int,
        fastest_laps: int,
        points: float,
    ):
        """
        adds a driver to the database
        """
        self.cursor.execute(
            """
            INSERT INTO Driver (name, nationality, race_entries, race_starts, pole_positions, race_wins, podiums, fastest_laps, points)
            VALUES (:name, :nationality, :race_entries, :race_starts, :pole_positions, :race_wins, :podiums, :fastest_laps, :points)
            """,
            {
                "name": name,
                "nationality": nationality,
                "race_entries": race_entries,
                "race_starts": race_starts,
                "pole_positions": pole_positions,
                "race_wins": race_wins,
                "podiums": podiums,
                "fastest_laps": fastest_laps,
                "points": points,
            },
        )

        return self.cursor.lastrowid
        
        
    def add_season(self, year: int, champion: int):
        """
        adds a season to the database
        """
        self.cursor.execute(
            """
            INSERT INTO Seasons
            VALUES (:year, :champion)
            """,
            {
                "year": year, 
                "champion": champion
            },
        )

    def add_raced(self, driver_id: int, year: int):
        self.cursor.execute(
            """
            INSERT INTO Raced
            VALUES (:driver_id, :year)
            """,
            {
                "driver_id": driver_id, 
                "year": year
            },
        )