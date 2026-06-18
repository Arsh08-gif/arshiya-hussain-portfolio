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

    return render_template(
        "index.html",
        title="MLH Fellow",
        url=os.getenv("URL"),
        about=about,
        work_experiences=work_experiences,
    )
