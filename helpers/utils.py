def get_timer(length:float,type:str='long'):
    h = length // 3600
    m = length % 3600 // 60
    s = length % 3600 % 60
    if type=='short':
        return f"{h}h {f'0{m}' if m < 10 else m}m"

    if type=='min':
        return f"{f'0{m}' if m < 10 else m}min"

    else:
        if h>=1:
            return f"{h}:{f'0{m}' if m < 10 else m}:{f'0{round(s)}' if s < 10 else round(s)}"
        else:
            return f"{f'0{int(m)}' if m < 10 else m}:{f'0{round(s)}' if s < 10 else round(s)}"


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip