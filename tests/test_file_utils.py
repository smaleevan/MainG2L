"""Tests for file utility functions."""

import os
import tempfile

import pytest
from utils.file_utils import (
    read_lines,
    write_lines,
    file_exists,
    count_lines,
)


@pytest.fixture
def tmp_file(tmp_path):
    """Return a path to a temporary file with three lines."""
    path = tmp_path / "sample.txt"
    path.write_text("line one\nline two\nline three", encoding="utf-8")
    return str(path)


class TestReadLines:
    def test_reads_all_lines(self, tmp_file):
        lines = read_lines(tmp_file)
        assert lines == ["line one", "line two", "line three"]

    def test_missing_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            read_lines(str(tmp_path / "missing.txt"))


class TestWriteLines:
    def test_writes_and_reads_back(self, tmp_path):
        path = str(tmp_path / "out.txt")
        write_lines(path, ["alpha", "beta", "gamma"])
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        assert content == "alpha\nbeta\ngamma"

    def test_overwrites_existing(self, tmp_file):
        write_lines(tmp_file, ["new content"])
        with open(tmp_file, "r", encoding="utf-8") as fh:
            content = fh.read()
        assert content == "new content"


class TestFileExists:
    def test_existing_file(self, tmp_file):
        assert file_exists(tmp_file) is True

    def test_missing_file(self, tmp_path):
        assert file_exists(str(tmp_path / "no_such_file.txt")) is False

    def test_directory_returns_false(self, tmp_path):
        assert file_exists(str(tmp_path)) is False


class TestCountLines:
    def test_count_three_lines(self, tmp_file):
        assert count_lines(tmp_file) == 3

    def test_single_line(self, tmp_path):
        path = tmp_path / "one.txt"
        path.write_text("only one line", encoding="utf-8")
        assert count_lines(str(path)) == 1

    def test_missing_file_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            count_lines(str(tmp_path / "missing.txt"))
