import sys
import click
from nsut.notice_scraper import print_notices


@click.group()
@click.version_option("0.0.1")
def main():
    """CLI FOR NSUT'S IMS"""
    pass


@main.command()
@click.option('--max', default=5, help='maximum number of notices')
def notice(max_notices):
    """Get Most Recent Notices"""
    print_notices(max_notices)


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("CLI for NSUT'S IMS")
    main()
