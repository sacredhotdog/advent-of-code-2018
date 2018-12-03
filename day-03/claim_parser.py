import re
from claim import Claim


class ClaimParser:

    def __init__(self):
        self._regex = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

    def parse(self, claim_string):
        if claim_string:
            match = self._regex.match(claim_string)

            if match:
                claim = Claim()
                claim.claim_id = match.group(1)
                claim.inches_from_left_edge = int(match.group(2))
                claim.inches_from_top_edge = int(match.group(3))
                claim.width = int(match.group(4))
                claim.height = int(match.group(5))

                return claim

        return None
