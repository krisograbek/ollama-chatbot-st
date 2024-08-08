## Local AI Chatbot with Llama3, Ollama & Streamlit

This repository contains the code for a simple web application built with [Streamlit](https://streamlit.io/), which uses OpenAI's GPT-3 model for generating AI responses in a chat-like interface.

### Prerequisites
1. Python 3.8 or above

### App Demo
![StreamlitChatbot](https://github.com/krisograbek/streamlit_chatbot_base/assets/48050596/e1c62c71-0b3d-4a3b-9855-e48fc73e402b)


### Steps to run the application
**1. Clone the repository to your local machine:**
```shell
git clone https://github.com/krisograbek/ollama-chatbot-st.git
```

**2. Navigate to the project directory:**
```shell
cd ollama-chatbot-st
```

3. Create a virtual environment and activate it:

On macOS and Linux:
```shell
python3 -m venv myenv
source myenv/bin/activate
```

On Windows:
```shell
python -m venv myenv
.\myenv\Scripts\activate
```

3a. Upgrade pip (optional but recommended)
```shell
pip install --upgrade pip
```

4. Install the necessary Python packages:
```shell
pip install -r requirements.txt
```


5. Run the Streamlit application:
```shell
streamlit run chatbot.py
```

Open a web browser and navigate to http://localhost:8501 to interact with the application.

License
This project is open source, under the terms of the MIT license.

Note: This app makes requests to OpenAI's servers whenever the chat is used. Please be aware of this, especially if you're on a paid plan with OpenAI.
