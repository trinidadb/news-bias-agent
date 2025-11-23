# News Bias Analyzer Agent 📰

# WIP!!! 

TODO:
- agentic logic
- logger
- and a LOT of stuff

A bias detection system using LLMs and structured output for analyzing news headlines and descriptions.


## 🏗️ Architecture

```
news-bias-agent/
├── src/
│   ├── schemas.py           # Pydantic models for type-safe outputs
│   ├── prompts.py           # Engineered system prompts
│   ├── biasAnalyzer.py      # Core analysis engine
│   └── dataLoader.py        # Data loading and preprocessing
├── notebooks/
│   └── ....                 # Interactive development & experimentation
├── data/
│   └── News_Category_Dataset_v3.json
├── requirements.txt
├── .env.example             # API keys example
└── README.md
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/news-bias-agent
cd news-bias-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Create .env file
cp .env.example .env

# Add your API key
echo "GOOGLE_API_KEY=your_key_here" >> .env
```

Get your Gemini API key at: https://makersuite.google.com/app/apikey

### 3. Download Dataset

Download the [News Category Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset) from Kaggle and place it in the `data/` directory.

### 4. Run Analysis

For now just jupyter :D 