"""Transparent concept-mastery calculations for LDICA practice.

This is a rule-based educational aid, not a generative AI model or a diagnosis
of a student's ability. Recommendations are based only on recorded answers.
"""
from datetime import datetime, timedelta, timezone


def utcnow():
    return datetime.now(timezone.utc)


def next_review_delay_days(mastery_score, consecutive_correct):
    """Return a conservative spaced-review interval based on recent evidence."""
    if mastery_score < 40 or consecutive_correct == 0:
        return 1
    if mastery_score < 65 or consecutive_correct < 2:
        return 2
    if mastery_score < 85 or consecutive_correct < 3:
        return 5
    return 10


def update_mastery(record, is_correct, now=None):
    """Update one ConceptMastery-like record in place and return it."""
    now = now or utcnow()
    record.attempts += 1
    if is_correct:
        record.correct_count += 1
        record.consecutive_correct += 1
    else:
        record.consecutive_correct = 0
    # Recent streak contributes modestly; raw accuracy remains the main signal.
    accuracy = record.correct_count / record.attempts
    # Require repeated evidence before a concept can appear fully mastered.
    confidence = min(record.attempts / 4, 1.0)
    streak_bonus = min(record.consecutive_correct * 2.5, 10) / 100
    record.mastery_score = round(min(1.0, accuracy * confidence * 0.9 + streak_bonus) * 100, 1)
    record.last_seen_at = now
    record.next_review_at = now + timedelta(days=next_review_delay_days(
        record.mastery_score, record.consecutive_correct
    ))
    return record


def recommendation_for(record, now=None):
    """Describe the next action using score and review timing, not opaque AI."""
    now = now or utcnow()
    next_review = record.next_review_at
    if next_review is not None and next_review.tzinfo is None:
        next_review = next_review.replace(tzinfo=timezone.utc)
    due = next_review is None or next_review <= now
    if record.attempts == 0:
        return {"label": "Start here", "reason": "No practice evidence has been recorded yet.", "priority": 1}
    if record.mastery_score < 55:
        return {"label": "Relearn and practise", "reason": "Recent answers show this concept needs another explanation and a short practice set.", "priority": 0}
    if due and record.mastery_score < 80:
        return {"label": "Review now", "reason": "This concept is due for a spaced-revision check.", "priority": 1}
    if record.mastery_score >= 80:
        return {"label": "Maintain mastery", "reason": "Keep the concept active with an occasional mixed question.", "priority": 3}
    return {"label": "Build consistency", "reason": "Try another question to make the result more reliable.", "priority": 2}
