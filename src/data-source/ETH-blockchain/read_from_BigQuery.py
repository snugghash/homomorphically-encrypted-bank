"""
TODO Actually implement scalable reading, move that for loop over, run a function inside loop or maybe micro batch with 100 or so transactions. ETH TPS is 15.
"""
from google.cloud import bigquery
from pprint import pprint
from datetime import datetime



def main():
    data = get_data_from_big_query(0, 10)
    formatted_data = get_relevant_info_as_dict(data)
    with open("../../../var/amount.txt", "w") as outfile:
        outfile.write("\n".join([i['value'] for i in formatted_data]))






def get_data_from_big_query(starting_from_index, number_of_rows):
    """
    Read arbitrary number from BigQuery, does NOT scale
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
    return [
        x for x in client.list_rows(
            transactions_table_ref,
            start_index=starting_from_index,
            selected_fields=schema_subset,
            max_results=number_of_rows)
    ]



def get_relevant_info_as_dict(results):
    """
    Returns relevant info: inputs, outputs, etc. in dict, given dict
    TODO perhaps make this a fn which only acts on one row, and RF out the rest
    """
    formatted = []
    for row in results:
        dict_row = dict(row)
        # TODO dict_row['block_timestamp'] = datetime(dict_row['block_timestamp']).utcnow()
        dict_row['value'] = str(dict_row['value'])
        formatted.append(dict_row)
    return formatted



def get_data_from_BigQuery_scalable():
    """
    Microbatch the data to get millions of transactions from a stream of microbatches
    """
    pass



if __name__ == "__main__":
    main()
