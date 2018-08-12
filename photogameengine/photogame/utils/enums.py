from enum import Enum

class Categories(Enum):
    PEOPLE = "People"
    NATURE = "Nature"
    CITYLIFE = "City Life"
    LOVE = "Love"
    SPORTS = "Sports"
    FAMILY = "Family"

class VoteTypes(Enum):
    UPVOTE = 1
    DOWNVOTE = 0