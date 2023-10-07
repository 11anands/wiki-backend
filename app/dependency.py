

def paginate(page_num: int, page_size: int, data, data_length, url):
    """
    Pagination dependency function to provide data with a limit and an offset
    """
    start = (page_num - 1) * page_size
    end = start + page_size
    response = {
        "data": data[start:end],
        "total": data_length,
        "count": page_size,
        "page_num": page_num,
        "pagination": {}
    }
    if end >= data_length:
        response["pagination"]["next"] = None
        if page_num > 1:
            response["pagination"]["previous"] = f"/{url}?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None
    else:
        if page_num > 1:
            response["pagination"]["previous"] = f"/{url}?page_num={page_num-1}&page_size={page_size}"
        else:
            response["pagination"]["previous"] = None
        response["pagination"]["next"] = f"/{url}?page_num={page_num+1}&page_size={page_size}"
    return response

