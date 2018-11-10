from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    __version__ = 'unknown'

from .ext import html_page_context


def setup(app):
    app.add_config_value('og_site_url', None, 'html')
    app.add_config_value('og_twitter_site', None, 'html')
    app.connect('html-page-context', html_page_context)
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
