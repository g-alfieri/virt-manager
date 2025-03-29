
def add_evdev_device(xml, device_path, grab_toggle="ctrl-ctrl"):
    """
    Aggiunge un dispositivo evdev all'XML della VM.
    """
    evdev_xml = ("<input type='evdev' dev='{device}' grab='all' repeat='on' grabToggle='{grab_toggle}'/>"
                 .format(device=device_path, grab_toggle=grab_toggle))
    xml.append(evdev_xml)
