# ...existing code...
from typing import Dict, Any, List, Optional, Tuple
# Default weights (must sum to 1.0)
DEFAULT_WEIGHTS = {
    "education": 0.20,
    "experience": 0.20,
    "skills": 0.25,
    "certifications": 0.05,
    "location": 0.05,
    "interview": 0.20,
    "resume": 0.03,
    "references": 0.02,
}
EDU_SCORE_MAP = {
    "phd": 1.00,
    "doctorate": 1.00,
    "masters": 0.85,
    "bachelor": 0.70,
    "bachelors": 0.70,
    "diploma": 0.50,
    "highschool": 0.30,
    "none": 0.00,
}
def normalize_education(value: str) -> float:
    if not value:
        return 0.0
    return EDU_SCORE_MAP.get(value.strip().lower(), 0.0)
def normalize_experience(years: float, cap: float = 20.0) -> float:
    if years <= 0:
        return 0.0
    years = float(years)
    return min(years, cap) / cap  # linear up to cap
def normalize_skills(match_score: Any) -> float:
    # Accept either fraction (0-1) or percent (0-100) or list of matched skills
    if match_score is None:
        return 0.0
    if isinstance(match_score, (int, float)):
        val = float(match_score)
        if val > 1.0:
            # treat as percent
            val = val / 100.0
        return max(0.0, min(1.0, val))
    if isinstance(match_score, list):
        # list of booleans or matched skill names => fraction of skills matched is expected externally
        return min(1.0, len(match_score) / max(1, len(match_score)))
    return 0.0
def normalize_certifications(count: int, cap: int = 5) -> float:
    if count is None or count <= 0:
        return 0.0
    return min(count, cap) / cap
def normalize_location(match: Any) -> float:
    # Accept bool, int (0/1), or float 0-1
    if isinstance(match, bool):
        return 1.0 if match else 0.0
    if isinstance(match, (int, float)):
        val = float(match)
        if val > 1:
            # treat >1 as percent
            val = val / 100.0
        return max(0.0, min(1.0, val))
    return 0.0
def normalize_interview(score: Any) -> float:
    if score is None:
        return 0.0
    if isinstance(score, (int, float)):
        val = float(score)
        if val > 1.0:
            val = val / 100.0
        return max(0.0, min(1.0, val))
    return 0.0
def normalize_resume(score: Any) -> float:
    # Expected 0-1 or 0-100
    if score is None:
        return 0.0
    return normalize_interview(score)
def normalize_references(score: Any) -> float:
    return normalize_interview(score)
def apply_criminal_penalty(score: float, has_record: bool, penalty_factor: float = 0.6) -> float:
    return score * penalty_factor if has_record else score
def score_application(applicant: Dict[str, Any], weights: Optional[Dict[str, float]] = None,
                      penalize_criminal: bool = True) -> Tuple[float, Dict[str, float]]:
    """
    applicant expects keys:
      - education (str)
      - years_experience (number)
      - skills_match (0-1 or 0-100 or list)
      - certifications_count (int)
      - location_match (bool or 0-1)
      - interview_score (0-1 or 0-100)
      - resume_quality (0-1 or 0-100)
      - references_strength (0-1 or 0-100)
      - criminal_record (bool)
    Returns (score_0_100, breakdown_dict)
    """
    w = DEFAULT_WEIGHTS.copy()
    if weights:
        w.update(weights)
    # Normalize each component to 0..1
    edu = normalize_education(applicant.get("education"))
    exp = normalize_experience(applicant.get("years_experience", 0))
    skills = normalize_skills(applicant.get("skills_match"))
    certs = normalize_certifications(int(applicant.get("certifications_count", 0)))
    loc = normalize_location(applicant.get("location_match", False))
    interview = normalize_interview(applicant.get("interview_score"))
    resume = normalize_resume(applicant.get("resume_quality"))
    refs = normalize_references(applicant.get("references_strength"))
    breakdown = {
        "education": edu,
        "experience": exp,
        "skills": skills,
        "certifications": certs,
        "location": loc,
        "interview": interview,
        "resume": resume,
        "references": refs,
    }
    # Weighted sum 0..1
    raw_score = sum(breakdown[k] * w.get(k, 0.0) for k in breakdown)
    # Penalty for criminal record if present
    if penalize_criminal and applicant.get("criminal_record"):
        raw_score = apply_criminal_penalty(raw_score, True)
    # Final scaled to 0..100
    final_score = round(raw_score * 100, 2)
    return final_score, {k: round(v * 100, 2) for k, v in breakdown.items()}
def rank_applicants(applicants: List[Dict[str, Any]], top_n: Optional[int] = None,
                    weights: Optional[Dict[str, float]] = None) -> List[Tuple[Dict[str, Any], float, Dict[str, float]]]:
    scored = []
    for a in applicants:
        score, breakdown = score_application(a, weights=weights)
        scored.append((a, score, breakdown))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored if top_n is None else scored[:top_n]
if __name__ == "__main__":
    # Example usage on Windows: run `python c:\Users\sunil\OneDrive\Desktop\AIAPS\assignment-5\task4.py`
    sample = [
        {
            "name": "Alice",
            "education": "Masters",
            "years_experience": 6,
            "skills_match": 85,  # percent
            "certifications_count": 2,
            "location_match": True,
            "interview_score": 78,
            "resume_quality": 0.8,
            "references_strength": 0.7,
            "criminal_record": False,
        },
        {
            "name": "Bob",
            "education": "Bachelors",
            "years_experience": 3,
            "skills_match": 60,
            "certifications_count": 0,
            "location_match": False,
            "interview_score": 65,
            "resume_quality": 0.6,
            "references_strength": 0.4,
            "criminal_record": True,
        },
    ]
    ranked = rank_applicants(sample)
    for app, score, breakdown in ranked:
        print(f"{app.get('name')}: Score={score} Breakdown={breakdown}")
# ...existing code...