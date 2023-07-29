import pandas as pd

# define column names
columns = ['Date', 'Purchases', 'Payments/Refunds', 'Description', 'Reference Number']

# read the file
with open('20230721.txt', 'r') as file:
    data = file.readlines()

# create empty DataFrame
df = pd.DataFrame(columns=columns)

# iterate over each line in data
for line in data:
    line = line.strip()  # remove newline characters
    
    # parse each component based on your description
    split_line = line.split(' ')
    date = split_line[0]  # data before the first whitespace
    ref_num = split_line[1]  # data between the first and second whitespace
    trans_amt = split_line[-1]  # data after the last whitespace
    desc = ' '.join(split_line[2:-1])  # data between the second and the last whitespace

    # check if the transaction amount contains "cr" and separate accordingly
    credits = None
    if "cr" in trans_amt.lower():
        credits = trans_amt.replace("cr", "").replace("CR", "")
        trans_amt = None

    # add to DataFrame
    df = df._append({
        'Date': date,
        'Reference Number': ref_num,
        'Description': desc,
        'Purchases': trans_amt,
        'Payments/Refunds': credits
    }, ignore_index=True)

# save DataFrame to Excel
df.to_excel('20230721.xlsx', index=False)
