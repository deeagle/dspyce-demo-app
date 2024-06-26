import argparse
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


def access_demo_api_and_print_statistics() -> None:
    print("Demo implementation of a dspyce library")
    url = "https://demo.dspace.org/server/api"
    api_endpoint = get_rest_api_connection(url)
    print_statistics(api_endpoint)
    print("Demo successfully finished")


def print_app_description() -> None:
    print("Demo implementation of a dspyce library")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--desc', action='store_true', help='Request common description')
    args = parser.parse_args()

    if args.desc:
        print_app_description()
    else:
        access_demo_api_and_print_statistics()
