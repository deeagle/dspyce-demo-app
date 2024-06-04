import dspyce
import json


def get_rest_api_connection(endpoint_url: str) -> dspyce.rest.RestAPI:
    print("> Create RestApi connection")
    return dspyce.rest.RestAPI(endpoint_url, log_level="ERROR")


def print_statistics(api_endpoint: dspyce.rest.RestAPI, human_readable=True) -> None:
    print("> Print endpoint::statistics")
    stats = api_endpoint.get_api("/statistics")
    if human_readable:
        stats = json.dumps(stats, indent=2)
    print(stats)


if __name__ == "__main__":
    print("Demo implementation of a dspyce library")
    url = "https://demo.dspace.org/server/api"
    apiEndpoint = get_rest_api_connection(url)
    print_statistics(apiEndpoint)
    print("Demo successfully finished")
