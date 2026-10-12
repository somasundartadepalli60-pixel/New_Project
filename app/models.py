from datetime import datetime, timezone
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db

def utcnow():
    return datetime.now(timezone.utc)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False, index=True)
    email = db.Column(db.String(254), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=utcnow, nullable=False)
    progress = db.relationship("TopicProgress", backref="user", cascade="all, delete-orphan")
    bookmarks = db.relationship("Bookmark", backref="user", cascade="all, delete-orphan")
    notes = db.relationship("PersonalNote", backref="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(120), unique=True, nullable=False, index=True)
    title = db.Column(db.String(180), nullable=False)
    unit_number = db.Column(db.Integer, nullable=False, index=True)
    unit_title = db.Column(db.String(160), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    formula = db.Column(db.Text, default="")
    diagram_type = db.Column(db.String(40), default="concept")
    applications = db.Column(db.JSON, default=list)
    source_note = db.Column(db.Text, default="")
    progress = db.relationship("TopicProgress", backref="topic", cascade="all, delete-orphan")

class TopicProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)
    status = db.Column(db.String(20), default="not_started", nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=utcnow, onupdate=utcnow)
    __table_args__ = (db.UniqueConstraint("user_id", "topic_id", name="uq_user_topic_progress"),)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=utcnow)
    __table_args__ = (db.UniqueConstraint("user_id", "topic_id", name="uq_user_topic_bookmark"),)

class PersonalNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)
    body = db.Column(db.Text, nullable=False, default="")
    updated_at = db.Column(db.DateTime(timezone=True), default=utcnow, onupdate=utcnow)
    __table_args__ = (db.UniqueConstraint("user_id", "topic_id", name="uq_user_topic_note"),)

class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    unit_number = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=utcnow)


class StudyPlan(db.Model):
    """A user's active syllabus plan with an explicit target date and study availability."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    title = db.Column(db.String(120), nullable=False, default="My LDICA study plan")
    start_date = db.Column(db.Date, nullable=False)
    deadline = db.Column(db.Date, nullable=False)
    daily_minutes = db.Column(db.Integer, nullable=False, default=120)
    available_days = db.Column(db.JSON, nullable=False, default=lambda: [0, 1, 2, 3, 4, 5, 6])
    pace = db.Column(db.String(20), nullable=False, default="balanced")
    active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime(timezone=True), default=utcnow, nullable=False)
    tasks = db.relationship("StudyTask", backref="plan", cascade="all, delete-orphan",
                             order_by="StudyTask.scheduled_date")

class StudyTask(db.Model):
    """One planned learning session. A topic may be split into several tasks."""
    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey("study_plan.id"), nullable=False, index=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)
    scheduled_date = db.Column(db.Date, nullable=False, index=True)
    estimated_minutes = db.Column(db.Integer, nullable=False)
    sequence_number = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="planned")
    topic = db.relationship("Topic")


class ConceptMastery(db.Model):
    """Per-user, per-concept mastery summary computed from observed practice answers."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    concept_key = db.Column(db.String(100), nullable=False, index=True)
    concept_title = db.Column(db.String(180), nullable=False)
    unit_number = db.Column(db.Integer, nullable=False)
    attempts = db.Column(db.Integer, nullable=False, default=0)
    correct_count = db.Column(db.Integer, nullable=False, default=0)
    consecutive_correct = db.Column(db.Integer, nullable=False, default=0)
    mastery_score = db.Column(db.Float, nullable=False, default=0.0)
    last_seen_at = db.Column(db.DateTime(timezone=True), default=utcnow, nullable=False)
    next_review_at = db.Column(db.DateTime(timezone=True), default=utcnow, nullable=False)
    __table_args__ = (db.UniqueConstraint("user_id", "concept_key", name="uq_user_concept_mastery"),)

    @property
    def accuracy(self):
        return round((self.correct_count / self.attempts) * 100) if self.attempts else 0


