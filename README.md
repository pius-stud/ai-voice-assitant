# ai-voice-assitant
This repo contains code useful to create a base AI-voice-assitant employing open-source LLMs to run on your local machine.

The Repo contains 4 files (Please, follow this order in your )
- `ai_assistant_libraries.yaml` : is an Anaconda enviroment where all the python libraries needed are.
- `PyAudio-0.2.11-cp310-cp310-win_amd64.whl` : you might have some issues in getting access to your microphone if you're using a Mac. Installing this should sort everything.
- `assistant.py` : defines the python functions you need for speech recognition (then it will be imported in the python notebook below).
- `AI_voice_Assistant.ipynb` : This is the python notebook where you can set a quantized LLM and use your voice to talk wiith AI.

## NOTES
Using a Macbook Air M1 has given me good results, maybe sometimes, for complex questions you may wait longer and it could be tedious. If you have better pc, you will not have these problems.

### LLMs tested - Quantized Version
- mistral-7b-instruct-v0.2.Q3_K_S.gguf (from: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF).
- llama-2-7b-chat.Q2_K.gguf (from: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF).
