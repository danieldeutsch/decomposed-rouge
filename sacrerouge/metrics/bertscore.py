import argparse
from overrides import overrides
from typing import List

from sacrerouge.commands import MetricSetupSubcommand
from sacrerouge.common.util import flatten
from sacrerouge.data import MetricsDict
from sacrerouge.data.types import ReferenceType, SummaryType
from sacrerouge.metrics import Metric, ReferenceBasedMetric

try:
    import bert_score
except ImportError:
    BERTSCORE_INSTALLED = False

    @Metric.register('bertscore')
    class BertScore(ReferenceBasedMetric):
        def __init__(self, *args, **kwargs):
            pass

        def score_multi_all(self, *args, **kwargs):
            raise NotImplementedError('Please install the "bert_score" python library library to use BertScore')
else:
    BERTSCORE_INSTALLED = True

    @Metric.register('bertscore')
    class BertScore(ReferenceBasedMetric):
        def __init__(self,
                     model_type: str = None,
                     num_layers: int = None,
                     nthreads: int = 4,
                     batch_size: int = 64,
                     lang: str = 'en',
                     verbose: bool = False) -> None:
            super().__init__()
            self.model_type = model_type
            self.num_layers = num_layers
            self.nthreads = nthreads
            self.batch_size = batch_size
            self.lang = lang
            self.verbose = verbose

        def _get_unique_references(self, references_list: List[List[str]]) -> List[str]:
            unique_references = set()
            for references in references_list:
                for reference in references:
                    unique_references.add(reference)
            return list(unique_references)

        def _run(self,
                 summaries_list: List[List[SummaryType]],
                 references_list: List[List[ReferenceType]]) -> List[List[MetricsDict]]:
            summaries_list = [[flatten(summary) for summary in summaries] for summaries in summaries_list]
            references_list = [[flatten(reference) for reference in references] for references in references_list]

            # Create the candidate and reference lists for passing to the scoring function
            input_candidates = []
            input_references = []
            empty_inputs = set()
            for i, (summaries, references) in enumerate(zip(summaries_list, references_list)):
                for j, summary in enumerate(summaries):
                    if len(summary) == 0:
                        empty_inputs.add((i, j))
                    else:
                        input_candidates.append(summary)
                        input_references.append(references)

            # Score the summaries
            precisions, recalls, f1s = bert_score.score(
                input_candidates,
                input_references,
                model_type=self.model_type,
                num_layers=self.num_layers,
                idf=False,
                nthreads=self.nthreads,
                batch_size=self.batch_size,
                lang=self.lang,
                verbose=self.verbose
            )

            # Remap the scores to the summaries
            index = 0
            metrics_lists = []
            for i, summaries in enumerate(summaries_list):
                metrics_lists.append([])
                for j, summary in enumerate(summaries):
                    if (i, j) in empty_inputs:
                        precision, recall, f1 = 0.0, 0.0, 0.0
                    else:
                        precision = precisions[index].item()
                        recall = recalls[index].item()
                        f1 = f1s[index].item()
                        index += 1

                    metrics_lists[-1].append(MetricsDict({
                        'bertscore': {
                            'precision': precision,
                            'recall': recall,
                            'f1': f1,
                        }
                    }))

            return metrics_lists

        def score_multi_all(self,
                            summaries_list: List[List[SummaryType]],
                            references_list: List[List[ReferenceType]]) -> List[List[MetricsDict]]:
            return self._run(summaries_list, references_list)


@MetricSetupSubcommand.register('bertscore')
class BertScoreSetupSubcommand(MetricSetupSubcommand):
    @overrides
    def add_subparser(self, parser: argparse._SubParsersAction):
        description = 'Setup the BERTScore metric'
        self.parser = parser.add_parser('bertscore', description=description, help=description)
        self.parser.set_defaults(subfunc=self.run)

    @overrides
    def run(self, args):
        try:
            import bert_score
            print('BertScore setup success')
        except ImportError:
            print('Please pip install "bert_score" to complete setup')