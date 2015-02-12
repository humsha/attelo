"""
attelo subcommands
"""

# Author: Eric Kow
# License: CeCILL-B (French BSD3)

# pylint: disable=import-self
from . import\
    (decode,
     enfold,
     evaluate,
     graph,
     rewrite,
     learn,
     tmp,
     report)

SUBCOMMANDS = [learn,
               decode,
               enfold,
               evaluate,
               graph,
               rewrite,
               tmp,
               report]
