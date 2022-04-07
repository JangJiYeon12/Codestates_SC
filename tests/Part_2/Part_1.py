from openaq import OpenAQ
api = OpenAQ()

def test_get_results(get_results_func):
    func = get_results_func()
    results = func()
    assert type(results) == list
    assert len(results) >= 1
    for item in results:
        assert type(item) == tuple

