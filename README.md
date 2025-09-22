---------
## Table of contents

* Project Overview

* User Experience Features

* Core Functionality

* Technical Implementation

* Deployment Guide

* Acknowledgements
-----------

## Utamaduni Archives: Safeguarding Kenya's Tribal Heritage


The Utamaduni Archives is a digital platform that empowers Kenyan communities to preserve, manage, and share their cultural heritage—like stories, songs, and traditions—on their own terms. Instead of storing the content itself, it acts as a "digital library card" system, cataloging information about each cultural artifact and linking to where the community chooses to host it. Most importantly, it allows communities to set their own rules for who can access their culture and how it can be used.

Who It Is For

Kenyan Communities & Elders: The primary users.
It gives them the tools to digitally safeguard their legacy and control their narrative.

Cultural Rights Advocates & Researchers: Provides a trusted, ethical source for accessing authentic cultural materials with clear permissions.

The Kenyan Diaspora & Global Audience: Offers a legitimate window into authentic Kenyan heritage, ensuring they are connecting with and learning from the source.

Content Creators & Institutions: (e.g., filmmakers, museums, schools) Allows them to ethically source and license cultural content by connecting directly with the rightsholders.

## Color reference

:root {
  /* Primary Palette */
  --color-primary: #AA6C39;
  --color-primary-dark: #2A5A3C;
  --color-background: #E7D3B1;
  
  /* Accent Palette */
  --color-accent-red: #C2492D;
  --color-accent-gold: #E3A32D;
  --color-accent-blue: #4A7C8B;
  
  /* Neutral Palette */
  --color-text: #333333;
  --color-text-light: #666666;
  --color-border: #DDDDDD;
  --color-bg-alt: #F8F9FA;
  
  /* Semantic Colors */
  --color-success: var(--color-primary-dark);
  --color-error: var(--color-accent-red);
  --color-warning: var(--color-accent-gold);
  --color-info: var(--color-accent-blue);
}

/* Example usage */
body {
  background-color: var(--color-background);
  color: var(--color-text);
}

.stButton > button {
  background-color: var(--color-primary);
  color: white;
}

.stAlert {
  /* Streamlit's alert boxes can be targeted and customized with these variables */
}
## Deployment

Utamaduni Archives - Deployment Guide

This guide outlines the process to deploy the application to Streamlit Community Cloud, making it publicly accessible.

Prerequisites
Code Repository: github.com/your-username/utamaduni-archives).

Streamlit Account:

requirements.txt File: Ensure your project has a requirements.txt file listing all Python dependencies.

Step-by-Step Deployment Instructions
1. Preparation

text
utamaduni-archives/

    ├── app.py                 # Main application file
        ├── requirements.txt       # Python dependencies
        ├── data/                  # Your JSON data directory
        ├── utils/                 # Helper modules
        ├── pages/                 # Streamlit pages
        └── assets/                # Static files (CSS, images)

2. Requirements.txt File
This file tells Streamlit what Python packages to install. It should contain:

txt

streamlit
pandas

3. Streamlit Community Cloud(https://share.streamlit.io/)

GitHub repository (VorCollective/utamaduni-archives).

Branch: main or master.

Main file path: /app.py

App URL: tamadunizetu-kenya.

## Acknowledgements

The Utamaduni Archives project is a collective effort that stands on the shoulders of many individuals and institutions. We extend our deepest gratitude to all who have contributed to its vision and development.

First and Foremost, to the Communities of Kenya:
We acknowledge that this project is nothing without the wisdom, stories, and cultural wealth of Kenya's diverse tribal communities. Our profound respect and gratitude go to the elders, storytellers, artists, and knowledge keepers who are the true authors of this archive. Thank you for your trust and for sharing your invaluable heritage with future generations.

Project Advisors & Cultural Consultants:
We are deeply grateful to the historians, anthropologists, and cultural experts who provided essential guidance to ensure this platform is respectful, accurate, and ethically sound. Your insights were crucial in designing a system that truly serves community interests.

The Open-Source Community:
This project was built using powerful, free tools provided by the open-source community. We specifically thank:

The Streamlit team for creating an accessible framework that makes deploying web apps possible for developers of all levels.

The Python community for the versatile and robust language that forms the backbone of this application.

The countless maintainers of the libraries and dependencies that make modern software development possible.

Institutional Support:
We acknowledge the alignment of this project with the Kenyan government's Bottom-Up Economic Transformation Agenda (BETA), which highlights the critical importance of community-led initiatives and cultural empowerment. This framework provides a vital national context for our work.

Development & Testing Team:
Thank you to the developers, designers, and beta testers who donated their time, skills, and passion to build, refine, and test the platform. Your commitment to a user-friendly and robust experience is evident in every feature.

Personal Dedication:
This project is dedicated to the past, present, and future generations of Kenya. May it serve as a digital fortress for our cultures, ensuring that the songs of the past are never silenced and the stories of our elders continue to teach and inspire.

Asante Sana.
## User Experience Features

🌙 Light/Dark Mode Toggle
Simple toggle switch in header/navigation

Automatic system detection (follows device settings)

Persistent preference (remembers your choice)

Accessibility optimized (good contrast in both modes)

👀 Live Previews
Content previews when hovering over artifacts

Real-time form validation as you type

Media previews for audio/video before opening

Submission preview before final posting

📺 Fullscreen Mode
One-click fullscreen for media content (videos, images)

Focus mode for reading stories without distractions

Presentation mode for educational use

Easy exit with ESC key or close button

📱 Cross-Platform
Mobile-responsive (works on phones, tablets, desktop)

Progressive Web App (can "install" on mobile homescreen)

Touch-friendly buttons and navigation

Offline capability for basic browsing

Consistent experience across all devices



## Core Functionality
Core Features (Currently Implemented)
1. Digital Library Catalog System
Browse Archive: Search and filter cultural artifacts by tribe, type, language, region

Artifact Metadata Storage: Stores information about cultural items (not the items themselves)

External Content Linking: Points to where communities host their actual content (YouTube, etc.)

2. Community Control & Permissions
Community Portals: Dedicated dashboards for each tribe/community

Custom Permission Settings: Communities set usage rules (educational use, request permission, etc.)

Content Submission Wizard: Guided process for adding new cultural materials

3. Cultural Preservation Tools
Structured Data Organization: Consistent metadata (tribe, storyteller, type, context)

Context Preservation: Saves the story behind each artifact, not just the artifact itself

JSON-based Storage: Simple, portable data format that's easy to backup

4. Access & Discovery
Multi-page Interface: Organized sections for browsing, submitting, learning

Advanced Search: Filter by multiple criteria for researchers and users

Responsive Design: Works on desktop and mobile devices

5. Basic User Management
Different User Types: Community admins, researchers, general public

Permission-based Access: Different views based on user role

Contact System: Direct communication for permission requests

Technical Features
Streamlit-based Web Interface: Free, beautiful, and accessible

JSON Database: No complex database required

Free Deployment: Hosted on Streamlit Community Cloud

Simple Backup: Data can be saved to USB, email, or print

Key Differentiating Features
Community-Owned: Communities keep copyright and control

Metadata-Focused: Stores information about content, not content itself

Economic Empowerment: Creates pathways for ethical cultural commerce

Bottom-Up Approach: Aligns with Kenya's community-led development model


