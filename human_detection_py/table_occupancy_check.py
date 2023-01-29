zone_count_records = []
FPS = 15
zone_count = []

def is_table_occupied(record):
    result = []
    for zone_id in range(len(record[0])):
        # Cumulative avg >= 0.75 to filter out noise e.g. people passing by
        result.append(sum([row[zone_id] for row in record])/len(record) >= 0.75)
    return result

if len(zone_count_records) > FPS * 3:  # Records 3s history
    zone_count_records.pop(0)
zone_count_records.append(zone_count_output["zone_count"])
table_occupation = is_table_occupied(zone_count_records)