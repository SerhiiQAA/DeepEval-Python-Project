import requests
from deepeval.models import DeepEvalBaseLLM
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval import assert_test

class LocalLLM(DeepEvalBaseLLM):
    def __init__(self, base_url="http://127.0.0.1:1234", model="meta-llama-3.1-8b-instruct"):
        self.base_url = base_url
        self.model = model

    def get_model_name(self):
        return self.model
    
    def load_model(self) -> None:
        pass
    
    def generate(self, prompt: str):
        response = requests.post(
            f'{self.base_url}/v1/chat/completions',
            json={
                "messages": [{"role": "user", "content": prompt}],
                "model": self.model,
                "temperature": 0.7,
                "max_tokens": 100
            }
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"Raw response from LM Studio: {data}")  
            return data["choices"][0]["message"]["content"]
        else:
            print(f"Error: HTTP {response.status_code} - {response.text}")
            return "Error"
    
    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

local_llm = LocalLLM()

answer_relevancy_metric = AnswerRelevancyMetric(
    threshold=0.5,
    model=local_llm,
    include_reason=True
)

def test_capital_of_france():
    print("Generating actual_output for test case...")
    
    input_1 = "What is the capital of France?"
    actual_output_1 = local_llm.generate(input_1)
    print(f"Generated output for '{input_1}': {actual_output_1[:50]}...")
    
    test_case_1 = LLMTestCase(
        input=input_1,
        actual_output=actual_output_1,
        expected_output="Paris is the capital of France."
    )

    assert_test(test_case=test_case_1, metrics=[answer_relevancy_metric])