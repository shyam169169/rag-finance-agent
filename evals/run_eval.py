import json
from app.api.dependencies import retrieval_service

def evlauate():
    with open("evals/dataset.json", "r") as f:
        dataset = json.load(f)

    results = []

    for item in dataset:
        question = item["question"]
        expected_keywords = item["expected_keywords"]

        response = retrieval_service.query(question)

        answer = response["answer"]
        retrieved_chunks = response["retrieved_chunks"]

        #answer_hit
        answer_hit = any(keyword in answer.lower() for keyword in expected_keywords)

        #retrieval_hit
        retrieval_hit = any(
            any(keyword in chunk.lower() for keyword in expected_keywords)
            for chunk in retrieved_chunks
        )
        results.append({
            "question": question,
            "retrieval_hit":retrieval_hit,
            "answer_hit":answer_hit
        })
    
    retrieval_accuracy = sum( result["retrieval_hit"] for result in results)/ len(results)
    answer_accuracy = sum( result["answer_hit"] for result in results)/ len(results)

    summary = {
        "retrieval_accuracy": retrieval_accuracy,
        "answer_accuracy": answer_accuracy,
        "total_samples": len(results)
    }

    print("=== EVAL RESULTS ===")
    print(summary)

    with open("evals/results.json", "w") as f:
        json.dump({"summary": summary, "details": results}, f, indent=2)
    

if __name__ == "__main__":
    evlauate()