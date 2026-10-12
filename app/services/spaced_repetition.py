"""Transparent spaced-repetition scheduling for the LDICA learning hub.

The scheduler is deliberately deterministic and local-first. Ratings are learner
self-reports, not proof of mastery; objective quiz evidence remains separate.
"""
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

RATINGS = {"again", "hard", "good", "easy"}

@dataclass(frozen=True)
class ReviewDecision:
    interval_days: int
    ease_factor: float
    repetitions: int
    due_at: datetime
    message: str


def schedule_next_review(rating, repetitions=0, interval_days=0, ease_factor=2.5, now=None):
    """Calculate the next review date for Again/Hard/Good/Easy ratings.

    Again resets the streak and schedules a short relearning interval. Hard keeps
    a conservative interval. Good grows intervals gradually; Easy grows faster.
    Ease is bounded to prevent extreme intervals after repeated ratings.
    """
    if rating not in RATINGS:
        raise ValueError("rating must be one of: again, hard, good, easy")
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    repetitions = max(0, int(repetitions))
    interval_days = max(0, int(interval_days))
    ease_factor = min(3.0, max(1.3, float(ease_factor)))

    if rating == "again":
        repetitions, interval_days = 0, 1
        ease_factor = max(1.3, ease_factor - 0.2)
        message = "Revisit tomorrow; this card needs relearning."
    elif rating == "hard":
        repetitions += 1
        interval_days = max(1, round(interval_days * 1.2)) if interval_days else 2
        ease_factor = max(1.3, ease_factor - 0.15)
        message = "A short interval is scheduled because recall felt difficult."
    elif rating == "good":
        repetitions += 1
        interval_days = 1 if repetitions == 1 else 3 if repetitions == 2 else max(4, round(max(interval_days, 3) * ease_factor))
        message = "The next review is spaced further apart after successful recall."
    else:
        repetitions += 1
        interval_days = 4 if repetitions == 1 else 7 if repetitions == 2 else max(5, round(max(interval_days, 4) * (ease_factor + 0.35)))
        ease_factor = min(3.0, ease_factor + 0.15)
        message = "A longer interval is scheduled after easy recall."

    interval_days = min(interval_days, 180)
    return ReviewDecision(interval_days, round(ease_factor, 2), repetitions,
                          now + timedelta(days=interval_days), message)
