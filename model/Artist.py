from dataclasses import dataclass, field

@dataclass
class Artist:
    id: int
    name: str
    listBrani: list = field(default_factory=list)
    setPlaylist: set = field(default_factory=set)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, Artist) and self.id == other.id

    def __str__(self):
        return self.name if self.name is not None else str(self.id)

