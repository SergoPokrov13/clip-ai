def build_windows(segments, window_size=30):
    """
    Собирает окна по 30 секунд.
    """

    windows = []

    if not segments:
        return windows

    current_start = segments[0]["start"]
    current_end = current_start + window_size

    current_text = []

    for segment in segments:

        if segment["end"] <= current_end:

            current_text.append(segment)

        else:

            if current_text:

                windows.append({
                    "start": current_text[0]["start"],
                    "end": current_text[-1]["end"],
                    "text": " ".join(
                        x["text"] for x in current_text
                    )
                })

            current_text = [segment]

            current_start = segment["start"]
            current_end = current_start + window_size

    if current_text:

        windows.append({
            "start": current_text[0]["start"],
            "end": current_text[-1]["end"],
            "text": " ".join(
                x["text"] for x in current_text
            )
        })

    return windows