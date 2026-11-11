team_name = "Bayside Bandits"
games_played = 12
win_rate = 0.75
in_finals = True

def celsius_to_fahrenheit(celsius) -> float:
    return celsius * 9 / 5 + 32


print(celsius_to_fahrenheit(25))

def print_scoreboard(home, home_score, away, away_score) -> None:
    print(f"{home} {home_score} - {away_score} {away}")


print_scoreboard("Lions", 3, "Tigers", 1)

def average(scores) -> float:
    return sum(scores) / len(scores)


def count_words(words) -> dict[str, int]:
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


print(average([70, 85, 90]))
print(count_words(["red", "blue", "red"]))

def get_initials(first_name: str, last_name: str) -> str:
    return first_name[0] + last_name[0]


def total_marks(marks: list[int]) -> int:
    return sum(marks)


initials: str = get_initials("Sam", "Lee")
total: int = total_marks([18, 15, 20])
average_2: float = total / 3
print(initials, total, average_2)