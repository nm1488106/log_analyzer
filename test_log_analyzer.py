from log_analyzer import analyze_logs


def test_log_counts(tmp_path):
    log_file = tmp_path / "test.log"

    log_file.write_text(
        "INFO: Started\n"
        "WARNING: High memory\n"
        "ERROR: Failed\n"
        "INFO: Restarted\n"
    )

    result = analyze_logs(str(log_file))

    assert result["INFO"] == 2
    assert result["WARNING"] == 1
    assert result["ERROR"] == 1


def test_empty_log(tmp_path):
    log_file = tmp_path / "empty.log"
    log_file.write_text("")

    result = analyze_logs(str(log_file))

    assert result["INFO"] == 0
    assert result["WARNING"] == 0
    assert result["ERROR"] == 0