import tabula
import json
import logging

def get_pdf_table(file_name):
    file_name = file_name.replace('\\', '/')
    logging.basicConfig(filename='c:/tmp/logging.txt', filemode='w', level=logging.INFO)
    logging.info(file_name + '\n\n')

    income_df_list = tabula.read_pdf(file_name, pages='all')
    income_json = income_df_list[0].to_json(orient='records')
    logging.info('JSON: ' + income_json)
    return income_json

def get_random_text(random_text):
    logging.info(random_text)
    return random_text

# local testing
#file_name = "simple_data.pdf"
#income_json = get_pdf_table(file_name)

#print(income_json)