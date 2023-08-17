# encoding: utf-8
import pdfplumber
import pandas as pd
import re

def content_extract(pdf, n_pages):
    content_raw = ''
    for page in range(n_pages):
        page_binary = pdf.pages[page]
        content_raw += page_binary.extract_text()
    return content_raw

def extract(file_path):
    with pdfplumber.open(file_path) as pdf:
        n_pages = len(pdf.pages)
        content_raw = content_extract(pdf, n_pages)

    sep = '===================================================================================================='
    content_list = content_raw.split(sep)

    samples = content_list[3:]

    reads = []
    ## Início do loop
    for sample in samples:
        try:
            # sample = samples[2] # 3 é branco
            sample_lista = sample.split('\n')
            sample_seq = sample_lista[1].split(' ')[2]
            sample_name = sample_lista[2].split(' ')
            sample_name = ''.join(sample_name[2:sample_name.index('Date')])

            try:
                sample1_idx = [index - 1 for index, item in enumerate(sample_lista[8].split(' ')) if re.match(r'\d{2}:\d{2}:\d{2}', item)][0]
                sample1 = sample_lista[8].split(' ')[sample1_idx]
            except (IndexError, ValueError):
                sample1 = ''

            try:
                sample2_idx = [index - 1 for index, item in enumerate(sample_lista[9].split(' ')) if re.match(r'\d{2}:\d{2}:\d{2}', item)][0]
                sample2 = sample_lista[8].split(' ')[sample2_idx]
            except (IndexError, ValueError):
                sample2 = ''
            # print(f"amostra {sample_seq}: {sample_name}\nleitura 1: {sample1}\nleitura 2: {sample2}")
            reads.append({'#':sample_seq, 'nome':sample_name, 'leitura_1':sample1, 'leitura_2':sample2})
        except (IndexError, ValueError):
            continue

    df = pd.DataFrame(reads)
    return df
    # print(df.to_string())
