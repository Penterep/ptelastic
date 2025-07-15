from ptlibs import ptjsonlib
from ptlibs.ptprinthelper import ptprint

__TESTLABEL__ = "Example module"


class ExampleModule:

    def __init__(self, args: object, ptjsonlib: object, helpers: object, http_client: object, base_response: object) -> None:
        self.args = args
        self.ptjsonlib = ptjsonlib
        self.helpers = helpers
        self.http_client = http_client
        self.base_response = base_response

        self.helpers.print_header(__TESTLABEL__)

    def run(self) -> None:
        ptprint("Info example", "INFO", not self.args.json, colortext=False)
        ptprint("Indented lorem ipsum...", "TEXT", not self.args.json, indent=4)

        self._send_test_request(url="https://example.com/")

    def _send_test_request(self, url: str) -> None:
        """Demo method"""
        ptprint(f"Sending request to: {url}", "TITLE", not self.args.json, colortext=False)
        response = self.http_client.send_request(url, method="GET", headers=self.args.headers, allow_redirects=False)
        ptprint(f"Returned response status: {response.status_code}", "TEXT", not self.args.json, indent=4)

def run(args, ptjsonlib, helpers, http_client, base_response):
    """Entry point for running the CT module (Cipher Test)."""
    ExampleModule(args, ptjsonlib, helpers, http_client, base_response).run()