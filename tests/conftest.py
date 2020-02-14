from pathlib import Path
import pytest


@pytest.fixture
def test_data_dir():
    return Path(__file__).absolute().parent.joinpath('data')


@pytest.fixture
def input_paths(test_data_dir):
    return [test_data_dir.joinpath('ref_%d.vcf' % i) for i in range(1, 7)]


@pytest.fixture
def ref_merged(test_data_dir):
    return test_data_dir.joinpath('ref_merged.vcf')


@pytest.fixture
def invalid_vcf_file_path(test_data_dir):
    return test_data_dir.joinpath('ref_invalid.vcf')
