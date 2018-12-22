import re
from claim import Claim

_CLAIM_ID = "claim_id"
_LEFT = "inches_from_left"
_TOP = "inches_from_top"
_WIDTH = "width"
_HEIGHT = "height"


class ClaimParser:

    def __init__(self):
        self._regex = re.compile(
            "#(?P<claim_id>[0-9]+) @ " +
            "(?P<inches_from_left>[0-9]+),(?P<inches_from_top>[0-9]+): (?P<width>[0-9]+)x(?P<height>[0-9]+)")

    def parse(self, claim_string):
        if claim_string:
            match = self._regex.match(claim_string)

            if match:
                claim = Claim()
                claim.claim_id = match[_CLAIM_ID]
                claim.inches_from_left_edge = int(match[_LEFT])
                claim.inches_from_top_edge = int(match[_TOP])
                claim.width = int(match[_WIDTH])
                claim.height = int(match[_HEIGHT])

                return claim

        return None
