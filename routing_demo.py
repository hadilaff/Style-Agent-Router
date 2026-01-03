def route_query(query):
    """
    Determine if a query requires thinking and/or web access.
    Returns a tuple (thinking, web)
    """
    # Your routing logic here
    thinking = False
    web = False
    
    # Example logic 
    if "why" in query.lower() or "how" in query.lower():
        thinking = True
    
    if "latest" in query.lower() or "current" in query.lower():
        web = True
    
    return thinking, web

def get_system_prompt(thinking, web):
    """
    Return the appropriate system prompt based on routing decision.
    """
    # Your system prompt selection logic here
    if thinking and web:
        return "Thinking + Web prompt"
    elif thinking and not web:
        return "Thinking + No-Web prompt"
    elif not thinking and web:
        return "Non-Thinking + Web prompt"
    else:
        return "Non-Thinking + No-Web prompt"

# Example usage
if __name__ == "__main__":
    query = "What is the latest news about AI?"
    thinking, web = route_query(query)
    system_prompt = get_system_prompt(thinking, web)
    
    print(f"Query: {query}")
    print(f"Thinking: {thinking}, Web: {web}")
    print(f"System Prompt: {system_prompt}")