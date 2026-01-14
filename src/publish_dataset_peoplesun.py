
import os
import pandas as pd
from settings import *
from getpass import getpass
import requests as req


if __name__ == '__main__':

    print(f"Start data publication on OEP")

    apitoken = getpass('OEP API Token:')

    topic = "model_draft"
    publish_in_topic = "demand"

    table_list = extract_filenames(filepath_list)
    print(table_list)

    for table in table_list:
        print(table)
        auth_headers = {"Authorization": "Token %s" % apitoken}
        table_publish_api_url = f"https://openenergyplatform.org/api/v0/schema/{topic}/tables/{table}/move_publish/{publish_in_topic}/"
        table_undo_publish_api_url = f"https://openenergyplatform.org/api/v0/schema/{publish_in_topic}/tables/{table}/move_publish/{topic}/"

        print(table_publish_api_url)
        print(table_undo_publish_api_url)

        embargo = {
            "embargo": {"duration": "none"},
        }

        res = req.post(table_publish_api_url, json = {"query": embargo},
                       headers = auth_headers)

        # raise Exception if request fails
        if not res.ok:
            raise Exception(res.reason )

        print(f"Table {table} successfully published")

    print(f"Data publication on OEP finished")


# Revoke publish (move back)
# res = req.post(table_undo_publish_api_url, headers=auth_headers)
#
# # raise Exception if request fails
# if not res.ok:
#     raise Exception(res.text)