from typing import List
from subprocess import run, PIPE
import re

PIP_INSTALL_NO_VERSION_PATTERN = re.compile(r'([\w\s:=(]+versions: )([\d., ]+)(\)[\\n\w\s:=]+)')


def get_package_latest_version(package: str) -> str:
    versions = get_package_versions(package)
    return versions[-1]


def get_package_versions(package: str) -> List[str]:
    error_version_output = _run_capture_stderr(f'pip install {package}==')
    versions = _versions_from_pip_install_error_output(error_version_output)
    return versions


def _run_capture_stderr(command: str) -> str:
    process = run(command, shell=True, stderr=PIPE, universal_newlines=True)
    output = process.stderr
    return output


def _versions_from_pip_install_error_output(err_output: str) -> List[str]:
    match = PIP_INSTALL_NO_VERSION_PATTERN.match(err_output)
    if not match:
        raise ValueError(f'could not parse output for versions: {err_output}')
    versions_str = match.group(2)
    return versions_str.split(', ')


if __name__ == '__main__':
    import sys
    version = get_package_latest_version(sys.argv[1])
    print(version)
