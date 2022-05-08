import itertools
from pathlib import Path

import click

from cosmoshield import get_blacklisted_domains


ASSET_DIR = 'assets'
OUTPUT_FILE = 'umatrix-rules.txt'
OUTPUT_MIN_FILE = 'umatrix-rules.min.txt'


def generate_lines_for_domain(entry, minimal: bool = False):
    """Generates a comment/config/spacer line for each blacklisted domain

    Entry is an entry as described by the Interbloc API. Expected fields are
    domain, date, and reason. Domain is the only field required to generate
    a valid entry.
    """
    domain = entry.get('domain', None)
    if domain:

        if not minimal:
            date = entry.get('date', None)
            reason = entry.get('reason', None)

            comment_line = [f'# {domain}:']
            if date:
                comment_line.append(f'{date}')
            if reason:
                comment_line.append(f'{reason}')

            yield ' '.join(comment_line)

        yield f'* {domain} * block'

        if not minimal:
            yield ''


@click.command
@click.option(
    '--minimal',
    required=False,
    default=False,
    is_flag=True,
    help=(
        'Flag indicating whether non config lines for each domain should be '
        'included in the output. Defaults to False.'
    ),
)
def main(minimal: bool):
    lines = []
    blacklist = get_blacklisted_domains()
    for entry in blacklist.values():
        lines.extend(generate_lines_for_domain(entry, minimal))

    output_path = Path(ASSET_DIR) / (
        OUTPUT_MIN_FILE if minimal else OUTPUT_FILE
    )
    with open(output_path, 'wt') as output:
        output.writelines('\n'.join(lines))


if __name__ == '__main__':
    main()
