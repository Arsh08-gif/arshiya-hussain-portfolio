import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    about = """I'm a Master's student in Computer Science at Northeastern University, focused on building scalable, intelligent software systems. I am drawn to the question of how intelligent systems break — and how we can build them better. My work spans full-stack engineering and agentic AI orchestration — from building ERP platforms for state government initiatives to developing AI-powered triage.

        I enjoy the problem-solving layer beneath the surface — designing efficient algorithms, thinking through system architecture, and understanding the failure points that emerge at scale. I'm currently exploring the security side of agentic AI through OpenClaw, a research project analyzing skill-level attack surfaces in AI agent frameworks."""

    work_experiences = [
        {
            "role": "Production Engineering Fellow",
            "company": "MLH Fellowship",
            "duration": "Jun 2026 — Present",
            "type": "Fellowship",
        },
        {
            "role": "Software Engineer Intern",
            "company": "E-Connect Solutions",

            "duration": "Feb 2024 — July 2024",
            "type": "Internship",
            "points": [
                "Developed full stack budget management modules for state government's ERP platform, consolidating fragmented budget workflows across 10+ regional divisions into a unified platform with real-time approval status tracking for stakeholders."
            ],
        },
        {
            "role": "Salesforce Trainee",
            "company": "V2 Solutions",
            
            "duration": "Jan 2025 — June 2025",
            "type": "Internship",
            "points": [
                "Built a booking engine for multi-location healthcare diagnostic centers on Salesforce Community Cloud, leveraging relational data modeling to enable cross-entity data retrieval, centralizing scheduling and eliminating location-wise data silos."
            ],
        },
    ]

    education = [
        {
            "degree": "Master of Science, Computer Science",
            "school": "Northeastern University",
            "location": "Boston, MA",
            "department": "Khoury College of Computer Sciences",
            "duration": "2025 — 2027",
            "status": "In Progress",
            "points": [
                "Exploring agent skill security through OpenClaw malicious skill analysis",
                "MITRE eCTF 2026 Participant",
                "Brainstorm BCI Hackathon 2026 — Runner Up",
            ],
        },
        {
            "degree": "Bachelor of Technology, Information Technology",
            "school": "Manipal University Jaipur",
            "location": "Jaipur, India",
            "department": "Department of Information Technology",
            "duration": "2020 — 2024",
            "status": "Completed",
            "points": [
                "Graduated with First Class Distinction",
                "Internship: E-Connect Solutions (.NET)",
                "Internship: V2 Solutions (Salesforce)",
            ],
        },
    ]

    places = [
        {
            "name": "India",
            "emoji": "🇮🇳",
            "lat": 20.5937,
            "lng": 78.9629,
            "note": "Home 🏠",
        },
        {
            "name": "Boston, USA",
            "emoji": "🇺🇸",
            "lat": 42.3601,
            "lng": -71.0589,
            "note": "Northeastern University",
        },
        {
            "name": "Jaipur, India",
            "emoji": "🏰",
            "lat": 26.9124,
            "lng": 75.7873,
            "note": "Manipal University Jaipur",
        },
        {
            "name": "Vietnam",
            "emoji": "🇻🇳",
            "lat": 14.0583,
            "lng": 108.2772,
            "note": "Visited 🌿",
        },
        {
            "name": "New York, USA",
            "emoji": "🗽",
            "lat": 40.7128,
            "lng": -74.0060,
            "note": "The Big Apple",
        },
        {
            "name": "Dubai, UAE",
            "emoji": "🇦🇪",
            "lat": 25.2048,
            "lng": 55.2708,
            "note": "City of Gold ✨",
        },
        {
            "name": "Abu Dhabi, UAE",
            "emoji": "🕌",
            "lat": 24.4539,
            "lng": 54.3773,
            "note": "Capital of UAE",
        },
        {
            "name": "Spiti Valley, India",
            "emoji": "🏔️",
            "lat": 32.2461,
            "lng": 78.0337,
            "note": "Hidden Himalayan gem",
        },
        {
            "name": "Delhi, India",
            "emoji": "🏛️",
            "lat": 28.6139,
            "lng": 77.2090,
            "note": "Capital of India",
        },
        {
            "name": "Meghalaya, India",
            "emoji": "☁️",
            "lat": 25.4670,
            "lng": 91.3662,
            "note": "Abode of Clouds",
        },
        {
            "name": "Shillong, India",
            "emoji": "🎵",
            "lat": 25.5788,
            "lng": 91.8933,
            "note": "Scotland of the East",
        },
    ]

    return render_template(
        "index.html",
        title="MLH Fellow",
        url=os.getenv("URL"),
        about=about,
        work_experiences=work_experiences,
        education=education,
        places=places,
    )
    
    
@app.route('/hobbies')
def hobbies_page():
    hobbies = [
        {
            "name": "Running",
            "icon": "🏃",
            "description": "Long distance running keeps me grounded. Pushing through the last mile translates directly to how I approach hard problems.",
            "image": "https://images.pexels.com/photos/2524368/pexels-photo-2524368.jpeg?w=400"
        },
        {
            "name": "Reading",
            "icon": "📚",
            "description": "I love getting lost in a good book — fiction, non-fiction, anything that makes me think differently about the world.",
            "image": "https://images.pexels.com/photos/256450/pexels-photo-256450.jpeg?w=400"
        },
        {
            "name": "Doing Art",
            "icon": "🎨",
            "description": "Art makes a quiet appearance in my life every once in a while — a small painting here and there, just for the joy of it.",
            "image": "https://images.pexels.com/photos/1269968/pexels-photo-1269968.jpeg?w=400"
        },
    ]
    return render_template('hobbies.html', hobbies=hobbies)
