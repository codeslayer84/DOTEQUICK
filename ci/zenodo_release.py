#!/usr/bin/env python3
"""
Publish a GitHub release as a new version of the guide's Zenodo record.

Creates a new version under the existing concept DOI, replaces its files
with the given ones, applies the metadata from .zenodo.json plus the
release version, and publishes it.

Usage: zenodo_release.py VERSION FILE [FILE ...]
Environment: ZENODO_TOKEN (personal access token with deposit:write and
deposit:actions scopes)
"""

import datetime
import json
import os
import pathlib
import sys
import urllib.parse
import urllib.request

ZENODO_API = "https://zenodo.org/api"
# Any record in the guide's version history; the latest version is looked up from it.
KNOWN_RECORD_ID = "23417100"


def request(method, url, data=None, content_type="application/json"):
    headers = {"Authorization": f"Bearer {os.environ['ZENODO_TOKEN']}"}
    if data is not None:
        headers["Content-Type"] = content_type
        if content_type == "application/json":
            data = json.dumps(data).encode()
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
    except urllib.error.HTTPError as error:
        sys.exit(f"{method} {url} failed: {error.code} {error.read().decode()}")
    return json.loads(body) if body else None


def main():
    version, files = sys.argv[1], [pathlib.Path(f) for f in sys.argv[2:]]

    latest = request("GET", f"{ZENODO_API}/records/{KNOWN_RECORD_ID}/versions/latest")
    print(f"Latest published version: {latest['id']} ({latest['metadata'].get('version')})")

    new_version = request(
        "POST", f"{ZENODO_API}/deposit/depositions/{latest['id']}/actions/newversion"
    )
    draft = request("GET", new_version["links"]["latest_draft"])
    print(f"Created draft {draft['id']}")

    # Drop the files carried over from the previous version
    for old_file in draft.get("files", []):
        request("DELETE", old_file["links"]["self"])

    bucket = draft["links"]["bucket"]
    for path in files:
        print(f"Uploading {path.name}")
        request(
            "PUT",
            f"{bucket}/{urllib.parse.quote(path.name)}",
            data=path.read_bytes(),
            content_type="application/octet-stream",
        )

    metadata = json.loads(pathlib.Path(".zenodo.json").read_text())
    metadata["version"] = version
    metadata["publication_date"] = datetime.date.today().isoformat()
    request("PUT", draft["links"]["self"], data={"metadata": metadata})

    published = request("POST", draft["links"]["publish"])
    print(f"Published {version}: https://doi.org/{published['doi']}")
    print(f"Concept DOI: https://doi.org/{published['conceptdoi']}")


if __name__ == "__main__":
    main()
