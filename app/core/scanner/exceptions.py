class ScannerError(Exception):
    """
    Base exception for the scanner.
    """

    pass


class PackageNotFoundError(ScannerError):
    """
    Raised when a package cannot be imported.
    """

    pass


class InvalidPackageError(ScannerError):
    """
    Raised when the provided package is invalid.
    """

    pass
