# AI-Powered Nutritional Regimen Generation System

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-yes-blue?logo=docker)](https://www.docker.com/)

## Description
Development of an **AI-Powered Nutritional Regimen**. Integrated OpenAI API for intelligent meal recommendations, automated workflow orchestration using n8n, and backend services designed with FastAPI connected to PostgreSQL. Includes data preprocessing, model testing, and seamless API responses for PDF report generation.

## Features
- Personalized meal plan generation using AI
- Workflow automation with n8n
- FastAPI backend connected to PostgreSQL
- PDF export of generated diets

## Installation
```bash
git clone https://github.com/zeineb22/ai-powered-nutritional-regimen-generator.git
cd ai-powered-nutritional-regimen-generator
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / MacOS
source venv/bin/activate
pip install -r requirements.txt
--> python api/app/main.py
