# AI Chatbot Test Project

This project is a simple implementation of an AI chatbot testing framework using DeepEval and a local language model hosted via LM Studio. The goal is to evaluate the chatbot's responses for relevancy using the `AnswerRelevancyMetric`.

## Features
- Tests a chatbot's response to the question "What is the capital of France?".
- Utilizes the `meta-llama-3.1-8b-instruct` model via LM Studio's API.
- Integrates DeepEval for automated evaluation of chatbot responses.

## Prerequisites
- Python 3.12 or later.
- DeepEval (`pip install -U deepeval`).
- LM Studio with the `meta-llama-3.1-8b-instruct` model installed and running on `http://127.0.0.1:1234`.

## Installation
1. Clone the repository or create a project directory:
   ```bash
   mkdir AI_Test_Project
   cd AI_Test_Project

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -U deepeval requests

4. Start LM Studio and load the meta-llama-3.1-8b-instruct model.

## Usage
1. Run the tests:
    ```bash
    deepeval test run test_chatbot.py

2. Check the output for test results and metrics.

## Contributing
Feel free to suggest improvements or add more test cases!