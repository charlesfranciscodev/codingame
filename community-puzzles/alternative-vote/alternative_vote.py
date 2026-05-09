import math


if __name__ == "__main__":
    candidates = {}  # candidate id => name
    votes = []

    # Read game input
    nb_candidates = int(input())
    for i in range(1, nb_candidates + 1):
        name = input()
        candidates[i] = name
    nb_voters = int(input())
    for i in range(nb_voters):
        votes.append([int(v) for v in input().split()])

    # Eliminate candidates
    while len(candidates) > 1:
        # Count votes
        vote_count = [0] * (nb_candidates + 1)
        for vote in votes:
            vote_count[vote[0]] += 1

        # Determine the loser of this round
        min_votes = math.inf
        loser_id = 0
        for candidate_id in candidates.keys():
            nb_votes = vote_count[candidate_id]
            if nb_votes < min_votes:
                min_votes = nb_votes
                loser_id = candidate_id
        print(candidates[loser_id])
        del candidates[loser_id]

        # Remove all the votes for the loser
        for vote in votes:
            vote.remove(loser_id)
        # Reset the vote count
        for i in range(0, nb_candidates + 1):
            vote_count[i] = 0

    winner_id = list(candidates.keys())[0]
    print(f"winner:{candidates.get(winner_id)}")
