from app.models.events import Meta


def get_events(regions):
    events_model = Meta()
    output = events_model.to_dict(regions)

    return output
