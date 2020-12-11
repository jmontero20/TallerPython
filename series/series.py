def slices(series, length):
    if length > len(series) or length <= 0 or not series:
        raise ValueError("Invalid Input")
    array = []
    for i in range(0, len(series)-length+1):
        array.append(series[i:i+length])
    return array