class MasteryResponse(db.Model):
    """An auditable response used to explain mastery recommendations."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    question_key = db.Column(db.String(100), nullable=False)
    concept_key = db.Column(db.String(100), nullable=False, index=True)
    unit_number = db.Column(db.Integer, nullable=False)
    selected_index = db.Column(db.Integer, nullable=False, default=-1)
    correct_index = db.Column(db.Integer, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False, default=False)
    selected_text = db.Column(db.String(300), nullable=False, default="Not answered")
    misconception = db.Column(db.Text, nullable=False, default="")
    explanation = db.Column(db.Text, nullable=False, default="")
    reviewed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=utcnow, nullable=False, index=True)

class ReviewSchedule(db.Model):
    """Per-user spaced-repetition state for a lesson-derived revision card."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False, index=True)
    repetitions = db.Column(db.Integer, nullable=False, default=0)
    interval_days = db.Column(db.Integer, nullable=False, default=0)
    ease_factor = db.Column(db.Float, nullable=False, default=2.5)
    due_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, index=True)
    last_rating = db.Column(db.String(12), nullable=False, default="new")
    review_count = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, onupdate=utcnow)
    topic = db.relationship("Topic")
    __table_args__ = (db.UniqueConstraint("user_id", "topic_id", name="uq_user_topic_review_schedule"),)


