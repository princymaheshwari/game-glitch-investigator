from logic_utils import check_guess, update_score, get_range_for_difficulty, reset_game

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Hints were reversed ---

def test_check_guess_too_high_returns_correct_outcome():
    # guess above secret must return Too High, not Too Low
    assert check_guess(60, 50) == "Too High"

def test_check_guess_too_low_returns_correct_outcome():
    # guess below secret must return Too Low, not Too High
    assert check_guess(40, 50) == "Too Low"

def test_check_guess_correct():
    assert check_guess(50, 50) == "Win"


# --- Type coercion bug: check_guess must work correctly with two ints ---

def test_check_guess_no_string_coercion_high():
    # 9 vs 50 — string comparison "9" > "50" is True, numeric is False
    # must return Too Low, not Too High
    assert check_guess(9, 50) == "Too Low"

def test_check_guess_no_string_coercion_low():
    assert check_guess(50, 9) == "Too High"


# --- Attempts must start at 0 ---

def test_reset_game_attempts_start_at_zero():
    state = reset_game(1, 100)
    assert state["attempts"] == 0


# --- New game resets all state ---

def test_reset_game_clears_score():
    state = reset_game(1, 100)
    assert state["score"] == 0

def test_reset_game_clears_status():
    state = reset_game(1, 100)
    assert state["status"] == "playing"

def test_reset_game_clears_history():
    state = reset_game(1, 100)
    assert state["history"] == []


# --- reset_game secret stays within the difficulty range ---

def test_reset_game_secret_within_easy_range():
    for _ in range(50):
        state = reset_game(1, 20)
        assert 1 <= state["secret"] <= 20

def test_reset_game_secret_within_hard_range():
    for _ in range(50):
        state = reset_game(1, 200)
        assert 1 <= state["secret"] <= 200


# --- Score deducts equally for both wrong guess types ---

def test_update_score_too_high_subtracts():
    # must subtract 5, never add
    assert update_score(100, "Too High", 1) == 95
    assert update_score(100, "Too High", 2) == 95  # even attempt — was adding 5 before fix

def test_update_score_too_low_subtracts():
    assert update_score(100, "Too Low", 1) == 95
    assert update_score(100, "Too Low", 2) == 95

def test_update_score_wrong_guess_consistent():
    # both directions must produce the same deduction
    assert update_score(100, "Too High", 3) == update_score(100, "Too Low", 3)


# --- Win on attempt 1 should give 100 points ---

def test_update_score_win_attempt_1_gives_100():
    # 100 - 10 * (1 - 1) = 100
    assert update_score(0, "Win", 1) == 100

def test_update_score_win_decreases_with_attempts():
    # each extra attempt reduces the win bonus by 10
    assert update_score(0, "Win", 2) == 90
    assert update_score(0, "Win", 3) == 80

def test_update_score_win_minimum_10_points():
    # score should never drop below 10 for a win
    assert update_score(0, "Win", 100) == 10


# --- Hard difficulty must be harder (wider range) than Normal ---

def test_hard_range_wider_than_normal():
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    assert (hard_high - hard_low) > (normal_high - normal_low)

def test_easy_range_narrower_than_normal():
    normal_low, normal_high = get_range_for_difficulty("Normal")
    easy_low, easy_high = get_range_for_difficulty("Easy")
    assert (easy_high - easy_low) < (normal_high - normal_low)

def test_get_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_get_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_get_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert high > 100  # must exceed Normal's upper bound
