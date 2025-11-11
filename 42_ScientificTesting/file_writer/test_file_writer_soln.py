import file_writer


class MockFM:
    def __init__(self):
        self.one = None
        self.two = []
        self.three = None

    def save_1(self, value):
        self.one = value

    def save_2(self, values):
        self.two = values

    def save_3(self, value):
        self.three = value


def test_compute_value_2_draws_size():
    dp = file_writer.DataProcessor()
    dp.compute_value_2(7)

    # One solution: mock the file manager
    # Could also consider making the members accessible for testing
    # or reading the files from disk for the real version, plus cleanup
    mock_fm = MockFM()
    dp.write_files(mock_fm)
    assert len(mock_fm.two) == 7
