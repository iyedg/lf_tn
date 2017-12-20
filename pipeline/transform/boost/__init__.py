import re


def transform_rows(work_sheet):
    header_regex = re.compile(r"[A-Z]+\d*\s*")
    # header
    raw_header_row = work_sheet.iter_rows(max_row=1)
    # TODO: better regex, this is hacky
    header_row = [header_regex.search(cell.value).group(
    ).strip() for cell in next(raw_header_row)]
    # rows
    rows = work_sheet.iter_rows(min_row=2)
    while True:
        yield dict(zip(header_row, [cell.value for cell in next(rows)]))
