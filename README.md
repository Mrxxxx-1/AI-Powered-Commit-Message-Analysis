# AI-Powered Commit Message Analysis

## 1. Overview

This project provides a tool for analyzing Git commit messages using the power of Large Language Models (LLMs) like GPT. It automatically categorizes commits, summarizes changes, and extracts key information from commit histories. By applying natural language understanding to development workflows, this tool helps teams gain deeper insights into their project's evolution, identify trends, and improve their commit practices without manual effort.

The primary goal is to transform unstructured commit logs into structured, actionable data.

## 2. How It Works

The system operates by processing a repository's Git history and leveraging an LLM for analysis.

### a. Data Extraction
The tool first clones a target Git repository and extracts the commit history. For each commit, it gathers the author, date, and the full commit message.

### b. LLM-Powered Analysis
Each commit message is sent to a GPT-based model via an API. A carefully crafted prompt instructs the model to perform several tasks:
* **Categorization:** Classify the commit into predefined categories (e.g., `feature`, `bugfix`, `refactor`, `docs`, `test`, `chore`).
* **Summarization:** Generate a concise, one-sentence summary of the changes described in the commit.
* **Keyword Extraction:** Identify the most relevant keywords or technologies mentioned.

### c. Output Generation
The results of the analysis are compiled into a structured format, such as a CSV or JSON file. This file provides a clear, organized view of the repository's history, ready for further data analysis, visualization, or reporting.

[Image or diagram showing the workflow: Git Repo -> Data Extraction -> LLM API -> Structured Data (CSV/JSON)]

## 3. Key Features

* **Automated Commit Categorization:** Automatically assigns a category to each commit message.
* **AI-Generated Summaries:** Creates human-readable summaries for complex commit messages.
* **Insightful Analytics:** Enables trend analysis by providing structured data on development activities.
* **Extensible and Configurable:** Easily adaptable to different LLM providers and customizable analysis prompts.
* **Language Agnostic:** Works with any programming language, as it analyzes the natural language of the commit messages.

## 4. How to Use

### Prerequisites
* Python 3.x
* An API key for an LLM provider (e.g., OpenAI)

### Installation
1.  Clone this repository:
    ```bash
    git clone [URL_of_this_repo]
    cd [repo_directory]
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Set up your API key as an environment variable:
    ```bash
    export OPENAI_API_KEY='your_api_key_here'
    ```

### Execution
Run the main script from your terminal, providing the URL of the Git repository you want to analyze and specifying an output file.

```bash
python analyze_commits.py --repo_url [https://github.com/user/repository.git](https://github.com/user/repository.git) --output results.csv
