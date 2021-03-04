import events_by_date
from datetime import datetime, timedelta
from pytest import fixture


@fixture
def last_week_event():
    last_week = (datetime.utcnow() - timedelta(days=7)).isoformat()
    return {'event_dates': {'starting_day': last_week}}


@fixture
def next_week_event():
    next_week = (datetime.utcnow() + timedelta(days=7)).isoformat()
    return {'event_dates': {'starting_day': next_week}}


@fixture
def next_year_event():
    next_year = (datetime.utcnow() + timedelta(days=365)).isoformat()
    return {'event_dates': {'starting_day': next_year}}


def test_swap_two_events(last_week_event, next_week_event, next_year_event):
    events = [next_year_event, next_week_event, last_week_event]
    events_by_date.swap(events, 0, 2)
    assert events == [last_week_event, next_week_event, next_year_event]


def test_get_start_time():
    event_with_date = {'event_dates': {'starting_day': '2022-01-01T12:00:00Z'}}
    assert '2022-01-01T12:00:00Z' == events_by_date.get_start_time(
        event_with_date)


def test_get_start_time_with_no_starting_day():
    event_with_no_date = {'event_dates': {'starting_day': None}}
    assert '' == events_by_date.get_start_time(event_with_no_date)


def test_get_name_returns_english_name_when_finnish_does_not_exist():
    tapahtuma = {'name': {'fi': None, 'en': 'Christmas'}}
    assert 'Christmas' == events_by_date.get_name(tapahtuma)


def test_get_name_returns_finnish_name_when_both_english_and_finnish_exist():
    event_with_two_names = {'name': {'fi': 'Joulu', 'en': 'Christmas'}}
    assert 'Joulu' == events_by_date.get_name(event_with_two_names)


def test_bubble_sort(last_week_event, next_week_event, next_year_event):
    events = [next_year_event, last_week_event, next_week_event]

    events_by_date.bubble_sort(events)

    assert events == [last_week_event, next_week_event, next_year_event]


def test_next_month_filter(last_week_event, next_week_event, next_year_event):
    events = [last_week_event, next_week_event, next_year_event]
    filtered = list(filter(events_by_date.next_month_filter, events))

    assert filtered == [next_week_event]
