# AI-Powered Nutritional Regimen Generation System

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-yes-blue?logo=docker)](https://www.docker.com/)

## Description
AI-Powered system that generates **personalized nutritional plans** based on patient data. Optimizes diets using AI algorithms and provides PDF reports for easy access.

## Features
- Personalized diet plan generation
- PDF export of meal plans
- SQL-based data storage
- Dockerized for easy deployment

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
## Usage
python api/app/main.py
