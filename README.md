# **AI-Powered Text Completion using Cohere**

## **Project Overview**
This project demonstrates the use of **Cohere's Generative AI** to complete text based on user prompts. The application allows users to interact with an AI model that generates relevant and coherent responses. Users can fine-tune the model's behavior by adjusting key parameters such as **temperature** (creativity) and **max_tokens** (response length).

## **Features**
- Accepts **multiple prompts** in a single session.
- Supports **user-controlled model parameters** for customization.
- Implements **error handling** to prevent crashes.
- Enables **AI-generated responses** for diverse text completion tasks.

## **Setup Instructions**
### **Prerequisites**
Ensure you have Python installed on your machine. You can check by running:
```bash
python --version
```

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ai-text-completion-project.git
cd ai-text-completion-project
```

### **Step 2: Install Dependencies**
Install the required Python library:
```bash
pip install cohere
```

### **Step 3: Set Up Your API Key**
To ensure security, store your **Cohere API key** as an environment variable.

#### **Windows (PowerShell)**
```powershell
$env:COHERE_API_KEY="your_api_key_here"
```
#### **Mac/Linux (Terminal)**
```bash
export COHERE_API_KEY="your_api_key_here"
```

You can verify it's stored correctly by running:
```bash
echo $COHERE_API_KEY
```

### **Step 4: Run the Application**
Once everything is set up, execute the script:
```bash
python text_completion_app.py
```
Enter a prompt when asked, and the AI will generate a relevant response.

## **Usage Examples**
Try out different prompts:
- `"Explain photosynthesis in simple terms."`
- `"Write a short story about an astronaut."`
- `"Generate a haiku about nature."`

## **Adjusting Model Parameters**
Modify the `temperature` or `max_tokens` values in the script to customize AI behavior:
```python
response = co.generate(
    model="command",
    prompt=prompt,
    max_tokens=800,
    temperature=0.7
)
```
- Lower **temperature** (`0.3`) → More structured responses.
- Higher **temperature** (`1.0`) → More creative responses.
- Lower **max_tokens** (`600`) → Shorter responses.
- Higher **max_tokens** (`1200`) → More detailed responses.

## **Troubleshooting**
### **Invalid API Key Error**
- Ensure your API key is **correctly set** in the environment.
- If the issue persists, regenerate your key from [Cohere's dashboard](https://dashboard.cohere.com/).

### **Empty or Unexpected AI Response**
- Try using a **different prompt** or adjusting the **temperature**.
- Lower temperature values (`0.3`) provide **precise answers**, while higher ones (`0.9`) **increase variety**.

## **Future Enhancements**
- **Allow users to adjust parameters dynamically** via input prompts.
- **Integrate fact-checking mechanisms** for improved accuracy.
- **Enhance the user interface** for better accessibility.

## **Project Contributors**
- **Author:** Chris Malit
- **GitHub:** (https://github.com/YOUR_GITHUB_USERNAME](https://github.com/malitc902)
- **Date:** June 2025  

## **License**
This project is released under the **MIT License**. Feel free to modify and contribute.

---

This README is **clear, well-structured, and easy to follow**. Let me know if you’d like to customize any sections further.

