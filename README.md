## Local AI Chatbot with Llama3, Ollama & Streamlit

This repository contains the code for a simple web application built with [Streamlit](https://streamlit.io/), which uses Ollama to run the Llama 3 model for generating AI responses in a chat-like interface.

### Prerequisites
1. Python 3.8 or above

### App Demo

![download](https://github.com/user-attachments/assets/4fba519c-bd4c-472c-8806-20c8d296622b)


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
