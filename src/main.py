from dotenv import load_dotenv
import os
def print_author():
    load_dotenv(dotenv_path=r'C:\Users\Wh1teCoder\Desktop\DataScience\Python\GitHub_practice\my_project')
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")
print_author()
