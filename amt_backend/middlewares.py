def cors_middleware(get_response):

    def middleware(request):
        # code to execute before calling view
        response = get_response(request)

        # code to execute after calling view
        response.headers['Access-Control-Allow-Origin'] = "*"
        # response.headers['Access-Control-Allow-Methods'] = "POST,OPTIONS"
        response.headers['Access-Control-Allow-Headers'] = "Content-Type"
        return response

    return middleware
