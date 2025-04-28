import pandas as pd
import json
class FewShotPosts:
    def __init__(self, file_path = "data/processed_post.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length )
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(all_tags)
           

    def categorize_length(self, line_count):
        if line_count < 3:
         return "Short"
        elif 3 <= line_count <= 5:
            return "Medium"
        else:
            return "Long"
                        
    def get_tags(self):
        self.unique_tags.append("Other")
        self.unique_tags = list(dict.fromkeys(self.unique_tags))
        return self.unique_tags 
    
    def get_filtered_posts(self, length, tag):
        df_filtered = self.df[
             
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags))
        ]

        return df_filtered.to_dict(orient="records")

         
if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Medium", "English", "AI")
    print(posts)
    pass



        