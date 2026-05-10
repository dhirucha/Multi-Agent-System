from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def extract_text_content(content):

    # already plain text
    if isinstance(content, str):
        return content

    # structured response
    if isinstance(content, list):

        texts = []

        for item in content:

            if (
                isinstance(item, dict)
                and item.get("type") == "text"
            ):
                texts.append(item.get("text", ""))

        return "\n".join(texts)

    return str(content)

def run_research_pipeline(topic:str) -> dict:
    
    state = {}
    
    #search agent work
    print("\n"+" ="*50)
    print("step 1 - search agent is working ...")
    print("="*50)
    
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
    "messages": [(
        "user",
        f"Find recent, reliable and detailed information about: {topic}"
    )]
})
    
    raw_search_content = search_result['messages'][-1].content

    state["search_results"] = extract_text_content(
    raw_search_content
    )
    
    print("\n search result ",state['search_results'])
    
    
    #step2 reader agent
    print("\n"+" ="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)
    
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    raw_reader_content = reader_result['messages'][-1].content

    state['scraped_content'] = extract_text_content(
    raw_reader_content
)
    
    print("\nscrapped content: \n", state['scraped_content'])
    
    
    #step3 - writer agent
    print("\n"+" ="*50)
    print("step3 - Writer is drafting the report ...")
    print("="*50)
    
    research_combined = (
        f"SEARCH RESULTS : \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
    )
    
    state["report"] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })
    
    print("\n Final Reports\n", state['report'])
    
    
    #critic prompt
    print("\n"+" ="*50)
    print("step4 - critic is reviewing the report ...")
    print("="*50)
    
    
    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })
    
    print("\n critic report \n", state['feedback'])
    
    
    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic: ")
    run_research_pipeline(topic)