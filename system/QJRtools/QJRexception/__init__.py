
class QJRasCompilingError(Exception):
    """
    An exception to do not tell
    the user about a successful
    compilation.
    """
    pass

class QJRcommandError(Exception):

    """Q-J-R command error."""

class QJRruntimeError(Exception):

    """Q-J-R runtime error."""

class QJRassemblyError(Exception):

    """QJRassembly error."""

class QJRsecurityError(Exception):

    """QJRsecurity error."""
