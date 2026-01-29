from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden

erro_403_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>403 Forbidden</title>
    <style>
        /* General Styles */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f3f4f6;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            text-align: center;
            padding: 30px;
            max-width: 400px;
            width: 100%;
        }

        h1 {
            font-size: 32px;
            color: #e3342f;
            margin-bottom: 20px;
        }

        p {
            font-size: 16px;
            color: #4a4a4a;
            margin-bottom: 20px;
        }

        a {
            display: inline-block;
            padding: 12px 24px;
            background-color: #3490dc;
            color: #ffffff;
            font-weight: bold;
            text-decoration: none;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s, box-shadow 0.3s;
        }

        a:hover {
            background-color: #2779bd;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>403 - Access Forbidden</h1>
        <p>Sorry, you are not authorized to access this page.</p>
        <a href="/">Return to Home</a>
    </div>
</body>
</html>

"""

def login_and_role_required(required_role):
  def decorator(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
      user = request.user
      if required_role == "customer" and not user.is_customer:
        return HttpResponseForbidden(erro_403_html)
      if required_role == "seller" and not user.is_seller:
        return HttpResponseForbidden(erro_403_html)
      return view_func(request, *args, **kwargs)
    return _wrapped_view
  return decorator
