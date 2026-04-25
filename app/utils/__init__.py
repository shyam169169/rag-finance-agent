

def calculate_cost(input_tokens: int, output_tokens: int):
    INPUT_TOKENS_COST_PER_1M = 0.15
    OUTPUT_TOKENS_COST_PER_1M = 0.60

    input_cost = (input_tokens/1000000) * INPUT_TOKENS_COST_PER_1M
    output_cost = (output_tokens/1000000) * OUTPUT_TOKENS_COST_PER_1M

    return {
        "input_cost":input_cost,
        "output_cost": output_cost,
        "total_cost": input_cost + output_cost
    }