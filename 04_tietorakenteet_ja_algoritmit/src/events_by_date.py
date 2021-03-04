import urllib.request
import json
from datetime import datetime, timedelta

EVENTS_API_URL = 'http://open-api.myhelsinki.fi/v1/events/'


def get_events():
    with urllib.request.urlopen(EVENTS_API_URL) as response:
        json_response = json.load(response)
        return json_response['data']


def next_month_filter(event):
    now = datetime.utcnow()
    next_month = now + timedelta(days=30)

    min = now.isoformat()
    max = next_month.isoformat()

    return get_start_time(event) != '' and min <= get_start_time(event) <= max


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def get_start_time(event):
    return event['event_dates']['starting_day'] or ''


def get_name(event):
    return (event['name']['fi'] or event['name']['en'] or '').strip()


def bubble_sort(events):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(events) - 1):
            if get_start_time(events[i]) > get_start_time(events[i+1]):
                swapped = True
                swap(events, i, i+1)


def get_events_next_month():
    all_events = get_events()
    next_month = list(filter(next_month_filter, all_events))
    return next_month


def main():
    events = get_events_next_month()
    bubble_sort(events)

    latest_date = ''

    for event in events:
        # esim. '2022-01-01T12:00:00Z' tai ''
        event_start = get_start_time(event)

        date = event_start[:10]     # '2022-01-01' tai ''
        time = event_start[11:16]   # '12:00' tai ''
        name = get_name(event)

        if date != latest_date:
            print()
            print(date)  # tulostetaan uusi päivämäärä
            latest_date = date

        print(f' { time } { name }')


if __name__ == "__main__":
    main()
