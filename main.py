from pkg.repository.data_repository import DataRepository
from pkg.services.matchs_service import MatchsService
from pkg.config.dataset_configuration import (
    DatasetConfiguration,
    volleyball_configuration,
)
from pkg.services.stats_service import StatsService


def main():

    configuration: DatasetConfiguration = volleyball_configuration

    repository = DataRepository(
        file=configuration.dataset_path_match,
        adapter=configuration.adapter_match,
        sep=configuration.dataset_sep_match,
    )

    MatchsService(
        adapter=configuration.adapter_match, repository=repository
    ).display_matchs()

    print(StatsService(matches=repository.load()).compute_ranking())


if __name__ == "__main__":
    main()
