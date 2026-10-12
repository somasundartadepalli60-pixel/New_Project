import os
import secrets
from dotenv import load_dotenv
from flask import Flask
from .extensions import db, migrate, csrf, login_manager
from .security.hardening import install_security_hardening
from .content.catalog import UNITS
from .models import User, Topic, TopicProgress, Bookmark, PersonalNote, QuizAttempt, StudyPlan, StudyTask, ConceptMastery, MasteryResponse

# Load a local .env before reading environment-based configuration. Existing OS
# environment variables take precedence, and no external API keys are required.
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=(
            os.environ.get("SECRET_KEY", "").strip()
            if os.environ.get("SECRET_KEY", "").strip()
            and not os.environ.get("SECRET_KEY", "").strip().lower().startswith("replace-with-")
            else load_local_secret(app.instance_path)
        ),
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            "DATABASE_URL", "sqlite:///" + os.path.join(app.instance_path, "ldica.db")
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_TIME_LIMIT=None,
    )
    if test_config:
        app.config.update(test_config)

    # Flask already defines SESSION_COOKIE_SECURE=False, so setdefault() would
    # never enable it in production. Respect an explicit test/app config first,
    # then an environment override, then infer production from deployment env.
    if not test_config or "SESSION_COOKIE_SECURE" not in test_config:
        secure_cookie = os.environ.get("SESSION_COOKIE_SECURE")
        if secure_cookie is not None:
            app.config["SESSION_COOKIE_SECURE"] = secure_cookie.strip().lower() in {"1", "true", "yes", "on"}
        else:
            environment = os.environ.get("ENVIRONMENT", os.environ.get("FLASK_ENV", "")).strip().lower()
            app.config["SESSION_COOKIE_SECURE"] = environment in {"production", "prod"}
    install_security_hardening(app)

    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    from .routes.main import main_bp
    from .routes.auth import auth_bp
    from .routes.learning import learning_bp
    from .routes.dashboard import dashboard_bp
    from .routes.practice import practice_bp
    from .routes.planner import planner_bp
    from .routes.tutor import tutor_bp
    from .routes.media import media_bp
    from .routes.tools import tools_bp
    from .routes.lab import lab_bp
    from .routes.mastery import mastery_bp
    from .routes.graph import graph_bp
    from .routes.curriculum import curriculum_bp
    from .routes.assessments import assessments_bp
    from .routes.engineering import engineering_bp
    from .routes.analytics import analytics_bp
    from .routes.search import search_bp
    from .routes.practicals import practicals_bp
    from .routes.academic import academic_bp
    from .routes.community import community_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(learning_bp, url_prefix="/learn")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(practice_bp, url_prefix="/practice")
    app.register_blueprint(tools_bp, url_prefix="/tools")
    app.register_blueprint(planner_bp, url_prefix="/planner")
    app.register_blueprint(tutor_bp, url_prefix="/tutor")
    app.register_blueprint(media_bp, url_prefix="/media")
    app.register_blueprint(lab_bp, url_prefix="/lab")
    app.register_blueprint(mastery_bp, url_prefix="/mastery")
    app.register_blueprint(graph_bp, url_prefix="/graph")
    app.register_blueprint(curriculum_bp, url_prefix="/curriculum")
    app.register_blueprint(assessments_bp, url_prefix="/assessments")
    app.register_blueprint(engineering_bp, url_prefix="/engineering")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")
    app.register_blueprint(search_bp, url_prefix="/search")
    app.register_blueprint(practicals_bp, url_prefix="/practicals")
    app.register_blueprint(academic_bp, url_prefix="/academic")
    app.register_blueprint(community_bp, url_prefix="/community")

    @app.errorhandler(413)
    def request_too_large(_error):
        return "Request too large. Please reduce the uploaded content and try again.", 413

    @app.errorhandler(500)
    def internal_server_error(_error):
        db.session.rollback()
        return "Something went wrong. Please try again. If the issue continues, contact the site administrator.", 500

    with app.app_context():
        db.create_all()
        seed_catalog()

    return app

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

def seed_catalog():
    for unit in UNITS:
        for topic in unit["topics"]:
            existing = Topic.query.filter_by(slug=topic["slug"]).first()
            if not existing:
                db.session.add(Topic(
                    slug=topic["slug"], title=topic["title"],
                    unit_number=unit["number"], unit_title=unit["title"],
                    summary=topic["summary"], explanation=topic["explanation"],
                    formula=topic.get("formula", ""), diagram_type=topic.get("diagram_type", "concept"),
                    applications=topic.get("applications", []),
                    source_note=topic.get("source_note", "Syllabus topic; verify detailed derivation against the supplied unit notes.")
                ))
    db.session.commit()


def load_local_secret(instance_path):
    """Create a local-only session signing key on first run; no provider/API key is needed."""
    os.makedirs(instance_path, exist_ok=True)
    key_path = os.path.join(instance_path, ".local_session_key")
    try:
        with open(key_path, "r", encoding="utf-8") as key_file:
            key = key_file.read().strip()
            if len(key) >= 32:
                return key
    except OSError:
        pass
    key = secrets.token_urlsafe(48)
    try:
        with open(key_path, "w", encoding="utf-8") as key_file:
            key_file.write(key)
        try:
            os.chmod(key_path, 0o600)
        except OSError:
            pass
    except OSError:
        # Ephemeral fallback still avoids a hardcoded secret; sessions reset on restart.
        return key
    return key

# Safe, non-diagnostic error responses. Details remain in server-side logs.
