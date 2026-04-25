

def calculate_cost(input_tokens: int, output_tokens: int):
    INPUT_TOKENS_COST_PER_1M = 0.15
    OUTPUT_TOKENS_COST_PER_1M = 0.60

    input_cost = round((input_tokens * INPUT_TOKENS_COST_PER_1M)/1000000, 6)
    output_cost = round((output_tokens * OUTPUT_TOKENS_COST_PER_1M)/1000000, 6)

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": input_cost + output_cost
    }