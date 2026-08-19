"""Sync the LMS learningUnits (what the live course page renders as the syllabus)
to the v12.0 courseware, and drop the stray subtopic left over from another course.

Read-modify-write via lms_push.build_payload + the {"courseData": ...} envelope,
the same path the working push uses. --apply to write; default is a dry run.
"""
import os, sys, json, importlib.util
DRY = "--apply" not in sys.argv
os.environ.setdefault("LMS_TMS_API_KEY", open(os.path.expanduser("~/.claude/lms_tms_api_key")).read().strip())
sys.path.insert(0, ".claude/skills/courseware-build/build")
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
ACT = DOMAIN1 + DOMAIN2 + DOMAIN3

spec = importlib.util.spec_from_file_location("lp", ".claude/scripts/lms_push.py")
lp = importlib.util.module_from_spec(spec); _argv = sys.argv; sys.argv = ["lms_push.py", "--dry-run"]
try: spec.loader.exec_module(lp)
except SystemExit: pass
sys.argv = _argv

CID = "a82fa945-f407-4205-b9c1-676e0607e6f6"
course = (lp.get_json(f"{lp.API}/api/courses/edit-data?courseId={CID}") or {}).get("data") or {}
if not course: raise SystemExit("no course object")

WATCH = ("trainerSlidesUrl","slidesUrl","learnerGuideUrl","lessonPlanUrl",
         "practicalPerformanceAssessmentLink","activitiesUrl","courseLink","title","courseCode")
before = {k: course.get(k) for k in WATCH}
before_oq = ((course.get("assessmentMethods") or {}).get("oralQuestioning") or {}).get("link","")

# Desired syllabus: the topic subtitles, then each activity, from the single source.
want = []
for t in C.TOPICS:
    subs = [s.strip() for s in t["subtitle"].split("·")]
    subs += [f"Activity {a['num']}: {a['title']}" for a in ACT if a["topic"] == t["num"]]
    want.append((f"Topic {t['num']}: {t['title']}", subs))

units = course.get("topics") or course.get("learningUnits") or []
print(f"{'DRY RUN — ' if DRY else ''}syncing {len(units)} learning units\n")
for i, (title, subs) in enumerate(want):
    u = units[i] if i < len(units) else None
    if u is None:
        print(f"! no existing unit {i+1} on the LMS — skipping"); continue
    old = [s.get("title") for s in (u.get("subtopics") or [])]
    print(f"TOPIC {i+1}: {u.get('title')!r}")
    if u.get("title") != title:
        print(f"   title: {u.get('title')!r} -> {title!r}")
    for o in old:
        if o not in subs: print(f"   REMOVE  {o}")
    for s in subs:
        if s not in old: print(f"   ADD     {s}")
    u["title"] = title
    u["subtopics"] = [{"id": None, "title": s} for s in subs]
    print()

course["topics"] = units
payload = lp.build_payload(course, {})
for must in ("title", "courseCode"):
    if not payload.get(must): raise SystemExit(f"Refusing to PUT: '{must}' empty")
n = sum(len(u.get("subtopics") or []) for u in payload["learningUnits"])
print(f"payload: {len(payload['learningUnits'])} units, {n} subtopics")
if DRY:
    print("\nDry run — nothing written. Re-run with --apply."); raise SystemExit(0)

status, body = lp.put_multipart(f"{lp.API}/api/courses/update-course?courseId={CID}",
                                {"courseData": json.dumps(payload)})
if not body.get("success", status == 200):
    raise SystemExit(f"rejected ({status}): {json.dumps(body)[:300]}")
print("PUT update-course ->", status)

after = (lp.get_json(f"{lp.API}/api/courses/edit-data?courseId={CID}") or {}).get("data", {})
print("\nread back:")
for u in (after.get("topics") or after.get("learningUnits") or []):
    print(" ", u.get("title"))
    for s in (u.get("subtopics") or []): print("     -", s.get("title"))
print("\nregression check:")
ok = True
for k, v in before.items():
    same = after.get(k) == v; ok &= same
    print(f"  {k:38s} {'OK' if same else f'CHANGED -> {after.get(k)!r}'}")
oq = ((after.get("assessmentMethods") or {}).get("oralQuestioning") or {}).get("link","")
same = oq == before_oq; ok &= same
print(f"  {'oralQuestioning link':38s} {'OK' if same else f'CHANGED -> {oq!r}'}")
print("\nRESULT:", "syllabus updated, nothing else touched" if ok else "REVIEW ABOVE")
