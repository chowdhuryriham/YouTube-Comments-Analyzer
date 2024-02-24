import pandas as pd

def save_to_excel(processed_comments, output_excel):
    df = pd.DataFrame(processed_comments)
    df.to_excel(output_excel, index=False)
