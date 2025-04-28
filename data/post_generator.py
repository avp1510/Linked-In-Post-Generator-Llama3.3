from llm_helper import llm
from few_shot import FewShotPosts

fs = FewShotPosts()

def get_prompt(length, topic, inp):
    length_str = get_length_str(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    1) Topic: {topic}
    2) Length: {length}
    The script for the generated post should always be English.
    '''
    examples = fs.get_filtered_posts(length,topic)

    if len(examples) >= 0 :
        prompt += "3) Use writing style using following examples : "
        for i, post in enumerate(examples):
             post_text = post["text"]
             prompt += f"\n\n Example {i+1} \n\n {post_text}"
             if i == 1:
                 break
    prompt += f"\n\n Also try to write according to this authors tips as well: \n{inp}"
    return prompt


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long": 
        return "11 to 15 lines"

def generate_post(length, topic, inp):
    prompt = get_prompt(length, topic, inp)
    response = llm.invoke(prompt)
    return response.content
    


if __name__ == "__main__":
    post = generate_post("Short" , "AI")
    print(post)