import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    about = """I'm a Master's student in Computer Science at Northeastern University, focused on building scalable, intelligent software systems. I am drawn to the question of how intelligent systems break — and how we can build them better. My work spans full-stack engineering and agentic AI orchestration — from building ERP platforms for state government initiatives to developing AI-powered triage.

        I enjoy the problem-solving layer beneath the surface — designing efficient algorithms, thinking through system architecture, and understanding the failure points that emerge at scale. I'm currently exploring the security side of agentic AI through OpenClaw, a research project analyzing skill-level attack surfaces in AI agent frameworks."""

    return render_template(
        "index.html",
        title="MLH Fellow",
        url=os.getenv("URL"),
        about=about,
        
    )
