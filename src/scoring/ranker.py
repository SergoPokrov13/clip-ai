from src.scoring.score_engine import calculate_score


def rank_windows(windows, audio_events):

    ranked = []

    for window in windows:
        ranked.append(
            calculate_score(window, audio_events)
        )

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked