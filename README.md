AI-Powered DBMS Teaching Assistant using IBM Granite and LangFlow

Project Overview

The AI-Powered DBMS Teaching Assistant is an intelligent educational chatbot designed to help students learn Database Management Systems (DBMS) through interactive conversations. The system leverages IBM watsonx.ai, IBM Granite Models, LangFlow, and Agentic AI to provide personalized explanations, SQL query assistance, and instant doubt resolution.

The chatbot acts as a virtual tutor capable of answering questions related to:

* Database Fundamentals
* ER Modeling
* Relational Algebra
* SQL Queries
* Normalization
* Transactions
* Concurrency Control
* Indexing
* Query Processing
* Database Security

The solution provides 24×7 learning support and enhances the educational experience through conversational AI.

⸻

Problem Statement

Students often struggle to understand complex DBMS concepts and require continuous academic support outside classroom hours. Traditional learning resources are distributed across books, notes, and online materials, making it difficult to obtain instant and personalized assistance.

This project addresses these challenges by providing an AI-powered DBMS Teaching Assistant capable of answering queries, explaining concepts, and supporting self-paced learning.

⸻

Objectives

* Provide instant DBMS doubt resolution.
* Explain DBMS concepts in simple language.
* Assist students with SQL queries.
* Support personalized and interactive learning.
* Enable 24×7 academic assistance.
* Improve student engagement and learning outcomes.

⸻

Technologies Used

IBM Technologies

* IBM watsonx.ai
* IBM Granite Foundation Models
* IBM BoB VS Code Extension

Development Technologies

* LangFlow
* Python
* Flask
* HTML
* CSS
* JavaScript

Deployment Technologies

* ngrok
* Tiiny Host
* GitHub

AI Technologies

* Agentic AI
* Retrieval-Augmented Generation (RAG)

⸻

System Architecture

Student/User

↓

Web Interface (HTML/CSS/JavaScript)

↓

Tiiny Host

↓

Flask Proxy API

↓

ngrok Tunnel

↓

LangFlow Workflow

↓

IBM watsonx.ai

↓

IBM Granite Model

↓

AI Generated Response

↓

Student/User

⸻

Key Features

* AI-powered DBMS Teaching Assistant
* Conversational Question Answering
* SQL Query Assistance
* Personalized Learning Support
* Context-Aware Responses
* Agentic AI Workflow
* Educational Knowledge Retrieval
* Responsive Web Interface
* Public Deployment Support

⸻

Project Components

Frontend

* index.html
* Responsive chatbot user interface

Backend

* proxy.py
* Flask-based API integration layer

AI Workflow

* LangFlow Workflow
* IBM Granite Model Integration

Knowledge Source

* DBMS Notes
* Educational Learning Resources

⸻

Role of Agentic AI

Agentic AI enables the assistant to function as an intelligent virtual tutor rather than a simple chatbot.

The system:

* Understands student intent
* Retrieves relevant educational content
* Maintains conversational context
* Generates personalized explanations
* Assists with SQL and DBMS concepts
* Provides continuous learning support

⸻

IBM BoB Contribution

IBM BoB VS Code Extension was used for:

* Rapid code generation
* Development assistance
* Frontend enhancement
* Backend workflow development
* Project implementation support

Additionally, the existing educational website was enhanced using IBM BoB-assisted development techniques.

Website:

https://nikhilmhala.github.io

⸻

Deployment Steps

Step 1: Create Virtual Environment

python3 -m venv myenv
source myenv/bin/activate

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Start LangFlow

langflow run

Step 4: Start Flask Proxy

python proxy.py

Step 5: Start ngrok

ngrok http 5050

Step 6: Launch Frontend

Open:

index.html

or

python3 -m http.server 8000

⸻

Repository Structure

AI-DBMS-Teaching-Assistant/
│
├── README.md
├── index.html
├── proxy.py
├── requirements.txt
|-- app2.py
│
├── screenshots/
│   ├── langflow_workflow.png
│   ├── website_ui.png

│
├── docs/
│   ├── 
│   ├── Project_Presentation.pptx

│
└── langflow/
    └── dbms_agent_flow.json

⸻

Future Scope

* Voice-Based Learning Assistant
* Multilingual Support
* Student Progress Analytics
* LMS Integration
* Mobile Application Development
* Expansion to Data Structures, Algorithms, Operating Systems, Machine Learning, and Deep Learning

⸻

Developer

Dr. Nikhil Mhala

Assistant Professor
Computer Science & Engineering (AIML)

⸻

Acknowledgement

This project was developed as part of the IBM University Engagement Program using IBM watsonx.ai, IBM Granite Models, LangFlow, and Agentic AI technologies.