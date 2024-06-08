#!/usr/bin/python3
"""Docstrin"""

DD_SITE = "datadoghq.com"
DD_API_KEY = "<DD_API_KEY>"
DD_APP_KEY = "<DD_APP_KEY>"

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )

    print(response)
