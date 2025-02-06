def generate_health_report(metadata_list):
    report = {
        'total_tracks': len(metadata_list),
        'missing_isrc': 0,
        'missing_metadata': {}
    }

    for metadata in metadata_list:
        for key, value in metadata.items():
            if not value:
                report['missing_metadata'].setdefault(key, 0)
                report['missing_metadata'][key] += 1
        if not metadata.get('isrc'):
            report['missing_isrc'] += 1

    return report
