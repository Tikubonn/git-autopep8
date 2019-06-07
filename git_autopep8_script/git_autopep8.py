
import re
import subprocess
import argparse
import sys


def get_hash(arguments):
    process = subprocess.run(
        ("git", "rev-parse", "--verify", "HEAD"),
        stderr=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        check=False
    )
    if process.stdout.decode("utf-8"):
        return "HEAD"
    else:
        return "4b825dc642cb6eb9a060e54bf8d69288fbee4904"  # empty hash


def list_modified_python_file(arguments):
    hash = get_hash(arguments)
    process = subprocess.run(
        ("git", "diff-index", "--name-status", "--full-index", hash),
        stdout=subprocess.PIPE,
        check=True
    )
    return re.findall(
        "^[UMA]\s*(.*\.py)$",
        process.stdout.decode("utf-8"),
        re.MULTILINE
    )


def update(arguments):
    for modified in list_modified_python_file(arguments):
        process = subprocess.run(
            ("autopep8", "--in-place", modified) + tuple(arguments.arguments),
            check=True
        )
        process = subprocess.run(
            ("git", "add", modified),
            check=True
        )


def main():
    parser = argparse.ArgumentParser(
        description="apply PEP8 code style to your codes that add to Git."
    )
    parser.add_argument(
        "arguments",
        help="arguments are providen to autopep8.",
        nargs=argparse.REMAINDER
    )
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version="%(prog)s 1.0.0"
    )
    arguments = parser.parse_args()
    # main
    try:
        update(arguments)
    except subprocess.CalledProcessError:
        sys.exit(1)
