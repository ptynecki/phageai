from phageai.lifecycle.classifier import LifeCycleClassifier


def test_invalid_access_token_and_fasta_file():
    """
    Test API reaction on invalid access token and FASTA file
    """

    lcc = LifeCycleClassifier(access_token='INVALID_TOKEN')

    result = lcc.predict(fasta_path='INVALID_FASTA_FILE')

    assert result == {}


def test_empty_access_token():
    """
    Test API reaction on empty access token
    """

    lcc = LifeCycleClassifier(access_token='')

    result = lcc.predict(fasta_path='INVALID_FASTA_FILE')

    assert result == {}


def test_null_access_token():
    """
    Test API reaction on null access token
    """

    lcc = LifeCycleClassifier(access_token=None)

    result = lcc.predict(fasta_path='INVALID_FASTA_FILE')

    assert result == {}


def test_random_access_token():
    """
    Test API reaction on random access token
    """

    lcc = LifeCycleClassifier(access_token='16fd2706-8baf-433b-82eb-8c7fada847da')

    result = lcc.predict(fasta_path='INVALID_FASTA_FILE')

    assert result == {}
