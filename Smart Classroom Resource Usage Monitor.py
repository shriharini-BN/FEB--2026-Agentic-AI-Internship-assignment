def resource_monitor(usage):
    overused = []

    for resource in usage:
        if usage[resource] > 8:
            overused.append(resource)

    if len(overused) > 0:
        print("Overused Resources:", ",".join(overused))
        print("Energy Alert: Yes")
    else:
        print("Overused Resources: None")
        print("Energy Alert: No")
usage = {
    "Projector": 6,
    "AC": 9,
    "Lights": 4
}
resource_monitor(usage)