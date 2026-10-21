#!/usr/bin/env python3
"""Compile a PO catalog to MO without rejecting legacy printf mismatches.

CDDA's 0.I Chinese catalog contains a small number of historical format
placeholder mismatches.  GNU msgfmt accepts the catalog unless format checks
are explicitly requested, whereas Babel's CLI always runs Catalog.check().
Use Babel's parser/writer directly to retain msgfmt-compatible behaviour.
"""

import argparse

from babel.messages.mofile import write_mo
from babel.messages.pofile import read_po


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    args = parser.parse_args()

    with open(args.input, "rb") as po_file:
        catalog = read_po(po_file, locale=None, ignore_obsolete=True)
    with open(args.output, "wb") as mo_file:
        write_mo(mo_file, catalog, use_fuzzy=True)


if __name__ == "__main__":
    main()
