# LDICA expansion roadmap (Phases 6–20)

This roadmap defines the implementation order. A phase is complete only when its functionality, tests, documentation, and integration checks are present; a heading or placeholder alone is not completion evidence.

| Phase | Scope | Current status |
|---|---|---|
| 1–5 | Core hub, mastery, signal workbench, concept graph, smart revision | Existing project baseline; re-verify during regression testing |
| 6 | Curriculum content engine and quality audit | Initial implementation added: catalogue audit and coverage filters |
| 7 | Question bank and assessment engine | Initial implementation added: searchable local reviewed-starter bank |
| 8 | Timed mock exams | Initial implementation added: timed unit/mixed sessions, server scoring, history |
| 9 | Digital logic simulator | Initial implementation added: gate truth-table explorer and CSV export |
| 10 | Sequential circuits and timing simulator | Initial implementation added: clock-edge DFF and modulo-counter state sequences |
| 11 | Analog virtual lab expansion | Initial implementation added: inverting/non-inverting gain, 555 estimate, ADC step, RC time constant |
| 12 | Formula and derivation workbench | Initial implementation added: selected formula evaluator and unit/assumption notes |
| 13 | Personalisation and spaced revision expansion | Initial implementation added: active recall, review ratings, due scheduling and per-user preferences; broaden coverage in regression review |
| 14 | Advanced learning analytics | Initial implementation added: personal practice trends, unit comparisons, mastery and CSV export; verify runtime integration |
| 15 | Local study assistant and indexed search | Initial implementation added: ranked local lesson search, bundled PDF page text search, unit filters, snippets, lesson/source-page links, JSON endpoint; OCR remains needed for scanned pages |
| 16 | Assignment and practical-work system | Initial implementation added: assignment briefs, saved/submitted reports, rubric self-assessment and practical history; regression verify |
| 17 | Course and academic administration | Initial implementation added: course register/version metadata, academic terms, learning outcomes, topic mappings, admin-gated publishing and separate content-review decisions |
| 18 | Collaboration and classroom features | Pending |
| 19 | Security, accessibility and reliability | Pending |
| 20 | Extension framework and quality engineering | Pending |

LOC target: measure source files with a repeatable script and report blank-inclusive and nonblank counts separately. Never count generated PDF content, dependencies, virtual environments, build artefacts, duplicate code, or caches as authored source LOC.
| 18 | Collaboration and classroom features | Initial implementation added: private join-code study groups, membership-gated discussions, owner announcements, shared revision lists, peer-practice challenge targets, and post hide/delete controls; continue full runtime and usability validation |


## Phase 19 — Security, Accessibility & Reliability
- Security response headers, per-request diagnostics, configurable secure cookie defaults, request-size limit and generic error responses.
- Accessible skip navigation, visible focus and reduced-motion support.
- SQLite online backup utility with integrity check and deployment/recovery checklist.
- Automated tests for headers, configuration and accessibility landmarks.


## Phase 20 — Extension Framework & Quality Engineering

Implemented an explicit trusted plugin registry, deployment diagnostics, quality-check guidance and focused tests. See `phase20-extension-quality.md`.
