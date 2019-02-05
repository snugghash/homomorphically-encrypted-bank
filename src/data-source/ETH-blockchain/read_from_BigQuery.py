"""
Scalably (arbitrarily) reads ETH data from Google BigQuery
ETH TPS is 15.

TODO this partial fn as formatter seems computationally inefficient, ironically I did it for the opposite reason.
"""
from google.cloud import bigquery
from pprint import pprint
from datetime import datetime
import timeit



def main():
    start = timeit.default_timer()
    formatted_data = get_data_from_big_query(0, 10**5)
    # Note: 10**6 takes 94 secs. 10**5 takes 12 secs.
    print("10**5 elapsed ", timeit.default_timer() - start)
    with open("../../../var/amount.txt", "w") as outfile:
        outfile.write("\n".join([i['value'] for i in formatted_data]))



def get_data_from_big_query(starting_from_index, number_of_rows):
    """
    Read arbitrary number from BigQuery
    """
    client = bigquery.Client.from_service_account_json(
        'scalable-homom-encryp-c5d5f9e88750.json',
        project='bigquery-public-data')

    reference = client.dataset('ethereum_blockchain')
    dataset = client.get_dataset(reference)
    transactions_table_ref = client.get_table(dataset.table('transactions'))

    schema_subset = [
        col for col in transactions_table_ref.schema
        if col.name in ('from_address', 'to_address', 'block_number', 'block_timestamp', 'value')
    ]
    data = [
        x for x in client.list_rows(
            transactions_table_ref,
            start_index=starting_from_index,
            selected_fields=schema_subset,
            max_results=number_of_rows)
    ]
    formatted_data = batch_reformatter(data)
    return formatted_data



def get_relevant_info_as_dict(row):
    """
    Returns relevant info: inputs, outputs, etc. in dict, a weird Row() format from BigQuery
    """
    # Confirmed this is not a reference, it's deepcopy: https://stackoverflow.com/a/47576546/
    dict_row = dict(row)
    # TODO Fix this weirdness, datetime docs are so flipping arcane
    # dict_row['block_timestamp'] = datetime(dict_row['block_timestamp']).utcnow()
    # Store value in ether, converted from wei (1 wei = 10^-18 ETH)
    dict_row['value'] = str(dict_row['value']/10**18)
    return dict_row



def batch_reformatter(data, reformat_fn=get_relevant_info_as_dict):
    formatted_data = []
    for row in data:
        formatted_data.append(reformat_fn(row))
    return formatted_data



def get_data_from_BigQuery_continuous_stateful(batch_size):
    """
    Microbatch the data to get millions of transactions as a stream of microbatches.
    Stateful, built as a generator that returns the next batch_size every call to next().
    TODO add current ETH blockheight instead of infi loop.
    """
    start_index = 0
    while(True):
        yield get_data_from_big_query(start_index, batch_size)
        start_index += batch_size



if __name__ == "__main__":
    main()
