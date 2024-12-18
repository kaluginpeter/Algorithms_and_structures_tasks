# Convert DD (decimal degrees) position to DMS (degrees, minutes, seconds).
#
# Inputs:
# dd_lat and dd_lon 2 floats representing the latitude and the longitude in degree -i.e. 2 floats included in [-90, 90] and [-180, 180]. Note that latitude 0 is north, longitude 0 is east.
#
# Outputs:
# A tuple of DMS latitudes formated as follows: DDD*mm'ss.sss"C
#
# With:
#
# DDD: degrees
# mm: minutes
# ss.sss: seconds rounded to 3 decimals
# C: first letter uppercase of the cardinal direction
# ressources
# about WGS 84 on Wikipedia
#
# StringsFundamentals
# Solution
def convert_to_dms(dd_lat, dd_lon):
    def dd_to_dms(dd, is_latitude):
        if is_latitude:
            direction = 'N' if dd >= 0 else 'S'
        else:
            direction = 'E' if dd >= 0 else 'W'
        dd = abs(dd)
        degrees = int(dd)
        minutes = int((dd - degrees) * 60)
        seconds = (dd - degrees - minutes / 60) * 3600
        seconds_rounded = round(seconds, 3)
        dms = f"{degrees:03d}*{minutes:02d}'{seconds_rounded:06.3f}\"{direction}"
        return dms
    dms_lat = dd_to_dms(dd_lat, True)
    dms_lon = dd_to_dms(dd_lon, False)
    return (dms_lat, dms_lon)