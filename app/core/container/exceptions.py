class ContainerError(Exception):
    """
    Base exception for the dependency injection container.
    """

    pass


class DependencyAlreadyRegisteredError(ContainerError):
    """
    Raised when attempting to register a service twice.
    """

    pass


class DependencyNotRegisteredError(ContainerError):
    """
    Raised when a dependency cannot be resolved.
    """

    pass