import os
from ctransformers import AutoModelForCausalLM


class Translator:
    """
    Lightweight local LLM-based translator.
    CPU-only inference using quantized GGUF model.
    """

    def __init__(self, model_path):
        if not os.path.exists(model_path):
            raise FileNotFoundError("LLM model file not found.")

        model_dir = os.path.dirname(model_path)
        model_file = os.path.basename(model_path)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_dir,
            model_file=model_file,
            model_type="llama",
            gpu_layers=0
        )

    def translate(self, text, target_language="Hindi"):
        prompt = (
            f"You are a translator.\n"
            f"Translate the following English sentence into pure {target_language}.\n"
            f"Do NOT explain.\n"
            f"Do NOT paraphrase.\n"
            f"Only output the translated sentence.\n\n"
            f"Sentence: {text}\n"
            f"Translation:"
        )

        response = self.model(prompt, max_new_tokens=128)
        return response.strip()

