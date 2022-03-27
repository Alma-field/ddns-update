from .awhc import get_ip as awhc
from .wafc import get_ip as wafc

__all__ = ['awhc', 'wafc']

ALL = [awhc, wafc]
