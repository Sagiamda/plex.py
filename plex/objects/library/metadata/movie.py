from plex.objects.core.base import Property
from plex.objects.library.extra.genre import Genre
from plex.objects.library.metadata.base import Metadata
from plex.objects.library.video import Video
from plex.objects.mixins.rate import RateMixin
from plex.objects.mixins.scrobble import ScrobbleMixin


class Movie(Video, Metadata, RateMixin, ScrobbleMixin):
    genres = Property(resolver=lambda: Genre.from_node)

    studio = Property
    content_rating = Property('contentRating')

    year = Property(type=int)
    originally_available_at = Property('originallyAvailableAt')

    tagline = Property
