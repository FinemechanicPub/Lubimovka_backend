import logging
from datetime import datetime as dt

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from apps.main.models import SettingGoogleExport
from config.settings.base import GOOGLE_PRIVATE_KEY, GOOGLE_PRIVATE_KEY_ID

PRIVATE_KEY = GOOGLE_PRIVATE_KEY
PRIVATE_KEY_ID = GOOGLE_PRIVATE_KEY_ID

SCOPES = "https://www.googleapis.com/auth/spreadsheets"
PATH = "https://lubimovka.kiryanov.ru"

logging.basicConfig()
logger = logging.getLogger(__name__)


def get_keys():
    KEYS = {
        "type": "service_account",
        "private_key": PRIVATE_KEY,
        "private_key_id": PRIVATE_KEY_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    }
    dict = {
        "project_id": "GOOGLE_PROJECT_ID",
        "client_email": "GOOGLE_CLIENT_EMAIL",
        "client_id": "GOOGLE_CLIENT_ID",
        "client_x509_cert_url": "GOOGLE_CLIENT_X509_CERT_URL",
    }
    for key, value in dict.items():
        KEYS[key] = SettingGoogleExport.objects.get(settings_key=value).text
    return KEYS


def build_service():
    KEYS = get_keys()
    scopes = [SCOPES]
    try:
        credentials = service_account.Credentials.from_service_account_info(KEYS)
    except ValueError as error:
        logger.error(error, exc_info=True)
        return
    scoped_credentials = credentials.with_scopes(scopes)
    return build("sheets", "v4", credentials=scoped_credentials)


def get_instance_values(instance) -> dict:
    instance_created = str(dt.now().date())
    instance_file_path = PATH + str(instance.file.url)
    instance_number = "---"
    return {
        "values": [
            [
                instance_number,
                instance_created,
                instance.first_name,
                instance.last_name,
                instance.birth_year,
                instance.city,
                str(instance.phone_number),
                instance.email,
                instance.year,
                instance.title,
                instance_file_path,
            ]
        ]
    }


def get_sheet_id_by_title():
    SPREADSHEET_ID = SettingGoogleExport.objects.get(settings_key="SPREADSHEET_ID").text
    SHEET = SettingGoogleExport.objects.get(settings_key="SHEET").text
    service = build_service()
    try:
        spreadsheet = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
        for _sheet in spreadsheet["sheets"]:
            if _sheet["properties"]["title"] == SHEET:
                return _sheet["properties"]["sheetId"]
    except HttpError as error:
        logger.error(error, exc_info=True)
        return
    service.spreadsheets().close()


def set_borders():
    SPREADSHEET_ID = SettingGoogleExport.objects.get(settings_key="SPREADSHEET_ID").text
    sheet_id = get_sheet_id_by_title()
    service = build_service()
    body = {
        "includeSpreadsheetInResponse": False,
        "requests": [
            {  # настраиваем границы
                "updateBorders": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 0,
                        "endRowIndex": 200,
                        "startColumnIndex": 0,
                        "endColumnIndex": 11,
                    },
                    "bottom": {"style": "SOLID", "width": 1, "color": {"red": 0, "green": 0, "blue": 0, "alpha": 1}},
                    "innerHorizontal": {
                        "style": "SOLID",
                        "width": 1,
                        "color": {"red": 0, "green": 0, "blue": 0, "alpha": 1},
                    },
                    "innerVertical": {
                        "style": "SOLID",
                        "width": 1,
                        "color": {"red": 0, "green": 0, "blue": 0, "alpha": 1},
                    },
                    "right": {"style": "SOLID", "width": 1, "color": {"red": 0, "green": 0, "blue": 0, "alpha": 1}},
                },
            },
            {  # настраиваем ячейки заголовка
                "repeatCell": {
                    "range": {"sheetId": sheet_id, "startRowIndex": 0, "endRowIndex": 1},
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
                            "horizontalAlignment": "CENTER",
                            "textFormat": {
                                "foregroundColor": {"red": 0.0, "green": 0.0, "blue": 0.0},
                                "fontSize": 10,
                                "bold": True,
                            },
                        },
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)",
                },
            },
            {  # закрепляем заголовок
                "updateSheetProperties": {
                    "properties": {
                        "sheetId": sheet_id,
                        "gridProperties": {"frozenRowCount": 1},
                    },
                    "fields": "gridProperties.frozenRowCount",
                },
            },
        ],
    }
    request = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=body,
    )
    try:
        request.execute()
    except HttpError as error:
        logger.error(error, exc_info=True)
        return
    service.spreadsheets().close()


def set_header():
    SPREADSHEET_ID = SettingGoogleExport.objects.get(settings_key="SPREADSHEET_ID").text
    RANGE = (
        SettingGoogleExport.objects.get(settings_key="SHEET").text + "!A1"
    )  # header starts at position "SheetTitle!A1"
    service = build_service()
    body = {
        "data": [
            {
                "range": RANGE,
                "values": [
                    [
                        "Номер",
                        "Дата создания заявки",
                        "Имя",
                        "Фамилия",
                        "Год рождения",
                        "Город",
                        "Телефон",
                        "Электронная почта",
                        "Год написания",
                        "Название",
                        "Ссылка на файл",
                    ]
                ],
            }
        ],
        "valueInputOption": "USER_ENTERED",
    }
    request = (
        service.spreadsheets()
        .values()
        .batchUpdate(
            spreadsheetId=SPREADSHEET_ID,
            body=body,
        )
    )
    try:
        request.execute()
    except HttpError as error:
        logger.error(error, exc_info=True)
        return
    service.spreadsheets().close()


def export_new_object(instance) -> None:
    SPREADSHEET_ID = SettingGoogleExport.objects.get(settings_key="SPREADSHEET_ID").text
    RANGE = SettingGoogleExport.objects.get(settings_key="SHEET").text
    value_input_option = "USER_ENTERED"
    body = get_instance_values(instance)
    service = build_service()
    request = (
        service.spreadsheets()
        .values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE,
            valueInputOption=value_input_option,
            body=body,
        )
    )
    try:
        request.execute()
    except HttpError as error:
        logger.error(error, exc_info=True)
        return
    service.spreadsheets().close()
