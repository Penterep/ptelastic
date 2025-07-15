"""
Elasticsearch test to see if authentication is enabled

This module implements a test that checks if an Elasticsearch instance has authentication
enabled by sending a request to the server and checking if we get an HTTP response of 401
"""

import http
from ptlibs import ptjsonlib
from ptlibs.ptprinthelper import ptprint

__TESTLABEL__ = "Elasticsearch authentication test"


class Auth:
    def __init__(self, args: object, ptjsonlib: object, helpers: object, http_client: object, base_response: object) -> None:
        self.args = args
        self.ptjsonlib = ptjsonlib
        self.helpers = helpers
        self.http_client = http_client
        self.base_response = base_response

        self.helpers.print_header(__TESTLABEL__)

    def run(self) -> None:
        url = self.args.url

        response = self.http_client.send_request(url, method="GET", headers=self.args.headers, allow_redirects=False)

        if self.args.verbose:
            ptprint(f"Sending request to: {url}", "INFO", not self.args.json, colortext=False, indent=4)
            ptprint(f"Returned response status: {response.status_code}", "INFO", not self.args.json, indent=4)

        if response.status_code == http.HTTPStatus.UNAUTHORIZED:
            ptprint(f"Authentication is enabled", "VULN", not self.args.json, indent=4)
        elif response.status_code == http.HTTPStatus.OK:
            ptprint(f"Authentication is disabled", "VULN", not self.args.json, indent=4)

def run(args, ptjsonlib, helpers, http_client, base_response):
    """Entry point for running the Auth test"""
    Auth(args, ptjsonlib, helpers, http_client, base_response).run()
