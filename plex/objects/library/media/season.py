from plex.objects.base import Property
from plex.objects.library.container import Container
from plex.objects.library.media.show import Show
from plex.objects.library.metadata import Metadata
from plex.objects.library.video import Directory


class Season(Directory, Metadata):
    show = Property(resolver=lambda: Season.construct_show)

    index = Property(type=int)

    banner = Property
    theme = Property

    year = Property(type=int)

    episode_count = Property('leafCount', int)
    viewed_episode_count = Property('viewedLeafCount', int)

    def children(self):
        response = self.request('children')

        return self.parse(response, {
            'MediaContainer': (EpisodeContainer, {
                'Video': {
                    'episode': 'Episode'
                }
            })
        })

    @staticmethod
    def construct_show(client, node):
        attribute_map = {
            'index':     'parentIndex',
            'key':       'parentKey',
            'ratingKey': 'parentRatingKey',

            'title':     'parentTitle',
            'summary':   'parentSummary',
            'thumb':     'parentThumb',

            'theme':     'parentTheme'
        }

        return attribute_map.values(), Show.construct(client, node, attribute_map, child=True)


class EpisodeContainer(Container, Season):
    show = Property(resolver=lambda: EpisodeContainer.construct_show)

    attribute_map = {
        'index':    'parentIndex',
        'title':    'parentTitle',
        'year':     'parentYear',

        '*':        '*'
    }

    @staticmethod
    def construct_show(client, node):
        attribute_map = {
            'title':            'grandparentTitle',

            'studio':           'grandparentStudio',
            'content_rating':   'grandparentContentRating',

            'theme':            'grandparentTheme'
        }

        return attribute_map.values(), Show.construct(client, node, attribute_map, child=True)