class LearningPreference(db.Model):
    """Small, explicit study preferences used to tailor local recommendations."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, unique=True, index=True)
    daily_goal_minutes = db.Column(db.Integer, nullable=False, default=30)
    preferred_session_minutes = db.Column(db.Integer, nullable=False, default=15)
    preferred_unit = db.Column(db.Integer, nullable=False, default=0)
    reminder_style = db.Column(db.String(20), nullable=False, default="gentle")
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, onupdate=utcnow)


class PracticalAssignment(db.Model):
    """A reusable assignment or lab brief created within the learning hub."""
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    title = db.Column(db.String(160), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    unit_number = db.Column(db.Integer, nullable=False, default=0, index=True)
    due_date = db.Column(db.Date, nullable=True, index=True)
    rubric_json = db.Column(db.Text, nullable=False, default="[]")
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, index=True)
    submissions = db.relationship("PracticalSubmission", backref="assignment", cascade="all, delete-orphan")


class PracticalSubmission(db.Model):
    """Per-user lab report with saved drafts and transparent self-assessment scores."""
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey("practical_assignment.id"), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    aim = db.Column(db.Text, nullable=False, default="")
    theory = db.Column(db.Text, nullable=False, default="")
    procedure = db.Column(db.Text, nullable=False, default="")
    observations = db.Column(db.Text, nullable=False, default="")
    analysis = db.Column(db.Text, nullable=False, default="")
    conclusion = db.Column(db.Text, nullable=False, default="")
    viva_answers = db.Column(db.Text, nullable=False, default="")
    status = db.Column(db.String(20), nullable=False, default="draft", index=True)
    rubric_scores_json = db.Column(db.Text, nullable=False, default="{}")
    rubric_total = db.Column(db.Integer, nullable=False, default=0)
    rubric_max = db.Column(db.Integer, nullable=False, default=0)
    submitted_at = db.Column(db.DateTime(timezone=True), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, onupdate=utcnow)
    __table_args__ = (db.UniqueConstraint("assignment_id", "user_id", name="uq_assignment_user_submission"),)

class AcademicCourse(db.Model):
    """Versioned course shell for organising LDICA units and outcomes."""
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(30), unique=True, nullable=False, index=True)
    title = db.Column(db.String(180), nullable=False)
    description = db.Column(db.Text, nullable=False, default="")
    syllabus_version = db.Column(db.String(40), nullable=False, default="R23")
    academic_year = db.Column(db.String(20), nullable=False, default="")
    status = db.Column(db.String(20), nullable=False, default="draft", index=True)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, onupdate=utcnow)
    outcomes = db.relationship("LearningOutcome", backref="course", cascade="all, delete-orphan", order_by="LearningOutcome.code")
    terms = db.relationship("AcademicTerm", backref="course", cascade="all, delete-orphan", order_by="AcademicTerm.start_date")


class AcademicTerm(db.Model):
    """Academic delivery window attached to a course."""
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("academic_course.id"), nullable=False, index=True)
    name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="planned")
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    __table_args__ = (db.CheckConstraint("end_date >= start_date", name="ck_academic_term_date_order"),)


class LearningOutcome(db.Model):
    """Course learning outcome mapped to catalogue topics."""
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("academic_course.id"), nullable=False, index=True)
    code = db.Column(db.String(30), nullable=False)
    statement = db.Column(db.String(500), nullable=False)
    bloom_level = db.Column(db.String(30), nullable=False, default="Understand")
    assessment_method = db.Column(db.String(100), nullable=False, default="Quiz / examination")
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    topic_links = db.relationship("OutcomeTopicMap", backref="outcome", cascade="all, delete-orphan")
    __table_args__ = (db.UniqueConstraint("course_id", "code", name="uq_course_outcome_code"),)


class OutcomeTopicMap(db.Model):
    """Explicit many-to-many map between a learning outcome and a catalogue topic."""
    id = db.Column(db.Integer, primary_key=True)
    outcome_id = db.Column(db.Integer, db.ForeignKey("learning_outcome.id"), nullable=False, index=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False, index=True)
    coverage_level = db.Column(db.String(20), nullable=False, default="introduced")
    notes = db.Column(db.String(500), nullable=False, default="")
    topic = db.relationship("Topic")
    __table_args__ = (db.UniqueConstraint("outcome_id", "topic_id", name="uq_outcome_topic_map"),)


class ContentReview(db.Model):
    """Auditable approval workflow for syllabus/lesson content changes."""
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False, index=True)
    submitted_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    change_summary = db.Column(db.String(240), nullable=False)
    proposed_content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="pending", index=True)
    reviewer_notes = db.Column(db.Text, nullable=False, default="")
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    reviewed_at = db.Column(db.DateTime(timezone=True), nullable=True)
    topic = db.relationship("Topic")
    submitter = db.relationship("User", foreign_keys=[submitted_by])
    reviewer = db.relationship("User", foreign_keys=[reviewer_id])


class StudyGroup(db.Model):
    """A small private classroom/study group owned by its creator."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False, default="")
    join_code = db.Column(db.String(16), unique=True, nullable=False, index=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    owner = db.relationship("User", foreign_keys=[owner_id])
    members = db.relationship("StudyGroupMember", backref="group", cascade="all, delete-orphan")
    posts = db.relationship("GroupDiscussionPost", backref="group", cascade="all, delete-orphan", order_by="GroupDiscussionPost.created_at.desc()")
    announcements = db.relationship("GroupAnnouncement", backref="group", cascade="all, delete-orphan", order_by="GroupAnnouncement.created_at.desc()")
    shared_lists = db.relationship("SharedRevisionList", backref="group", cascade="all, delete-orphan")
    challenges = db.relationship("PeerQuizChallenge", backref="group", cascade="all, delete-orphan")


class StudyGroupMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("study_group.id"), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    role = db.Column(db.String(16), nullable=False, default="member")
    joined_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    user = db.relationship("User")
    __table_args__ = (db.UniqueConstraint("group_id", "user_id", name="uq_group_member"),)


class GroupDiscussionPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("study_group.id"), nullable=False, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    body = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(16), nullable=False, default="visible", index=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow, index=True)
    author = db.relationship("User")


class GroupAnnouncement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("study_group.id"), nullable=False, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(140), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    author = db.relationship("User")


class SharedRevisionList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("study_group.id"), nullable=False, index=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False, default="")
    topic_ids_json = db.Column(db.Text, nullable=False, default="[]")
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    creator = db.relationship("User")


class PeerQuizChallenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("study_group.id"), nullable=False, index=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    unit_number = db.Column(db.Integer, nullable=False, default=0)
    question_count = db.Column(db.Integer, nullable=False, default=5)
    closes_at = db.Column(db.DateTime(timezone=True), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=utcnow)
    creator = db.relationship("User")
