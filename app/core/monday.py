import monday

from .config import settings

monday_client = monday.MondayClient(api_key=settings.MONDAY_API_KEY)
