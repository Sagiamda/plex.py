from plex.objects.core.base import Property
from plex.objects.directory import Directory
from plex.objects.library.media.album import Album
from plex.objects.library.media.artist import Artist
from plex.objects.library.metadata import Metadata
from plex.objects.mixins.session import SessionMixin


class Track(Directory, Metadata, SessionMixin):
    artist = Property(resolver=lambda: Track.construct_artist)
    album = Property(resolver=lambda: Track.construct_album)

    index = Property(type=int)

    duration = Property(type=int)
    view_offset = Property('viewOffset', type=int)

    @staticmethod
    def construct_artist(client, node):
        attribute_map = {
            'key':          'grandparentKey',
            'ratingKey':    'grandparentRatingKey',

            'title':        'grandparentTitle',

            'thumb':        'grandparentThumb'
        }

        return Artist.construct(client, node, attribute_map, child=True)

    @staticmethod
    def construct_album(client, node):
        attribute_map = {
            'index':        'parentIndex',
            'key':          'parentKey',
            'ratingKey':    'parentRatingKey',

            'title':        'parentTitle',

            'thumb':        'parentThumb'
        }

        return Album.construct(client, node, attribute_map, child=True)
