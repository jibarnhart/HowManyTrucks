def cleaning(pieces, needed_equipment):

    for piece in pieces:
        if needed_equipment in ['dry van', 'reefer']:
            if piece['stackable']:
                piece['modified_height'] = piece['height']
            else:
                piece['modified_height'] = 108
            piece['modified_width'] = piece['width']
            
        elif needed_equipment == 'flatbed':
            if piece['stackable']:
                piece['modified_height'] = piece['height']
            else:
                piece['modified_height'] = 102

            if piece['height'] > 102:
                piece['over_height'] = True
            else:
                piece['over_height'] = False

            if piece['width'] > 102:
                piece['over_width'] = True
                piece['modified_width'] = piece['width']
            else:
                piece['over_width'] = False
                piece['modified_width'] = piece['width']

    return pieces