# simple menu app about me. console uses plain text; README uses markdown.
DATA = {
    "name": "Elene Pitskhelauri",
    "tagline": "Computer Engineering Student at the University of Georgia • Erasmus Exchange Student for a year at the Linnaeus University",
    "location": "Tbilisi, Georgia",
    "email": "eleneficxelauri01@gmail.com",
    "phone": "",
    "links": {
        "LinkedIn": "https://www.linkedin.com/in/elene-pitskhelauri-a287792bb/",
        "GitHub": "https://github.com/ElenePitskhelauri"
    },
    "education": [
        {"school": "The University of Georgia", "place": "Tbilisi, Georgia",
         "degree": "BSc in Computer Engineering (GPA 3.75)", "dates": "Expected 2027"},
        {"school": "Linnaeus University (Erasmus+)", "place": "Växjö, Sweden",
         "degree": "Exchange year – Computer Engineering", "dates": "Aug 2024 – Jun 2025"},
    ],
    "experience": [{
        "org": "The University of Georgia – Center for Quantum Computing & AI",
        "role": "Laboratory Assistant",
        "dates": "Apr 2024 – Aug 2024",
        "bullets": [
            "Maintained lab info systems; improved data accessibility & workflow.",
            "Set up equipment; ensured performance and safety compliance.",
            "Assisted experiments; recorded data for analysis.",
            "Supported ML model development for research outcomes.",
            "Built robots (LEGO EV3, mBot) and delivered robotics lectures to students."
        ]
    }],
    "projects": [
        {"name": "7-Segment Display Controller (ARM Assembly)",
         "desc": "Low-level control and timing on Raspberry Pi Pico / microcontrollers."},
        {"name": "Hotel Booking System (OO Analysis)",
         "desc": "Use cases, UML, and process modeling; clean modular design."},
        {"name": "3-Sum Problem (Python)",
         "desc": "Algorithm design & benchmarking; matplotlib visualizations."},
        {"name": "Robotics Workshops",
         "desc": "Designed and taught EV3/mBot sessions; hands-on coding for students."},
    ],
    "skills": {
        "Programming": ["Python", "C++", "ARM/Assembly", "HTML/CSS/JS (basics)"],
        "CS": ["Data Structures & Algorithms", "Computer Architecture", "Networks & Security (basics)"],
        "Tools": ["Git", "Microsoft Office", "Arduino basics"],
        "Topics": ["AI basics", "FinTech basics", "Quantum Computing (exposure)"]
    },
    "languages": [
        "Georgian (Native)", "English (Fluent)", "Russian (Fluent)",
        "Czech (Intermediate, studying)", "Turkish (Basic, studying)"
    ],
    "highlights": [
        "Scholarship (Immerse Education Essay Competition, 30% for CS).",
        "Erasmus+ in Slovenia & Norway – certified participation.",
        "University self-government member; led training trips and a robotics lecture."
    ],
    "quote": "Always learning, building, and growing — one project at a time."
}

# -------- console (plain text) --------

def line():
    print("-" * 60)

def show_profile_console():
    print(f"\nHi, I'm {DATA['name']}")
    print(DATA["tagline"])
    line()
    print(f"Location: {DATA['location']}")
    print(f"Email:    {DATA['email']}")
    if DATA["phone"]:
        print(f"Phone:    {DATA['phone']}")
    print(f"LinkedIn: {DATA['links']['LinkedIn']}")
    print(f"GitHub:   {DATA['links']['GitHub']}")

def show_list_console(title, items):
    print(f"\n{title}")
    line()
    for i, x in enumerate(items, 1):
        print(f"{i}. {x}")

def show_education_console():
    out = []
    for e in DATA["education"]:
        out.append(f"{e['school']} ({e['place']}) — {e['degree']} [{e['dates']}]")
    show_list_console("Education", out)

def show_experience_console():
    print("\nExperience")
    line()
    for x in DATA["experience"]:
        print(f"{x['role']} — {x['org']} [{x['dates']}]")
        for b in x["bullets"]:
            print(f"  - {b}")

def show_projects_console():
    out = [f"{p['name']} — {p['desc']}" for p in DATA["projects"]]
    show_list_console("Projects", out)

def show_skills_console():
    print("\nSkills")
    line()
    for k, v in DATA["skills"].items():
        print(f"{k}: " + ", ".join(v))

def show_languages_console():
    show_list_console("Languages", DATA["languages"])

def show_highlights_console():
    show_list_console("Highlights", DATA["highlights"])

# -------- README (markdown) --------

def render_md():
    def section(t): return f"\n## {t}\n"
    def bullets(v): return "".join(f"- {x}\n" for x in v)

    parts = []
    parts.append(f"# Hi, I'm {DATA['name']} 👋\n{DATA['tagline']}\n")
    contact = [f"**Location:** {DATA['location']}", f"**Email:** {DATA['email']}"]
    if DATA["phone"]:
        contact.append(f"**Phone:** {DATA['phone']}")
    parts.append(" | ".join(contact))
    parts.append(f"[LinkedIn]({DATA['links']['LinkedIn']}) | [GitHub]({DATA['links']['GitHub']})")

    parts.append(section("Education"))
    for e in DATA["education"]:
        parts.append(f"**{e['school']}**, {e['place']} — *{e['degree']}*  \n{e['dates']}\n")

    parts.append(section("Experience"))
    for x in DATA["experience"]:
        parts.append(f"**{x['role']}**, {x['org']}  \n{x['dates']}\n")
        parts.append(bullets(x["bullets"]))

    parts.append(section("Projects"))
    for p in DATA["projects"]:
        parts.append(f"- **{p['name']}** — {p['desc']}\n")

    parts.append(section("Skills"))
    for k, v in DATA["skills"].items():
        parts.append(f"- **{k}:** " + ", ".join(v) + "\n")

    parts.append(section("Languages"))
    parts.append(bullets(DATA["languages"]))

    parts.append(section("Highlights"))
    parts.append(bullets(DATA["highlights"]))

    parts.append(f'\n> _"{DATA["quote"]}"_\n')
    return "\n".join(parts).strip() + "\n"

def export_readme():
    md = render_md()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("\nREADME.md created/updated.")

def menu():
    while True:
        print("\n--- About Elene ---")
        print("1) Profile")
        print("2) Education")
        print("3) Experience")
        print("4) Projects")
        print("5) Skills")
        print("6) Languages")
        print("7) Highlights")
        print("8) Export README.md (markdown)")
        print("0) Exit")
        c = input("choose: ").strip()
        if c == "1": show_profile_console()
        elif c == "2": show_education_console()
        elif c == "3": show_experience_console()
        elif c == "4": show_projects_console()
        elif c == "5": show_skills_console()
        elif c == "6": show_languages_console()
        elif c == "7": show_highlights_console()
        elif c == "8": export_readme()
        elif c == "0":
            print("bye.")
            break
        else:
            print("not a choice.")

if __name__ == "__main__":
    menu()
