from django.http import HttpResponse
from django.db import connection

def home(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()[0]
        return HttpResponse(f"✅ Connected to MySQL database: {db_name}")
    except Exception as e:
        return HttpResponse(f"❌ Database connection failed: {e}")