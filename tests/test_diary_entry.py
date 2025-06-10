from lib.diary_entry import *

def test_instantiation():
    entry = DiaryEntry('title', 'copy copy copy')
    assert entry.title == 'title'
    assert entry.contents == 'copy copy copy'

def test_format():
    entry = DiaryEntry('title', 'copy copy copy')
    assert entry.format() == 'title: copy copy copy'

def test_count_words():
    entry = DiaryEntry('title', 'copy copy copy')
    assert entry.count_words() == 4

def test_reading_time():
    entry = DiaryEntry('title', 'copy copy copy')
    assert entry.reading_time(1) == 4

def test_reading_chunk_once():
    entry = DiaryEntry('title', 'copy copy copy')
    chunk = entry.reading_chunk(1, 3)
    assert chunk == 'title: copy copy'

def test_reading_chunk_twice():
    entry = DiaryEntry('title', 'copy copy copy')
    chunk_1 = entry.reading_chunk(1, 2)
    chunk_2 = entry.reading_chunk(1, 2)
    assert chunk_1 == 'title: copy'
    assert chunk_2 == 'copy copy'

def test_reading_chunk_thrice():
    entry = DiaryEntry('title', 'copy copy copy')
    chunk_1 = entry.reading_chunk(1, 1)
    chunk_2 = entry.reading_chunk(1, 1)
    chunk_3 = entry.reading_chunk(1, 2)
    assert chunk_1 == 'title:'
    assert chunk_2 == 'copy'
    assert chunk_3 == 'copy copy'