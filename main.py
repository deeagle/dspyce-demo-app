import dspyce
import json


def getRestApiConnection(url: str):
    print("> Create RestApi connection")
    return dspyce.rest.RestAPI(url, log_level="ERROR")


def printStats(apiEndpoint, human_readable=True):
    print("> Print endpoint::statistics")
    stats = apiEndpoint.get_api("/statistics")
    if human_readable:
        stats = json.dumps(stats, indent=2)
    print(stats)


if __name__ == "__main__":
    print("Demo implementation of a dspyce library")
    url = "https://demo.dspace.org/server/api"
    apiEndpoint = getRestApiConnection(url)
    printStats(apiEndpoint)
    print("Demo successfully finished")
