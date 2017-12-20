import re

import bonobo
from pipeline import extract, transform

graph = bonobo.Graph(
    extract.boost.extract_excel,
    transform.boost.transform_rows,
    # TODO: replace separator with comma
    bonobo.CsvWriter("out.csv", ioformat="arg0")
)


if __name__ == '__main__':
    from bonobo.commands.run import get_default_services
    bonobo.run(graph, services=get_default_services(__file__))
