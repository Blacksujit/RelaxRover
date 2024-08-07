# Stress and Anxiety Relief Bot

## Overview

**CalmCraft** 

is a chatbot designed to provide stress and anxiety relief through conversational interactions. It utilizes the latest natural language processing (NLP) models to offer supportive and calming responses to users seeking help.


# Folder Structure:

```
project_root/
│
├── frontend/
│   ├── index.html
│   ├── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── script.js
│
├── backend/
|   |   models/
|   |   chatgpt_model.py
|   |   llama_model.py
│   ├── app.py
│   └── bot_logic.py
│
└── venv/ (your virtual environment)
|___   .env

```

## Features

- **Conversational Support:** Engage in conversations focused on stress relief and mental well-being.
- **AI-Powered Responses:** Leverage advanced NLP models for insightful and empathetic replies.
- **User-Friendly Interface:** A simple web interface for easy interaction with the bot.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites

- Python 3.8+
- Pip (Python package manager)
- A valid OpenAI API key

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/calmcraft.git
   ```

2. **Create a virtual environment and activate it:**


```
python -m venv venv
```

```
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages:**

```
pip install -r requirements.txt

```

4. **Set up environment variables:**

Create a `.env ` file in the root directory and add your OpenAI API key:

 
`OPEN_AI_API_KEY` = 'your_open_ai_api_key'

`LOGIN_KEY` = 'your_login_token_from_hugging_face'


5. **Start the Flask server:**

```
python backend/app.py

```

# **Contributing**:

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or fixes. For major changes, please open an issue to discuss your ideas first.

Fork the repository.

Create a new branch `(git checkout -b feature-branch).`

Commit your changes `(git commit -am 'Add new feature').`

Push to the branch` (git push origin feature-branch).`

Create a new Pull Request.


# **License**:
This project is licensed under the MIT License. See the LICENSE file for details.

# **Contact**:

For any inquiries or issues, please reach out to:

Author: Sujit Nirmal
Email: nirmalsujit981@gmail.com
GitHub: @Blacksujit