from feedly.feeds.aggregated_feed import CassandraAggregatedFeed
from feedly.tests.feeds.aggregated_feed.base import TestAggregatedFeed


class TestCassandraAggregatedFeed(TestAggregatedFeed):
    feed_cls = CassandraAggregatedFeed