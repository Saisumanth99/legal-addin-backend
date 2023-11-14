
def get_summarization_prompt(data):
    return f"""
    
    When given a context of legal data, your job is to summarize the data by highlighting the important points in
    given context. You must not only focus on shortening the data, make sure you have the contextual meaning in the data provided to you
    in the returned response. make sure your summary does not exceed 700 words.
    
    data: {data}
    """
