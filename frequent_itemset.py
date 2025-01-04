from mrjob.job import MRJob
from mrjob.step import MRStep
from itertools import combinations

class FrequentItemSet(MRJob):

    def configure_args(self):
        super(FrequentItemSet, self).configure_args()
        self.add_passthru_arg('--min-support', type=float, default=0.5, help='Minimum support threshold')
        self.add_passthru_arg('--k', type=int, default=2, help='Size of itemsets to analyze (e.g., 2 for pairs)')

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_items,
                   reducer=self.reducer_count_items),
            MRStep(mapper=self.mapper_find_frequent,
                   reducer=self.reducer_output_frequent)
        ]

    def mapper_get_items(self, _, line):
        items = line.strip().split(',')
        for combination in combinations(items, self.options.k):
            yield tuple(sorted(combination)), 1

    def reducer_count_items(self, itemset, counts):
        total_count = sum(counts)
        yield itemset, total_count

    def mapper_find_frequent(self, itemset, count):
        if count >= self.options.min_support:
            yield None, (itemset, count)

    def reducer_output_frequent(self, _, itemsets):
        for itemset, count in itemsets:
            yield itemset, count


if __name__ == '__main__':
    FrequentItemSet.run()