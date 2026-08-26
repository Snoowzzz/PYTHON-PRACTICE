### PHASE — OOP: Mixed with prior topics (step 1)
# Q1. [OOP + loops/lists]
#     Create a class Playlist with __init__(self, songs) where songs is a
#     list of (title, duration_in_minutes) tuples. Add a method
#     total_duration() that loops through songs and returns the sum of
#     all durations.


# Q2. [OOP + dict]
#     Create a class Inventory with __init__(self) that starts with an
#     empty dict self.stock. Add add_item(name, qty) — if name already
#     exists, increase its quantity; if not, add it. Add total_items()
#     returning the sum of all quantities in the dict.


# Q3. [OOP + string methods]
#     Create a class Message with __init__(self, text). Add word_count()
#     returning the number of words in text (use .split()), and
#     shout() returning text fully uppercased.


# Q4. [OOP + lambda/sorted]
#     Create a class Leaderboard with __init__(self, players) where
#     players is a list of (name, score) tuples. Add top_player()
#     returning the name of whoever has the highest score — use sorted()
#     with a lambda key, don't loop manually.


# Q5. [OOP + composition — one class holding objects of another]
#     Create a class Player with __init__(self, name, score). Create a
#     class Team with __init__(self, team_name, players) where players is
#     a LIST OF Player OBJECTS (not tuples this time). Add
#     average_score() that loops through self.players, pulling
#     player.score off each one, and returns the average.