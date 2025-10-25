from textwrap import indent, dedent

DATA = {
    "name": "Elene Pitskhelauri",
    "tagline": "Computer Engineering Student at the University of Georgia • Erasmus Exchange Student for a year at the Linnaeus University",
    "location": "Tbilisi, Georgia",
    "email": "eleneficxelauri01@gmail.com",
    "links": {
        "LinkedIn": "https://www.linkedin.com/in/elene-pitskhelauri-a287792bb/",
        "GitHub": "https://github.com/ElenePitskhelauri"  # ← update if different
    },
    "education": [
        {
            "school": "The University of Georgia",
            "place": "Tbilisi, Georgia",
            "degree": "BSc in Computer Engineering (GPA 3.75)",
            "dates": "Expected 2027"
        },
        {
            "school": "Linnaeus University (Erasmus+)",
            "place": "Växjö, Sweden",
            "degree": "Exchange year – Computer Engineering",
            "dates": "Aug 2024 – Jun 2025"
        }
    ],
    "experience": [
        {
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
        }
    ],
    "projects": [
        {
            "name": "7-Segment Display Controller (ARM Assembly)",
            "desc": "Low-level control and timing on Raspberry Pi Pico / microcontrollers."
        },
        {
            "name": "Hotel Booking System (OO Analysis)",
            "desc": "Use cases, UML, and process modeling; clean modular design."
        },
        {
            "name": "3-Sum Problem (Python)",
            "desc": "Algorithm design & benchmarking; matplotlib visualizations."
        },
        {
            "name": "Robotics Workshops",
            "desc": "Designed and taught EV3/mBot sessions; hands-on coding for students."
        }
    ],
    "skills": {
        "Programming": ["Python", "C++", "ARM/Assembly", "HTML/CSS/JS (basics)"],
        "CS": ["Data Structures & Algorithms", "Computer Architecture", "Networks & Security (basics)"],
        "Tools": ["Git", "Microsoft Office", "Arduino basics"],
        "Topics": ["AI basics", "FinTech basics", "Quantum Computing (exposure)"]
    },
    "languages": [
        "Georgian (Native)",
        "English (Fluent)",
        "Russian (Fluent)",
        "Czech (Intermediate, studying)",
        "Turkish (Basic, studying)"
    ],
    "highlights": [
        "Scholarship (Immerse Education Essay Competition, 30% for CS).",
        "Erasmus+ in Slovenia & Norway – certified participation.",
        "University self-government member; led training trips and a robotics lecture."
    ],
    "quote": "Always learning, building, and growing — one project at a time."
}

# ---------- rendering helpers ----------

def section(title: str) -> str:
    return f"\n## {title}\n"

def bullet_list(items):
    return "".join([f"- {item}\n" for item in items])

def render_profile() -> str:
    lines = [
        f"# Hi, I'm {DATA['name']} 👋",
        DATA["tagline"],
        "",
        f"**Location:** {DATA['location']}",
        f"**Email:** {DATA['email']}  |  **Phone:** {DATA['phone']}",
        " | ".join([f"[{k}]({v})" for k, v in DATA["links"].items()])
    ]
    return "\n".join(lines)

def render_education() -> str:
    out = section("Education")
    for e in DATA["education"]:
        out += f"**{e['school']}**, {e['place']} — *{e['degree']}*  \n"
        out += f"{e['dates']}\n\n"
    return out

def render_experience() -> str:
    out = section("Experience")
    for x in DATA["experience"]:
        out += f"**{x['role']}**, {x['org']}  \n{x['dates']}\n\n"
        out += bullet_list(x["bullets"]) + "\n"
    return out

def render_projects() -> str:
    out = section("Projects")
    for p in DATA["projects"]:
        out += f"- **{p['name']}** — {p['desc']}\n"
    return out + "\n"

def render_skills() -> str:
    out = section("Skills")
    for k, v in DATA["skills"].items():
        out += f"- **{k}:** " + ", ".join(v) + "\n"
    return out + "\n"

def render_languages() -> str:
    out = section("Languages")
    return out + bullet_list(DATA["languages"]) + "\n"

def render_highlights() -> str:
    out = section("Highlights")
    return out + bullet_list(DATA["highlights"]) + "\n"

def render_footer() -> str:
    return f"\n> _“{DATA['quote']}”_\n"

def render_full_markdown() -> str:
    parts = [
        render_profile(),
        render_education(),
        render_experience(),
        render_projects(),
        render_skills(),
        render_languages(),
        render_highlights(),
        render_footer(),
    ]
    return "\n".join(parts).strip() + "\n"

def menu():
    items = {
        "1": ("Show Profile", render_profile),
        "2": ("Show Education", render_education),
        "3": ("Show Experience", render_experience),
        "4": ("Show Projects", render_projects),
        "5": ("Show Skills", render_skills),
        "6": ("Show Languages", render_languages),
        "7": ("Show Highlights", render_highlights),
        "8": ("Export ALL to README.md", None),
        "0": ("Exit", None),
    }
    while True:
        print("\n=== About Elene CLI ===")
        for k, (label, _) in items.items():
            print(f"{k}. {label}")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Bye! Good luck 🤍")
            break
        elif choice == "8":
            md = render_full_markdown()
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(md)
            print("✅ Exported README.md (perfect for your GitHub repo).")
        elif choice in items and items[choice][1]:
            print("\n" + items[choice][1]())
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
